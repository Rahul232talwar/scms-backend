import uuid
from app.extensions import db


class MasterAdmin(db.Model):
    __tablename__ = "master_admins"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name= db.Column(db.String(50), nullable=False)
    middle_name= db.Column(db.String(50), nullable=True)
    last_name= db.Column(db.String(50), nullable=False)

    company_name= db.Column(db.String(150), nullable=False)
    company_email= db.Column(db.String(120), nullable=False, unique=True, index=True)
    company_phone= db.Column(db.String(20), nullable=False)
    company_address= db.Column(db.String(255), nullable=True)

    city= db.Column(db.String(100), nullable=True)
    state= db.Column(db.String(100), nullable=True)
    pincode= db.Column(db.String(10), nullable=True)
    country= db.Column(db.String(50), default="India")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<MasterAdmin id={self.id} email={self.companyEmail}>"