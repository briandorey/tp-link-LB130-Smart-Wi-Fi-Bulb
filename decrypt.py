#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for decrypting data from the TP-Link RBG wireless light
"""


def encrypt(value, key):
    '''
    Encrypt the command string
    '''
    valuelist = list(value)

    for i in range(len(valuelist)):
        val = ord(valuelist[i])
        valuelist[i] = chr(val ^ int(key))
        key = ord(valuelist[i])

    return "".join(valuelist)


def decrypt(value, key):
    '''
    Decrypt the command string
    '''
    valuelist = list(value)

    for i in range(len(valuelist)):
        val = valuelist[i]
        valuelist[i] = chr(val ^ key)
        key = val

    return "".join(valuelist)


def main():
    '''
    Main program function
    '''

    encryption_key = 0xAB

    teststring = [0xd0, 0xf2, 0x81, 0xec, 0x8d, 0xff, 0x8b, 0xe7, 0x8e, 0xe8,
                  0x8d, 0xa3, 0xca, 0xa5, 0xd1, 0xff, 0x9c, 0xf3, 0x9e, 0xf3,
                  0x9c, 0xf2, 0xdc, 0xa8, 0xc1, 0xac, 0xc9, 0xba, 0xdf, 0xab,
                  0xdf, 0xb6, 0xd8, 0xbf, 0x9d, 0xa7, 0xdc, 0xfe, 0x8d, 0xe8,
                  0x9c, 0xc3, 0xb7, 0xde, 0xb3, 0xd6, 0xf4, 0xce, 0xb5, 0x97,
                  0xee, 0x8b, 0xea, 0x98, 0xba, 0x80, 0xb2, 0x82, 0xb3, 0x84,
                  0xa8, 0x8a, 0xe7, 0x88, 0xe6, 0x92, 0xfa, 0xd8, 0xe2, 0xda,
                  0xf6, 0xd4, 0xb9, 0xdd, 0xbc, 0xc5, 0xe7, 0xdd, 0xef, 0xd7,
                  0xfb, 0xd9, 0xb1, 0xde, 0xab, 0xd9, 0xfb, 0xc1, 0xf0, 0xc6,
                  0xea, 0xc8, 0xa5, 0xcc, 0xa2, 0x80, 0xba, 0x8e, 0xbc, 0x90,
                  0xb2, 0xc1, 0xa4, 0xc7, 0xe5, 0xdf, 0xee, 0xd6, 0xab, 0xd6,
                  0xab]

    output = decrypt(teststring, encryption_key)
    print output


if __name__ == "__main__":
    main()
