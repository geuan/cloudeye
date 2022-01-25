import redis
conn = redis.StrictRedis(host='106.54.119.58',port=6379,db=0,password="xuchuan")
conn.set('lv','zhenjiang')
name  = conn.get('lv')
print name

from redis.sentinel import Sentinel
sentinel = Sentinel([('192.168.19.138',26379)],socket_timeout=0.1)
master = sentinel.master_for('mymaster',socket_timeout=0.1)
slave = sentinel.slave_for('mymaster',socket_timeout=0.1)

master.set('ll','123')

m = slave.get('ll')
print m


# sentinel = Sentinel([('192.168.19.138',26379)],socket_timeout=0.1)
# master = sentinel.discover_master("mymaster")
# slave = sentinel.discover_slaves("mymaster")
# print master
# print slave


