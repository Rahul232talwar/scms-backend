from app.tenant_extensions import TenantBase
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.utils.softDeleteMixin import SoftDeleteMixin

class RoleAndPermission(TenantBase, SoftDeleteMixin):
    __tablename__ = "role_and_permissions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    role_id = Column(
        String(36),
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False
    )

    permission_id = Column(
        String(36),
        ForeignKey("permissions.id", ondelete="CASCADE"),
        nullable=False
    )
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<RoleAndPermission id={self.id} role_id={self.role_id} permission_id={self.permission_id}>"
