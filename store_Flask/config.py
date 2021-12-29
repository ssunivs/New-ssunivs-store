from .ssunivs.dbsetting import db as dbsetting
db = {
    'user'     :  dbsetting['user'],
    'password' :  dbsetting['password'],
    'host'     :  dbsetting['host'],
    'port'     :  dbsetting['port'],
    'database' : dbsetting['database']
}
SQLALCHEMY_DATABASE_URL = "mysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 