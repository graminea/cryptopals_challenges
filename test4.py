from test3 import test_keys

if __name__ == "__main__":  # this is basically the test3 function but in a loop to test all the lines 
    best_score = 0.0 
    best_xor = b""  # in bytes form
    best_key = 0
    right_line = ""

    with open("data_files/4.txt", "r") as file:
        for line in file:
            line = line.strip()
            try:
                hex_bytes = bytes.fromhex(line) # convert to hex all the lines
            except ValueError:
                continue  # Skip bad lines

            xor, key, score = test_keys(hex_bytes) # test each line with the function of the last test
            if score < best_score or best_score == 0.0:  # choose the best score and save some variables related to it
                best_score = score
                best_xor = xor
                best_key = key
                right_line = line

    print("Linha:", right_line)
    print (best_xor)
    print(f"Key: {chr(best_key)}, Score: {best_score}")
    