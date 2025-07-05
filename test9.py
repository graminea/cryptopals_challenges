def padding(data, blocksize):
    padding_size = blocksize - (len(data))
    for i in range(padding_size):
        data += bytes([padding_size])
    return data

if __name__ == "__main__":
    data = b"YELLOW SUBMARINE"
    blocksize = 20
    print(repr(padding(data, blocksize)))