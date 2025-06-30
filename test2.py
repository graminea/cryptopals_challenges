def xor_hex(bytes1, bytes2):
    xor_return = bytearray() # prepare the variable to take the xor
    
    for i in range(len(bytes1)):
        xor_return.append(bytes1[i] ^ bytes2[i]) # xor each byte

    return bytes(xor_return) # return in bytes to better output, cause bytearray has a kinda weird print

if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    byte_hex1 = bytes.fromhex(hex1)
    byte_hex2 = bytes.fromhex(hex2)
    
    result = xor_hex(byte_hex1, byte_hex2)
    print(result.hex())