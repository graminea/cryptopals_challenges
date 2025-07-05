from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from random import randint
from test10 import CBC_encrypt
from test9 import padding

def get_ramdom_AES_key():
    return get_random_bytes(16)

def detect_ecb(text, block_size=16):
    blocks = []                                 # break in 16 byte blocks
    for j in range(0, len(text), block_size):
        block = text[j:j + block_size]          # same logic as the chunks of test6
        blocks.append(block)
    
    unique_blocks = set(blocks)
    
    if len(blocks) > len(unique_blocks):       # if theres reapeated blocks, the set will be smaller, thus is ECB. If its equal, its CBC (in the case of test11)
        return True
    return False

def encryption_oracle(text_input):
    key = get_ramdom_AES_key()
    text_input = get_random_bytes(randint(5, 10)) + text_input + get_random_bytes(randint(5, 10)) # add the random bytes
    text_input = padding(text_input) # pad to fit the blocksize (unsing test9 pading)
    which_mode = randint(0, 1) # choose randomly btween ECB and CBC (0 or 1)
    
    if which_mode == 0:
        mode = "ECB"
        #print("ECB mode")
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted = cipher.encrypt(text_input) 
    else:
        mode = "CBC"
        #print("CBC mode")
        iv = get_random_bytes(16)
        encrypted = CBC_encrypt(text_input, key, iv)
    
    return mode, encrypted

if __name__ == "__main__":
    text = b"X" * 48
    for i in range(100):
        mode, encrypted = encryption_oracle(text)
        
        if detect_ecb(encrypted):
            mode_found = "ECB"
        else:
            mode_found = "CBC"

        if mode != mode_found:
            raise Exception("Ta errado pai")
    
    print("Min de papai, acertou")
        
    

        
        