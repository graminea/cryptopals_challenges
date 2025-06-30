block_size = 16 
def detect_ecb(texts):                              
    max_repeats = 0
    line_index = -1 

    for i in range(len(texts)):
        hex_line = texts[i].strip()
        text = bytes.fromhex(hex_line)
        
        blocks = []                                 # break in 16 byte blocks
        for j in range(0, len(text), block_size):
            block = text[j:j + block_size]          # same logic as the chunks of test6
            blocks.append(block)

        unique_blocks = set(blocks)

        num_repeats = len(blocks) - len(unique_blocks) # count the reapeats by using the difference btween the lenght of the set (no repeats of blocks) and the original list
                                                       # the lenght of the blocks should be the same of the text divided by the block size, but if it reapeats, the set will be smaller

        if num_repeats > max_repeats:
            max_repeats = num_repeats
            line_index = i
                                                    
    return line_index, max_repeats


if __name__ == "__main__":
    with open("data_files/8.txt", "r") as f:
        lines = f.readlines()

    line_index, repeats = detect_ecb(lines)

    print(f"{line_index=}")
    print(f"{repeats=}")
    print(f"line: {lines[line_index].strip()}")
