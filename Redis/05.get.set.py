import redis, time # pip install redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# mget
r.mset({'k3':'v3','k4':'v4'})
print(r.mget('k3','k4'))

# get set
r.set('equity', 200000)
print(r['equity'])
print(r.getset('equity', 201000))
print(r['equity']) # 201000

# getrange
r.set('mvp', 'Lebron James')
print(r.getrange('mvp', 0, 6)) # Lebron

# setbit
r.set('message', 'Hello')
r.setbit('message', 2, 1) # 1 means binary 0010
print(r.get('message')) # Hello to hello


