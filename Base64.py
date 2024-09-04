###Using Base64 which allows us to represent binary data as an ASCII strug using an aplhabet of 64 charcters.One character of a Base64 string encodes 6 binary digits(bits), and so 4 charcters of Base64 encode three 8-bit bytes. Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.
##Take the below hex string, decode it into bytes and then encode it into Base64.

import base64

#decode the hex string into bytes
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_data = bytes.fromhex(hex_string)

#encode the bytes into Base64
base64_data = base64.b64encode(bytes_data)
print(base64_data.decode('utf-8'))