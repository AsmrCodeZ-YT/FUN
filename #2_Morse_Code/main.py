MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


MORSE_TO_TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        morse_code.append(MORSE_CODE_DICT.get(char, '/'))
    return ' '.join(morse_code)


def morse_to_text(morse):
    words = morse.split(' ')
    decoded_chars = []
    for code in words:
        decoded_chars.append(MORSE_TO_TEXT_DICT.get(code, '?'))
    return ''.join(decoded_chars)


# Test
text = "hello world"
morse = text_to_morse(text)
decoded = morse_to_text(morse)

print(text)
print(morse)
print(decoded)
