import pymysql
from yong.key import MYSQL_USER_PW, MYSQL_USER_ID
MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user=MYSQL_USER_ID,
    passwd=MYSQL_USER_PW,
    db='flask_db',
    charset='utf8'
)


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN