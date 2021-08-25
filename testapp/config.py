import os


class Config:
    MONGO_USERNAME = os.getenv('MONGO_USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
    MONGO_DB_IP = os.getenv('MONGO_DB_IP')
