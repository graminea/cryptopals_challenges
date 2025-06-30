from test2 import xor_hex

# this is the frequency of letter in english by their ASCII value, unsing only lowercase letters cause is more the enough for this
# Source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
CHAR_FREQ = {
    101: 12.02, 116: 9.1,  97: 8.12,  111: 7.68, 105: 7.31,
    110: 6.95,  115: 6.28, 114: 6.02, 104: 5.92, 100: 4.32,
    108: 3.98,  117: 2.88, 99: 2.71,  109: 2.61, 102: 2.3,
    121: 2.11,  119: 2.09, 103: 2.03, 112: 1.82, 98: 1.49,
    118: 1.11,  107: 0.69, 120: 0.17, 113: 0.11, 106: 0.1,
    122: 0.07
}

def score_text(text):
    total_letters = len(text)
    score = 0.0
    for letter, freq in CHAR_FREQ.items():                          # simple frequency analysis, compare the frequency of each letter in the text with the expected frequency
        actual_freq = (text.count(letter) / total_letters) * 100    # and give a score based on the diff (lower is better)
        diff = abs(actual_freq - freq)
        score += diff

    return score

def test_keys(hex_bytes):
    result = 0.0
    
    for key in range(256):
        xor = xor_hex(hex_bytes, bytes([key]) * len(hex_bytes)) # do the xor btween the input and all the keys and score for each decription
        score = score_text(xor)
        if result == 0.0 or score < result:
            result = score
            best_key = key
            best_xor = xor
    return best_xor, best_key, result
            
if __name__ == "__main__":
    hex_input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    hex_bytes = bytes.fromhex(hex_input)  # Convert hex string to bytes
    xor, key, score = test_keys(hex_bytes)
    xor = xor_hex(hex_bytes, bytes([key]) * len(hex_bytes))
    key = chr(key)
    print(f"{xor}, {key=}, {score=}")