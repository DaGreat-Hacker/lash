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
    "J": "/|\\",
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
    output = []
    for ch in text.upper():
        if ch.isalpha():
            output.append(LASH_MAP[ch])
        elif ch.isdigit():
            output.append(ch)
        elif ch == " ":
            continue  # spaces handled by user if needed
    return "{".join(output)

def decode(text):
    parts = text.split("{")
    result = []
    for p in parts:
        if p.isdigit():
            result.append(p)
        elif p in REVERSE_MAP:
            result.append(REVERSE_MAP[p])
        else:
            result.append("?")
    return "".join(result)

def main():
    print("Lash v2 Translator")
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
