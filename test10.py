from base64 import b64decode
from Cryptodome.Cipher import AES
from test2 import xor_hex

def CBC_mode(text, key, iv):
    blocks = []
    for i in range(0, len(text), len(key)): 
        block = text[i:i + len(key)]  # take the text in chunks of keysize
        blocks.append(block)
    cipher = AES.new(key, AES.MODE_ECB)  # create a new AES cipher in ECB mode
    final = b""
    previous = iv
    for j in range(len(blocks)):
        decrypted = cipher.decrypt(blocks[j])
        xor = xor_hex(decrypted, previous)
        final += xor
        previous = blocks[j]
    return final
    

if __name__ == "__main__":
    with open("data_files/10.txt", "r") as f:
        b64data = f.read()

    text_bytes = b64decode(b64data)
    key = b"YELLOW SUBMARINE"
    iv = b"\x00" * 16

    plaintext = CBC_mode(text_bytes, key, iv)
    print(plaintext)