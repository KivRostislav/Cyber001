from rich.prompt import Prompt
from rich.console import Console

def main():
    console = Console()
    firstname = Prompt.ask("Enter firstname", console=console)
    lastname = Prompt.ask("Enter lastname", console=console)
    age = Prompt.ask("Enter age", console=console)

    console.print("{firstname} {lastname}, {age} р.н."
                  .format(firstname=firstname, lastname=lastname, age=age))
    console.print("Прізвище: {lastname}\nІм'я: {firstname}\nРік народження: {age}"
                  .format(lastname=lastname, firstname=firstname, age=age))

if __name__ == "__main__":
    main()
