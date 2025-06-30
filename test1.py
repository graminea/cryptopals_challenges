from base64 import b64encode
    
def hex_to_base64(hex):
    raw_bites = bytes.fromhex(hex) # take teh bytes 

    base64 = b64encode(raw_bites) # encode to base64

    return base64

if __name__ == "__main__":
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(hex).decode('utf-8'))
    