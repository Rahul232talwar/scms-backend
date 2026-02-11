import os
import pymysql
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from app.models.masterModels.tenantDB import TenantDB
load_dotenv()

TenantBase = declarative_base()

def get_tenant_session(DB_NAME):
    
    if not create_tenant_database(DB_NAME):
        return None, None
    
    DB_USER=os.getenv("DB_USER")
    DB_PASSWORD=quote_plus(os.getenv("DB_PASSWORD"))
    DB_HOST=os.getenv("DB_HOST")
    DB_PORT=os.getenv("DB_PORT")
    db_url=(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return {"engine":engine, "session": Session()}
    
  

def create_tenant_database(DB_NAME):

    connection = None
    cursor = None
    try:
        DB_USER=os.getenv("DB_USER")
        DB_PASSWORD=os.getenv("DB_PASSWORD")
        DB_HOST=os.getenv("DB_HOST")

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")

        return True
    except Exception as e:
        raise RuntimeError(f"Failed to create database: {str(e)}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        

def get_dbName(company_name):
    masterAdmin = TenantDB.query.filter_by(slug=company_name).first()
    if not masterAdmin:
        raise ValueError("Company not found")
        
    return masterAdmin.dbName