from app.tenant_extensions import TenantBase
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.utils.softDeleteMixin import SoftDeleteMixin

class User(TenantBase, SoftDeleteMixin):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    first_name= Column(String(100), nullable=False)
    middle_name= Column(String(100), nullable=True)
    last_name=Column(String(100), nullable=False)

    company_name=Column(String(100), nullable=True)
    company_phone=Column(String(100), nullable=True)

    company_email=Column(String(100), nullable=True, unique=True)
    company_address=Column(String(100), nullable=True)
    city=Column(String(100), nullable=True)
    state=Column(String(100), nullable=True)
    pincode=Column(String(100), nullable=True)
    country=Column(String(100), nullable=True)

    aadhar_card=Column(String(20), nullable=True, unique=True)
    phone= Column(String(20), nullable=True, unique=True)
    date_of_joining=Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name}>"
