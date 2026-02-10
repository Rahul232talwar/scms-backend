import uuid
from app.extensions import db


class TenantDB(db.Model):
    __tablename__ = "tenant_dbs"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    masterAdminId = db.Column(
        db.String(36),
        db.ForeignKey("master_admins.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        unique=True
    )

    dbName = db.Column(db.String(100), nullable=False, unique=True)
    dbUser = db.Column(db.String(100), nullable=False)
    dbPassword = db.Column(db.String(200), nullable=False)
    dbHost = db.Column(db.String(100), nullable=False)

    slug = db.Column(db.String(100), nullable=False, unique=True, index=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<TenantDB id={self.id} dbName={self.dbName}"