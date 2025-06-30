from Cryptodome.Cipher import AES # using this lib that runs the AES chipher thing in the background, basically C
from base64 import b64decode

def decrypt_aes_ecb(text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB) # create the cipher with the key
    
    text_decrypted = cipher.decrypt(text) # decrypt the text using the cipher
    
    return text_decrypted.decode('utf-8')

if __name__ == "__main__":
    key = "YELLOW SUBMARINE"
    with open("data_files/7.txt", "r") as file:
        text_base64 = file.read()
        
    text = b64decode(text_base64)
    text_decrypted = decrypt_aes_ecb(text, key)
    print(text_decrypted)