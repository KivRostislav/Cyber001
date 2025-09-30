import rich
from rich.console import Console
from rich.prompt import Prompt

LEN_OF_ALPHABET = 26
START_OF_LOWER_LETTER = 97

def main():
    console = Console()
    text = Prompt.ask("Enter text to encrypt", console=console)
    shift = int(Prompt.ask("Enter shift", console=console))
    available_modes = ["encrypt", "decrypt"]
    mode = Prompt.ask("Enter mode", choices=available_modes, console=console)
    encrypt = True if mode == available_modes[0] else False

    if shift > LEN_OF_ALPHABET:
        console.print("Shift must be less than the alphabet.")
        return

    result = ""
    for letter in text.strip():
        if not letter.isalpha():
            result += letter
            continue

        is_capital = letter.isupper()
        letter = letter.lower()
        new_letter_index = ord(letter) + shift if encrypt else ord(letter) - shift
        if new_letter_index >= START_OF_LOWER_LETTER + LEN_OF_ALPHABET and encrypt:
            new_letter_index = new_letter_index - LEN_OF_ALPHABET
        if new_letter_index < START_OF_LOWER_LETTER and not encrypt:
            new_letter_index = new_letter_index + LEN_OF_ALPHABET
        new_letter = chr(new_letter_index)
        result = result + (new_letter.upper() if is_capital else new_letter)
    console.print(result)

if __name__ == "__main__":
    main()