import sys
import hashlib

string = sys.stdin.readline().rstrip()

result = hashlib.sha256(string.encode())

print(result.hexdigest())