#Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
def xor_label(label, key):
    result = ""
    for char in label:
        result += chr(ord(char) ^ key)
    return result

label = "label" # replace with your label
key = 13

new_string = xor_label(label, key)
flag = f"crypto{{{new_string}}}"
print(flag)