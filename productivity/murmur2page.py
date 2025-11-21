import re
import sys
from pathlib import Path

# ---- CONFIG: customise verbal commands ----
PUNCTUATION_MAP = {
    r"\bfull stop\b": ".",
    r"\bperiod\b": ".",
    r"\bcomma\b": ",",
    r"\bquestion mark\b": "?",
    r"\bexclamation mark\b": "!",
    r"\bexclamation point\b": "!",
    r"\bcolon\b": ":",
    r"\bsemicolon\b": ";",
    r"\bquote\b": '"',
    r"\bdouble quote\b": '"',
    r"\bsingle quote\b": "'",
    r"\bopen quote\b": '"',
    r"\bclose quote\b": '"',
    r"\bopen double quote\b": '"',
    r"\bclose double quote\b": '"',
    r"\bopen single quote\b": "'",
    r"\bclose single quote\b": "'", 
    r"\bdash\b": "—",
    r"\bhyphen\b": "-",
    r"\bopen brackets\b": "(",
    r"\bclose brackets\b": ")",
    r"\bopen parenthesis\b": "(",
    r"\bclose parenthesis\b": ")",
    r"\bellipsis\b": "…",
}

# Paragraph / line commands
PARAGRAPH_MARKERS = [
    r"\bnew paragraph\b",
    r"\bparagraph break\b",
]

LINEBREAK_MARKERS = [
    r"\bnew line\b",
    r"\bline break\b",
    r"\breturn\b",
]

def apply_verbal_punctuation(text: str) -> str:
    # Replace paragraph markers with a placeholder
    for pattern in PARAGRAPH_MARKERS:
        text = re.sub(pattern, "\n\n", text, flags=re.IGNORECASE)

    # Replace linebreak markers with a single newline
    for pattern in LINEBREAK_MARKERS:
        text = re.sub(pattern, "\n", text, flags=re.IGNORECASE)

    # Replace verbal punctuation with symbols
    for pattern, symbol in PUNCTUATION_MAP.items():
        # Ensure surrounding spaces are handled cleanly
        text = re.sub(rf"\s*{pattern}\s*", symbol + " ", text, flags=re.IGNORECASE)

    return text

def tidy_spaces(text: str) -> str:
    # Collapse multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.?!])", r"\1", text)

    # Ensure a space after punctuation when followed by a word character
    text = re.sub(r"([,.?!])([^\s\n])", r"\1 \2", text)

    # Normalize multiple blank lines (max two)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def capitalise_after_sentence(text: str) -> str:
    """
    Rough-and-ready capitalisation after . ? !
    Uses a regex to find sentence-ending punctuation followed by whitespace and a lowercase letter, and capitalises that letter.
    Can be disabled if preferred.
    """
    def repl(match):
        punctuation = match.group(1)
        space = match.group(2)
        letter = match.group(3)
        return f"{punctuation}{space}{letter.upper()}"

    # Capitalise first letter of the text
    text = text.lstrip()
    if text:
        text = text[0].upper() + text[1:]

    # Capitalise after sentence-ending punctuation
    pattern = r"([.?!])(\s+)([a-z])"
    text = re.sub(pattern, repl, text)

    return text

def process_text(text: str) -> str:
    text = apply_verbal_punctuation(text)
    text = tidy_spaces(text)
    text = capitalise_after_sentence(text)
    return text

def main():
    if len(sys.argv) < 3:
        print("Usage: python murmur2page.py input.txt output.txt")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    raw = input_path.read_text(encoding="utf-8")
    cleaned = process_text(raw)
    output_path.write_text(cleaned, encoding="utf-8")
    print(f"Processed text written to {output_path}")

if __name__ == "__main__":
    main()

