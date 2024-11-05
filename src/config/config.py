# # config.py
# import os
# from dotenv import load_dotenv
# from urllib.parse import quote_plus

# # Load environment variables from .env file
# load_dotenv()

# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SERVER = os.getenv('DB_SERVER')
#     PORT = os.getenv('DB_PORT')
#     DATABASE = os.getenv('DB_NAME')
#     USERNAME = os.getenv('DB_USER')
#     PASSWORD = os.getenv('DB_PASSWORD')

#     params = quote_plus(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#         f"SERVER={SERVER},{PORT};"
#         f"DATABASE={DATABASE};"
#         f"UID={USERNAME};"
#         f"PWD={PASSWORD}"
#     )
#     SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'DSJFHSDFUWEFHCNSDCWE')

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Cấu hình cho cơ sở dữ liệu chính
    DB_SERVER = os.getenv('DB_SERVER')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    # Kết nối cho cơ sở dữ liệu chính
    params = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER},{DB_PORT};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD}"
    )
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"

    # Cấu hình cho cơ sở dữ liệu thứ hai
    DB2_SERVER = os.getenv('DB2_SERVER')
    DB2_PORT = os.getenv('DB2_PORT')
    DB2_NAME = os.getenv('DB2_NAME')
    DB2_USER = os.getenv('DB2_USER')
    DB2_PASSWORD = os.getenv('DB2_PASSWORD')

    # Kết nối cho cơ sở dữ liệu thứ hai
    params2 = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB2_SERVER},{DB2_PORT};"
        f"DATABASE={DB2_NAME};"
        f"UID={DB2_USER};"
        f"PWD={DB2_PASSWORD}"
    )
    
    SQLALCHEMY_BINDS = {
        'db2': f"mssql+pyodbc:///?odbc_connect={params2}"
    }

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'DSJFHSDFUWEFHCNSDCWE')