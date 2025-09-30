import rich
from rich.console import Console
from rich.prompt import Prompt

def main():
    console = Console()
    number_str = Prompt.ask("Enter a number", console=console)

    result = 0
    for i in range(0, len(number_str)):
        result = result + int(number_str[i:i+1])

    rich.print(result)

if __name__ == "__main__":
    main()