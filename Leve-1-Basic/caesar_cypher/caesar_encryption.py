#!/usr/bin/env python3
"""
Cybersecurity Toolkit - Level 1
Caesar Cipher Implementation
Author: [Your Name]
GitHub: [Your GitHub]
"""


def caesar_cipher(text, shift, mode='encrypt'):
    """
    Implements the Caesar Cipher for encrypting or decrypting text.

    The Caesar Cipher is a substitution cipher where each letter in the plaintext 
    is shifted a fixed number of positions down or up the alphabet. This is one 
    of the simplest and most widely known encryption techniques.

    Args:
        text (str): Text to be processed (plaintext or ciphertext)
        shift (int): Number of positions to shift each letter (1-25)
        mode (str): 'encrypt' or 'decrypt'

    Returns:
        str: Processed text (ciphertext if encrypting, plaintext if decrypting)

    Example:
        >>> caesar_cipher("HELLO", 3, 'encrypt')
        'KHOOR'
        >>> caesar_cipher("KHOOR", 3, 'decrypt')
        'HELLO'
    """
    result = ""

    # Adjust shift direction based on mode
    # For decryption, we shift backwards (negative shift)
    if mode == 'decrypt':
        shift = -shift

    # Process each character in the input text
    for char in text:
        if char.isalpha():
            # Determine ASCII base value for uppercase or lowercase letters
            # ord('A') = 65, ord('a') = 97
            ascii_base = ord('A') if char.isupper() else ord('a')

            # Apply the Caesar Cipher formula:
            # 1. Convert char to 0-25 range (char - base)
            # 2. Apply shift and wrap around using modulo 26
            # 3. Convert back to ASCII range (+ base)
            new_char = chr((ord(char) - ascii_base + shift) % 26 + ascii_base)
            result += new_char
        else:
            # Keep non-alphabetic characters unchanged
            # This preserves spaces, numbers, punctuation, etc.
            result += char

    return result


def interactive_mode():
    """
    Provides an interactive command-line interface for the Caesar Cipher.

    This function allows users to:
    - Choose between encryption and decryption
    - Input their text and shift value
    - See immediate results
    - Handle errors gracefully
    """
    print("=== Caesar Cipher ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    while True:
        try:
            choice = input("\nChoose an option (1-3): ").strip()

            if choice == '3':
                print("Exiting...")
                break

            if choice in ['1', '2']:
                text = input("Enter the text: ")
                shift = int(input("Enter the shift value (1-25): "))

                # Validate shift range
                if not 1 <= shift <= 25:
                    print("Error: Shift must be between 1 and 25")
                    continue

                if choice == '1':
                    result = caesar_cipher(text, shift, 'encrypt')
                    print(f"\nEncrypted text: {result}")
                else:
                    result = caesar_cipher(text, shift, 'decrypt')
                    print(f"\nDecrypted text: {result}")
            else:
                print("Invalid option! Please choose 1, 2, or 3.")

        except ValueError:
            print("Error: Please enter a valid number for the shift.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


def demonstration():
    """
    Demonstrates the Caesar Cipher with example usage.

    This function shows:
    - How the cipher works with a known example
    - The encryption and decryption process
    - Handling of different character types
    """
    original_text = "Hello Cybersecurity World! 123"
    shift = 3

    print("=== Caesar Cipher Demonstration ===")
    print(f"Original text: {original_text}")
    print(f"Shift value: {shift}")

    # Encrypt the text
    encrypted_text = caesar_cipher(original_text, shift, 'encrypt')
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the text
    decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
    print(f"Decrypted text: {decrypted_text}")

    # Verify the process worked correctly
    if original_text == decrypted_text:
        print("✓ Encryption and decryption successful!")
    else:
        print("✗ Error in encryption/decryption process!")


def brute_force_decrypt(ciphertext):
    """
    Demonstrates a brute-force attack on the Caesar Cipher.

    Since there are only 25 possible shifts (1-25), the Caesar Cipher
    is vulnerable to brute-force attacks. This function tries all
    possible shifts and displays the results.

    Args:
        ciphertext (str): The encrypted text to brute-force

    Returns:
        dict: All possible decryptions with their shift values
    """
    print(f"\n=== Brute Force Attack on: '{ciphertext}' ===")
    results = {}

    for shift in range(1, 26):
        decrypted = caesar_cipher(ciphertext, shift, 'decrypt')
        results[shift] = decrypted
        print(f"Shift {shift:2d}: {decrypted}")

    return results


if __name__ == "__main__":
    """
    Main execution block when the script is run directly.

    This section:
    1. Runs a demonstration of the cipher
    2. Shows brute-force attack capabilities
    3. Launches interactive mode for user input
    """

    # Step 1: Show how the cipher works
    demonstration()

    # Step 2: Demonstrate brute-force attack
    print("\n" + "=" * 60)
    test_cipher = "KHOOR Frbvxulvhfwb Zruog! 123"
    brute_force_decrypt(test_cipher)

    # Step 3: Start interactive mode
    print("\n" + "=" * 60)
    interactive_mode()