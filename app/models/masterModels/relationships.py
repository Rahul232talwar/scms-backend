from app.models.masterModels.masterAdmin import MasterAdmin
from app.models.masterModels.tenantDB import TenantDB
from app.extensions import db


def register_relationships():

    # MasterAdmin → TenantDB (hasOne)
    MasterAdmin.tenantDB = db.relationship(
        "TenantDB",
        back_populates="masterAdmin",
        uselist=False,
        cascade="all, delete",
        lazy="selectin"
    )

    # TenantDB → MasterAdmin (belongsTo)
    TenantDB.masterAdmin = db.relationship(
        "MasterAdmin",
        back_populates="tenantDB",
        lazy="joined"
    )