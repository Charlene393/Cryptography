###using hex methond to encode an decode text to represent binary data as an ASCIII string.
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag = bytes.fromhex(hex_string).decode('utf-8')
print(flag)
