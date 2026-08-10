ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    shift_amount = shift_amount % 26

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in ALPHABET:
            output_text += letter
            continue

        shifted_position = ALPHABET.index(letter) + shift_amount
        shifted_position %= len(ALPHABET)
        output_text += ALPHABET[shifted_position]

    return output_text


def get_cipher_stats(text, shift, mode):
    return {
        'original_length': len(text),
        'processed_length': len(caesar(text, shift, mode)),
        'shift_used': shift,
        'alphabet_size': len(ALPHABET)
    }