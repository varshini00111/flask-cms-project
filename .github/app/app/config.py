import os

class Config:
    SQL_SERVER = os.getenv("SQL_SERVER")
    SQL_DATABASE = os.getenv("SQL_DATABASE")
    SQL_USER_NAME = os.getenv("SQL_USER_NAME")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")

    BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT")
    BLOB_CONTAINER = os.getenv("BLOB_CONTAINER")
    BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY")

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
