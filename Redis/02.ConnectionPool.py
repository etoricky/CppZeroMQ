import redis # pip install redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'Ricky')
print(r['name'])
print(r.get('name'))
# print(r.get('firstname', 'empty')) not really a dict
print(type(r.get('name')))

r.set('age', 32)
print(r.get('age'))
print(type(r.get('age'))) # also str although input is int 32

