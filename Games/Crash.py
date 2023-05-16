import hashlib
import hmac
import secrets

def generateHash(seed):
    hash_obj = hashlib.sha256(seed.encode('utf-8'))
    return hash_obj.hexdigest()

def divisible(hash, mod):
    val = 0
    o = len(hash) % 4
    for i in range(o if o > 0 else 0, len(hash), 4):
        val = ((val << 16) + int(hash[i:i+4], 16)) % mod
    return val == 0

def crashPointFromHash(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

serverSeed = generateHash(f'{secrets.randbelow(1000000)}') #possible security issue with the rand int, if implemented with real money, might want to use a more secure random integer gen.
salt = ""

crash_point = crashPointFromHash(serverSeed)
formatted_crash_point = "{:.2f}".format(crash_point)
print("Crash Point:", formatted_crash_point)



# iteration = 0
# for _ in range(1, 1000000):
#     server_seed = generateHash(str(secrets.randbelow(1000000)))
#     crash_point = crashPointFromHash(server_seed)
#     formatted_crash_point = "{:.2f}".format(crash_point)
#     print("Crash Point:", formatted_crash_point)
#     iteration += 1
#     if crash_point > 100000:
#         print(iteration)
#         break