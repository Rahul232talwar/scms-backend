import os
from app.extensions import db
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from app.models.masterModels.masterAdmin import MasterAdmin
from app.models.masterModels.tenantDB import TenantDB
from app.tenant_extensions import get_tenant_session
from app.utils.response import success_response, error_response
from app.tenant_extensions import TenantBase
from app.models.tenantModels.tenant_relationships import register_tenant_relationships
from app.models.tenantModels.tenant_seed.seed_roles_and_permissions import seed_roles_and_permissions
from app.models.tenantModels.user import User
from app.models.tenantModels.auth import Auth
from app.models.tenantModels.Role_And_Permission.role import Role
load_dotenv()

def admin_register(data):
    session = None
    try:
        email = data.get("email")
        password = data.get("password")
        company_name = data.get("company_name")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        required_fields = {
            "email": email,
            "password": password,
            "company_name": company_name,
            "first_name": first_name,
            "last_name": last_name
        }

        missing_fields = [field for field, value in required_fields.items() if not value]

        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        new_user, new_tenant = create_master_admin(data)

        engine, session = get_tenant_session(new_tenant.dbName)
  
        if not(engine and session):
            raise RuntimeError("FAILED_TO_INIT_TENANT_DB")
            
        register_tenant_relationships()
        TenantBase.metadata.create_all(engine)
        seed_roles_and_permissions(session)

        tenant_user,tenant_auth = create_tenant_admin(session, data)

        if not (tenant_user and tenant_auth):
            raise RuntimeError("FAILED_TO_CREATE_TENANT_ADMIN")

        data = {
            "admin_id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "company_name": new_user.company_name,
            "company_email": new_user.company_email,
            "company_phone": new_user.company_phone,
        }
       
        session.commit()
        db.session.commit()
        return success_response("Admin registered successfully", data, 201)
   
    except ValueError as e:
        db.session.rollback()
        return error_response("BAD_REQUEST", str(e), 400)

    except Exception as e:
        db.session.rollback()
        if session:
            session.rollback()
        return error_response("Registration failed", str(e), 500)

    finally:
        if session:
            session.close()

def create_master_admin(data):
  
    userExist = MasterAdmin.query.filter_by(company_email=data.get("companyEmail")).first()

    if userExist:
        raise ValueError("User already exists")

    new_user = MasterAdmin(
        first_name=data.get("first_name"),
        middle_name=data.get("middle_name"),
        last_name=data.get("last_name"),
        company_name=data.get("company_name"),
        company_email=data.get("company_email"),
        company_phone=data.get("company_phone"),
        company_address=data.get("company_address"),
        city=data.get("city"),
        state=data.get("state"),
        pincode=data.get("pincode"),
        country=data.get("country")
        )
    db.session.add(new_user)
    # db.session.commit()
    db.session.flush()

    companyName=data.get("company_name").replace(" ","_")

    hashed_db_password = generate_password_hash(os.getenv("DB_PASSWORD"))


    # Create tenant database entry
    new_tenant = TenantDB(
        masterAdminId = new_user.id,
        dbName = f"logistic_{companyName}",
        dbUser = os.getenv("DB_USER"),
        dbPassword = hashed_db_password,
        dbHost = os.getenv("DB_HOST"),
        slug= data.get("company_name")
    )

    db.session.add(new_tenant)
    db.session.flush()
    return new_user, new_tenant
    
def create_tenant_admin(session, data):
    tenant_user= User(
        first_name=data["first_name"],
        middle_name=data["middle_name"],
        last_name=data["last_name"],
        company_name=data["company_name"],
        company_email=data["company_email"],
        company_phone=data["company_phone"],
        company_address=data["company_address"],
        city=data["city"],
        state=data["state"],
        pincode=data["pincode"],
        country=data["country"]
    )
    session.add(tenant_user)
    session.flush()

    hashed_password = generate_password_hash(data.get("password"))
    tenant_role = session.query(Role).filter_by(name="super_admin").first()

    if not tenant_role:
        raise RuntimeError("SUPER_ADMIN_ROLE_NOT_FOUND")

    tenant_auth = Auth (
        email=data.get("email"),
        password=hashed_password,
        user_id=tenant_user.id,
        role_id= tenant_role.id
    )
    session.add(tenant_auth)
    session.flush()

    return tenant_user,tenant_auth