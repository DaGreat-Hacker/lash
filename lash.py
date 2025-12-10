

LASH_MAP = {
    "A": r"\",
    "B": r"\[",
    "C": r"[/",
    "D": r"|[",
    "E": r"|",
    "F": r"/[",
    "G": r"|\",
    "H": r"[|",
    "I": r"/",
    "J": r"/|\",
    "K": r"\|/",
    "L": r"/[/",
    "M": r"/\|",
    "N": r"/|/",
    "O": r"[",
    "P": r"\[|",
    "Q": r"|\/",
    "R": r"\|\",
    "S": r"[[|",
    "T": r"|\[",
    "U": r"\/",
    "V": r"\||",
    "W": r"||\",
    "X": r"||[",
    "Y": r"[|[",
    "Z": r"|\|",
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
            output.append("_")  # word separator for v2.1
    return "{".join(output)

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
