import os
class Config:
    # Flask Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    # Azure SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    # Microsoft Entra ID (Azure AD)
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    # Construct Database Connection String (ODBC)
    @staticmethod
    def get_db_connection_string():
        return (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server=tcp:{Config.SQL_SERVER},1433;"
            f"Database={Config.SQL_DATABASE};"
            f"Uid={Config.SQL_USER_NAME};"
            f"Pwd={Config.SQL_PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
