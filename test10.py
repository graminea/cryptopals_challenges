from base64 import b64decode
from Cryptodome.Cipher import AES
from test2 import xor_hex
from test9 import padding, unpadding


def CBC_decrypt(ciphertext, key, iv):
    blocks = []
    for i in range(0, len(ciphertext), len(key)): 
        blocks.append(ciphertext[i:i + len(key)])
    cipher = AES.new(key, AES.MODE_ECB)
    final = b""
    previous = iv
    for block in blocks:
        decrypted = cipher.decrypt(block)
        xored = xor_hex(decrypted, previous)
        final += xored
        previous = block
    return unpadding(final)


def CBC_encrypt(plaintext, key, iv):
    plaintext = padding(plaintext)
    blocks = []
    for i in range(0, len(plaintext), len(key)): 
        blocks.append(plaintext[i:i + len(key)])
    cipher = AES.new(key, AES.MODE_ECB)
    final = b""
    previous = iv
    for block in blocks:
        xored = xor_hex(block, previous)
        encrypted = cipher.encrypt(xored)
        final += encrypted
        previous = encrypted
    return final

if __name__ == "__main__":
    with open("data_files/10.txt", "r") as f:
        b64data = f.read()

    ciphertext = b64decode(b64data)
    key = b"YELLOW SUBMARINE"
    iv = b"\x00" * 16

    plaintext = CBC_decrypt(ciphertext, key, iv)
    print(plaintext.decode())