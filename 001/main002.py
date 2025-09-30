from rich.console import Console
from rich.prompt import Prompt

from math import sqrt, fabs
def main():
    console = Console()
    a = int(Prompt.ask("Enter a", console=console))
    b = int(Prompt.ask("Enter b", console=console))
    square_root = sqrt(a * b) if (a * b >= 0) else "не існує"
    console.print("Сума: {}\nРізниця: {}\nДобуток: {}"
                  "\nСереднє арифметичне: {}\nСереднє геометричне: {}\n"
                  "Відстань: {}\nМаксимум: {}\nМінімум: {}\n"
                  "Сума квадратів: {}\nКвадрат суми: {}\nа в степені b: {}"
                  .format(a+b, a-b, a*b, (a + b)/2, square_root, fabs(a-b),
                          max(a, b), min(a, b), a**2+b**2, (a+b)**2, a**b))

if __name__ == "__main__":
    main()