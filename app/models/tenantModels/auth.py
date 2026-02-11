from app.tenant_extensions import TenantBase
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.utils.softDeleteMixin import SoftDeleteMixin

class Auth(TenantBase, SoftDeleteMixin):
    __tablename__ = "auths"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email= Column(String(100), nullable=False, unique=True)
    password= Column(String(255), nullable=False)
    refresh_token = Column(String(500), nullable=True)
    user_id= Column(
        String(36),
        ForeignKey("users.id",ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
        )
    role_id= Column(
        String(36),
        ForeignKey("roles.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
        )
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<Auth id={self.id} email={self.email}>"
