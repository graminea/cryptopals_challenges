def repeating_key_xor(string_bytes, key_bytes): # take bytes (will help down the road in this set1)
    xor_return = bytearray()
    for i in range(len(string_bytes)):
        xor_return.append(string_bytes[i] ^ key_bytes[i % len(key_bytes)]) # take the lenght of the key and mod it to reapeat over and over

    return xor_return.hex()

if __name__ == "__main__":
    string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    string_bytes = string.encode('utf-8') # convert to bytes cause the function expects bytes
    key_bytes = key.encode('utf-8') # same here 
    result = repeating_key_xor(string_bytes, key_bytes)
    print("Result:  ", result)