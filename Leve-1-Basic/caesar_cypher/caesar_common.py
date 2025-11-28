#!/usr/bin/env python3
"""
Caesar Cipher Core Library
Contains all the basic functions
"""

def caesar_alphabet(text, shift, mode='encrypt'):
    """Basic alphabet-only Caesar cipher"""
    result = ""
    if mode == 'decrypt': 
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_ascii(text, shift, mode='encrypt'):
    """ASCII Caesar cipher"""
    result = ""
    if mode == 'decrypt': 
        shift = -shift
    
    for char in text:
        if 32 <= ord(char) <= 126:
            result += chr((ord(char) - 32 + shift) % 95 + 32)
        else:
            result += char
    return result