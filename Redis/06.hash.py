import redis, time # pip install redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

name = 'login:128001'
r.hset(name, 'balance', 1000*1000)
r.hset(name, 'equity', 200000)
r.hmset(name, {'name':'Ricky','age':32})

print(r.hget(name, 'name')) # Ricky
print(r.hmget(name, ['balance', 'equity', 'age'])) # ['1000000', '200000', '32']
print(r.hmget(name, 'balance', 'equity', 'age')) # ['1000000', '200000', '32'], same as above
print(r.hlen(name)) # 4 for 4 keys
print(r.hgetall(name)) # {'balance': '1000000', 'equity': '200000', 'name': 'Ricky', 'age': '32'}
print(r.hkeys(name)) # ['balance', 'equity', 'name', 'age']
print(r.hvals(name)) # ['1000000', '200000', 'Ricky', '32']
print(r.hexists(name, 'name')) # True
print(r.hexists(name, 'phone')) # False

print(r.hdel(name, 'name', 'age', 'phone')) # 2 means 2 deleted
print(r.hgetall(name)) # {'balance': '1000000', 'equity': '200000'}

print(r.hincrbyfloat(name, 'equity', 123.45)) # 200123.45
