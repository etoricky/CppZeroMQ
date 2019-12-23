import redis, time # pip install redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'Ricky', ex=3)
time.sleep(2.99)
print(r.get('name')) # Ricky
time.sleep(0.02)
print(r.get('name')) # None

