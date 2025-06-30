from test3 import test_keys, score_text
from test5 import repeating_key_xor
from base64 import b64decode

def hamming_distance(b1, b2):
    if (len(b1) != len(b2)):
        raise ValueError("Input byte arrays must have the same length")
    sum = 0
    for i in range(len(b1)):
        sum += bin(b1[i] ^ b2[i]).count("1") # do the xor and counts when is 1 (differs)
    return sum

def guess_keysize(text, minkeysize, max_keysize):
    scores = []
    for keysize in range(minkeysize, max_keysize + 1):
        chunks = []
        for i in range(0, len(text), keysize):
            chunk = text[i:i + keysize]  # take the text in chunks of keysize
            chunks.append(chunk)
        
        if len(chunks) < 4: # take like 4 chunks for good measure
            continue
        
        distances = []
        
        for i in range(3):
            chunk1 = chunks[i]
            chunk2 = chunks[i + 1]
            
            distances.append(hamming_distance(chunk1, chunk2) / keysize)    # calculate the hamming distance normalized for all the 3 first pairs of chunks

        if distances:   
            score = sum(distances) / len(distances) # score is the average of the distances
            scores.append((keysize, score))         # put the keysize and their score in a tuple to sort later
            
    scores.sort(key=lambda x: x[1]) 
    return scores[:5] # take the best 5 scores

def slice_text(text, keysize):  # slice the text in slices of keysize
    slices = []
    for i in range(keysize):
        slice = bytearray()
        for j in range(i, len(text), keysize):
            slice.append(text[j])
        slices.append(slice)
    return slices

def find_key(sliced_text):  # test the keys for each sliced text 
    key = bytearray()
    for slice in sliced_text:
        text, key_byte, score = test_keys(slice)
        key.append(key_byte)
    return bytes(key)

if __name__ == "__main__":
    with open("data_files/6.txt", "r") as file:
        b64data = file.read()
    text = b64decode(b64data) # decode the base64 data to bytes
    key_sizes = guess_keysize(text, 2, 40) # guess the key sizes, returns the best 5

    best_score = float('inf')
    best_key = None
    best_text = None
    
    for keysize, score in key_sizes:    # try the key sizes (5 best returned)
        slices = slice_text(text, keysize)
        
        key_bytes = []
        for slice in slices:
            xor, key_byte, score = test_keys(slice) # xor e score not used, just here to respect the function returns, used to take the key byte
            key_bytes.append(key_byte)  # this the byte of the key for each slice
        key = bytes(key_bytes) # form the key

        text_hex = repeating_key_xor(text, key) # do the decoding with the key using reapiting_key_xor from test5
        text_bytes = bytes.fromhex(text_hex) # convert the returned hex to bytes, for it to be used in the score_text function

        text_score = score_text(text_bytes)

        if text_score < best_score: # choose the best score
            best_score = text_score
            best_key = key
            best_text = text_bytes

    print(f"key: {best_key.decode('utf-8', errors='replace')}")
    print(f"Score: {best_score:.4f}")
    print("Text:")
    print(best_text.decode('utf-8', errors='replace'))
    
    