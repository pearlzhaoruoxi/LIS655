import hashlib

data = b'\x77'
print(hashlib.md5(data).hexdigest())

with open('tiny-file', 'wb') as f:
  f.write(data)

data = b'\x78'
print(hashlib.md5(data).hexdigest())

with open('tiny-file-2', 'wb') as f:
  f.write(data)
