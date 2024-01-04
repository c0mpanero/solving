def accum(text):
    text = text.lower()
    return "-".join(
        char.capitalize() + char*n for n, char in enumerate(text)
    )
