from gluon.contrib.redis_utils import RConn
from gluon.contrib.redis_cache import RedisCache
# connect to our redis cache
rconn = RConn('redis', 6379)
cache.redis = RedisCache(redis_conn=rconn, debug=True)
cache.ram = cache.disk = cache.redis

# use redis for sessions as well
from gluon.contrib.redis_session import RedisSession
sessiondb = RedisSession(redis_conn=rconn, session_expiry=3600 * 16, with_lock=True)
session.connect(request, response, db = sessiondb)
