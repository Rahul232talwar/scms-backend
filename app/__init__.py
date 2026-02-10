from flask import Flask
from sqlalchemy import text
from .extensions import db, migrate
# from .blueprints.admin_panel import admin_panel_bp
from .blueprints.admin_blueprints.admin import admin_bp
from .blueprints.health import health_bp
from .models.masterModels.relationships import register_relationships

def create_app(config_name="development"):
    app = Flask(__name__)

    # Load config
    app.config.from_object(f"config.{config_name.capitalize()}Config")

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register relationships
    register_relationships()

    # Register blueprints
    app.register_blueprint(admin_bp, url_prefix="/register")
    # app.register_blueprint(admin_panel_bp, url_prefix="/admin-panel")
    app.register_blueprint(health_bp, url_prefix="/health")

    # ✅ DB Connection Check
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print("✅ Database connected successfully")
            db.create_all()
            print("✅ All tables created successfully")
        except Exception as e:
            print("❌ Database connection failed:", e)

    return app
