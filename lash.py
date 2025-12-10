
LASH_MAP = {
    "A": "\\",
    "B": "\\[",
    "C": "[/",
    "D": "|[",
    "E": "|",
    "F": "/[",
    "G": "|\\",
    "H": "[|",
    "I": "/",
    "J": "/|",
    "K": "\\|/",
    "L": "/[/",
    "M": "/\\|",
    "N": "/|/",
    "O": "[",
    "P": "\\[|",
    "Q": "|\\/",
    "R": "\\|\\",
    "S": "[[|",
    "T": "|\\[",
    "U": "\\/",
    "V": "\\||",
    "W": "||\\",
    "X": "||[",
    "Y": "[|[",
    "Z": "|\\|",
}

# Reverse mapping
REVERSE_MAP = {v: k for k, v in LASH_MAP.items()}

def encode(text):
    """Encode text into Lash v2.1 with { between letters, _ between words"""
    words = text.upper().split(" ")
    encoded_words = []
    for word in words:
        letters = []
        for ch in word:
            if ch.isalpha():
                letters.append(LASH_MAP[ch])
            elif ch.isdigit():
                letters.append(ch)
        encoded_words.append("{".join(letters))
    return "_".join(encoded_words)

def decode(text):
    """Decode Lash v2.1 message into English"""
    words = text.split("_")
    decoded_words = []
    for word in words:
        letters = word.split("{")
        decoded_letters = []
        for token in letters:
            if token in REVERSE_MAP:
                decoded_letters.append(REVERSE_MAP[token])
            elif token.isdigit():
                decoded_letters.append(token)
            else:
                decoded_letters.append("?")  # unknown token
        decoded_words.append("".join(decoded_letters))
    return " ".join(decoded_words)

def main():
    print("Lash v2.1 Translator (Clean Version)")
    print("1) Encode")
    print("2) Decode")
    choice = input("> ").strip()

    if choice == "1":
        msg = input("Text to encode: ")
        print(encode(msg))
    elif choice == "2":
        msg = input("Lash to decode: ")
        print(decode(msg))
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
