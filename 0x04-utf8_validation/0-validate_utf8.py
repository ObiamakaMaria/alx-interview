#!/usr/bin/python3
'''Implementation of UTF-8 Encodung & Validation '''


def validUTF8(data):
    ''' Returns True if data is a valid UTF-8 encoding, else return False'''
    bytee = 0
    for a in data:
        n = 1 << 7
        if not bytee:
            while a & n:
                bytee += 1
                n >>= 1
            if not bytee:
                continue
            if bytee == 1 or bytee > 4:
                return False
        else:
            if a >> 6 != 0b10:
                return False
        bytee -= 1
    return bytee == 0
