import redis, time # pip install redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
try:
    r.delete('name')
except:
    pass
print(r.set('name', 'Dicky', xx=True)) # xx then set => modify, so Dicky ignored, return None
print(r.set('name', 'Ricky', nx=True)) # return True
print(r['name']) # Ricky
print(r.set('name', 'Micky', nx=True)) # return None
print(r['name']) # nx then set => create, so Micky ignored, so Ricky

