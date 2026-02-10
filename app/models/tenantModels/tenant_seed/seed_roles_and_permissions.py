from app.models.tenantModels.Role_And_Permission.role import Role
from app.models.tenantModels.Role_And_Permission.permission import Permission
from app.models.tenantModels.Role_And_Permission.role_and_permission import RoleAndPermission
from .role_seed import role_mapping
from .permission_seed import role_permissions_map

def seed_roles_and_permissions(session):    
    for role_key, role_name in role_mapping.items():
        role = session.query(Role).filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name, description=f"{role_key} role")
            session.add(role)
            session.flush()
        permissions = role_permissions_map.get(role_name,[])
        for per in permissions:
            permission = session.query(Permission).filter_by(name=per).first()
            if not permission:
                permission = Permission(name=per, description=f"Permission to {per}")
                session.add(permission)
                session.flush()
            role_and_permission = RoleAndPermission(role_id=role.id, permission_id=permission.id)
            session.add(role_and_permission)
            session.flush()    
    session.commit()

      
