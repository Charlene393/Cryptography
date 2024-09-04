#The properties include Commutative: A ⊕ B = B ⊕ A
#Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
#Identity: A ⊕ 0 = A
#Self-Inverse: A ⊕ A = 0 
from functools import reduce
from operator import xor

# Hexadecimal values provided
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_KEYS_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert hex to bytes
KEY1 = bytes.fromhex(KEY1_hex)
KEY2_XOR_KEY1 = bytes.fromhex(KEY2_XOR_KEY1_hex)
KEY2_XOR_KEY3 = bytes.fromhex(KEY2_XOR_KEY3_hex)
FLAG_XOR_KEYS = bytes.fromhex(FLAG_XOR_KEYS_hex)

# Find KEY2
KEY2 = bytes([x ^ y for x, y in zip(KEY2_XOR_KEY1, KEY1)])

# Find KEY3
KEY3 = bytes([x ^ y for x, y in zip(KEY2_XOR_KEY3, KEY2)])

# Find FLAG
FLAG = bytes([x ^ y ^ z for x, y, z in zip(FLAG_XOR_KEYS, KEY1, KEY3)])

# Print the FLAG in hexadecimal
print(f"FLAG in hex: {FLAG.hex()}")

# Try to decode to UTF-8, if it fails, fall back to raw bytes
try:
    flag_message = FLAG.decode('utf-8')
    print(f"crypto{{{flag_message}}}")
except UnicodeDecodeError:
    print(f"Decoding failed. FLAG (hex): {FLAG.hex()}")
