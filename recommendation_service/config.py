class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:yourStrong(!)Password@sqlserver/recommendationdb?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
    KAFKA_TOPIC = 'notifications'
