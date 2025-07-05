def padding(data, blocksize=16):
    padding_size = blocksize - (len(data) % blocksize)
    for i in range(padding_size):
        data += bytes([padding_size])
    return data
def unpadding(data):        # added after to help in another test10
    pad_len = data[-1]
    return data[:-pad_len]


if __name__ == "__main__":
    data = b"YELLOW SUBMARINE"
    blocksize = 20
    print(repr(padding(data, blocksize)))