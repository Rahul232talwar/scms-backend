from sqlalchemy.orm import relationship

from app.models.tenantModels.Role_And_Permission.role import Role
from app.models.tenantModels.Role_And_Permission.permission import Permission
from app.models.tenantModels.Role_And_Permission.role_and_permission import RoleAndPermission
from app.models.tenantModels.user import User
from app.models.tenantModels.auth import Auth

def register_tenant_relationships():
    Role.permissions = relationship(
        Permission,
        secondary=RoleAndPermission.__table__,
        back_populates="roles",
        lazy="selectin"
    )

    Permission.roles = relationship(
        Role,
        secondary=RoleAndPermission.__table__,
        back_populates="permissions",
        lazy="selectin"
    )

    User.auth = relationship(
        "Auth",
        back_populates="user",
        uselist=False,
        cascade="all, delete",
        lazy="selectin"
    )

    Auth.user = relationship(
        "User",
        back_populates="auth",
        lazy="joined"
    )

    Role.auth = relationship(
        "Auth",
        back_populates="role",
        uselist=False,
        cascade="all, delete",
        lazy="selectin"
    )

    Auth.role = relationship(
        "Role",
        back_populates="auth",
        lazy="joined"
    )

    