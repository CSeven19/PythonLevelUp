import redis
import msgpack
class Fibonacci:

  def fib(self,n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return self.fib(n-1) + self.fib(n-2)


class RedisRpcServer:

  def __init__(self, redis_url, list_name, klass):
    self.client = redis.from_url(redis_url)
    self.list_name = list_name
    self.klass = klass

  def start(self):
    print("Starting RPC server for " + self.list_name)
    while True:
      channel, request = self.client.brpop('fib')
      request = msgpack.unpackb(request, encoding='utf-8')

      print("Working on request: " + request['id'])

      result = getattr(self.klass, request['method'])(*request['params'])

      reply = {
        'jsonrpc': '2.0',
        'result': result,
        'id': request['id']
      }

      self.client.rpush(request['id'], msgpack.packb(reply, use_bin_type=True))
      self.client.expire(request['id'], 30)


RedisRpcServer('redis://localhost:6379', 'fib', Fibonacci()).start()