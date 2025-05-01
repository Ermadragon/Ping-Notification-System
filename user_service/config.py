import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:yourStrong(!)Password@sqlserver/userdb?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'supersecretkey')
