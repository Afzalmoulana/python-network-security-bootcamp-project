#1
import hashlib

string = input()
result = hashlib.md5(string.encode())  # encode():Converts the string into bytes to be acceptable by hash function
print(result.hexdigest())              # hexdigest():Returns the encoded data in hexadecimal format

#2
result = hashlib.sha224(string.encode())
print(result.hexdigest())

result = hashlib.sha1(string.encode())
print(result.hexdigest())

result = hashlib.sha256(string.encode())
print(result.hexdigest())