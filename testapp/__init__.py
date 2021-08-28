from flask import Flask
from testapp.config import Config
from testapp.dbwork import MongoDB
from testapp.utils import Utils


app = Flask(__name__)
varenv = Config()
mondb = MongoDB(username=varenv.MONGO_USERNAME,
                password=varenv.MONGO_PASSWORD,
                ip=varenv.MONGO_DB_IP,
                dbname=varenv.MONGO_DB_NAME)
util = Utils()


from testapp import routes
