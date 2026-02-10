from app.tenant_extensions import TenantBase
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.utils.softDeleteMixin import SoftDeleteMixin


class Role(TenantBase,SoftDeleteMixin):
    __tablename__ = "roles"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<Role id={self.id} name={self.name}>"
