def validUTF8(data):
    num_bytes_to_follow = 0
    
    for num in data:
        byte = num & 255  # Extracting the 8 least significant bits
        
        if num_bytes_to_follow == 0:
            # If it's a single-byte character (ASCII)
            if byte < 128:
                continue
            # Finding out how many bytes follow
            elif byte < 224:
                num_bytes_to_follow = 1
            elif byte < 240:
                num_bytes_to_follow = 2
            elif byte < 248:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            # Checking if the byte follows the pattern '10xxxxxx'
            if not (byte & 192 == 128):
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
