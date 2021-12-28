from .db import db as dbsetting
db = {
    'user'     :  dbsetting['user'],
    'password' :  dbsetting['password'],
    'host'     :  dbsetting['host'],
    'port'     :  dbsetting['port'],
    'database' : dbsetting['database']
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 