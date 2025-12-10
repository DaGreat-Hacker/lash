

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


REVERSE_MAP = {v: k for k, v in LASH_MAP.items()}

def encode(text):
    words = text.upper().split(" ")
    encoded_words = []
    for word in words:
        encoded_letters = []
        for ch in word:
            if ch.isalpha():
                encoded_letters.append(LASH_MAP[ch])
            elif ch.isdigit():
                encoded_letters.append(ch)
        encoded_words.append("{".join(encoded_letters))
    return "_".join(encoded_words)

def decode(text):
    parts = text.split("{")
    result = []
    for p in parts:
        if p == "_":
            result.append(" ")
        elif p.isdigit():
            result.append(p)
        elif p in REVERSE_MAP:
            result.append(REVERSE_MAP[p])
        else:
            result.append("?")  # unknown symbol
    return "".join(result)

def main():
    print("Lash v2.1 Translator")
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
