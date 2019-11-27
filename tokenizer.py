strip_chars = ',.\n\t()[]{}\\|\'\"<>*.-'


def termize_doc(doc):
    tokens = set()
    for token in doc.lower().split():
        tokens.add(token.strip(strip_chars))

    return tokens


def tokenize_str(str):
    tokens = list()
    for token in str.lower().split():
        tokens.append(token.strip(strip_chars))

    return tokens


if __name__ == "__main__":
    tokens = termize_doc("abc xyz abc")
    print("Tokens set: ", tokens)
    tokens = tokenize_str("abc xyz abc")
    print("Tokens list: ", tokens)
