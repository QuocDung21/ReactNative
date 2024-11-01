# config.py
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER = os.getenv('DB_SERVER')
    PORT = os.getenv('DB_PORT')
    DATABASE = os.getenv('DB_NAME')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')

    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER},{PORT};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD}"
    )
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'DSJFHSDFUWEFHCNSDCWE')
