# ============================================================
#              MORKOD - MORSE CODE TRANSLATOR
# ============================================================

# --- Morse Code Dictionary (Morse -> Letter/Number/Punctuation) ---
MORSE_TO_TEXT = {
    # Letters
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    # Numbers
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    # Punctuation
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}


# --- Method 1: 3-space word separator ---
def morse_to_text_spaces(morse_code):
    """
    Decodes Morse code using spacing conventions:
    - 1 space between letters
    - 3 spaces between words
    """
    words = morse_code.strip().split('   ')
    result = []

    for word in words:
        letters = word.split(' ')
        decoded_word = ''
        for code in letters:
            if code in MORSE_TO_TEXT:
                decoded_word += MORSE_TO_TEXT[code]
            elif code:
                decoded_word += f'[?{code}]'  # Show unknown symbol
        result.append(decoded_word)

    return ' '.join(result)


# --- Method 2: '/' slash word separator ---
def morse_to_text_slash(morse_code):
    """
    Decodes Morse code using '/' as word separator.
    - 1 space between letters
    - ' / ' between words
    Example: '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    """
    words = morse_code.strip().split(' / ')
    result = []

    for word in words:
        letters = word.split(' ')
        decoded_word = ''
        for code in letters:
            if code in MORSE_TO_TEXT:
                decoded_word += MORSE_TO_TEXT[code]
            elif code:
                decoded_word += f'[?{code}]'  # Show unknown symbol
        result.append(decoded_word)

    return ' '.join(result)


# --- Auto-detect which format is being used ---
def morse_to_text(morse_code):
    """
    Auto-detects format (slash or space-based) and decodes accordingly.
    """
    if ' / ' in morse_code:
        return morse_to_text_slash(morse_code)
    else:
        return morse_to_text_spaces(morse_code)


# --- Display known symbols ---
def show_morse_table():
    print("\n--- Morse Code Reference Table ---")
    categories = {
        'Letters': {k: v for k, v in MORSE_TO_TEXT.items() if v.isalpha() and len(v) == 1},
        'Numbers': {k: v for k, v in MORSE_TO_TEXT.items() if v.isdigit()},
        'Punctuation': {k: v for k, v in MORSE_TO_TEXT.items() if not v.isalnum()},
    }
    for category, entries in categories.items():
        print(f"\n{category}:")
        for morse, char in entries.items():
            print(f"  {char}  =>  {morse}")


# ============================================================
#                        MAIN PROGRAM
# ============================================================
def main():
    print("=" * 50)
    print   ("""
                ░█▄█░█▀█░█▀▄░█░█░█▀█░█▀▄
                ░█░█░█░█░█▀▄░█▀▄░█░█░█░█
                ░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░
            """)
    print("=" * 50)
    print("\nFormat options:")
    print("  [1] Space-based  : 1 space between letters, 3 spaces between words")
    print("  [2] Slash-based  : 1 space between letters, ' / ' between words")
    print("  [3] Auto-detect  : Program figures it out automatically")
    print("  [T] Show table   : Display full Morse code reference")
    print("  [Q] Quit")

    while True:
        print("\n" + "-" * 50)
        choice = input("Choose an option [1/2/3/T/Q]: ").strip().upper()

        if choice == 'Q':
            print("\nGoodbye!")
            break

        elif choice == 'T':
            show_morse_table()

        elif choice in ('1', '2', '3'):
            morse_input = input("\nEnter Morse code:\n> ").strip()

            if not morse_input:
                print("No input provided. Try again.")
                continue

            if choice == '1':
                result = morse_to_text_spaces(morse_input)
                method = "Space-based"
            elif choice == '2':
                result = morse_to_text_slash(morse_input)
                method = "Slash-based"
            else:
                result = morse_to_text(morse_input)
                method = "Auto-detected"

            print(f"\n[{method}] Decoded message:")
            print(f"  >> {result}")

        else:
            print("Invalid option. Please choose 1, 2, 3, T, or Q.")


if __name__ == "__main__":
    main()
