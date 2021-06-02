from datetime import date
from datetime import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_by(name):
    print("Adios " + name)

def print_preg(name):
    print(f"Cómo estás, {name}? Yo bien")

def print_ver(fecha):
    print(f"Realizado {fecha}")

def print_rama(rama):
    print(f'La rama es {rama}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Jose Luis')
    print_preg("Sara")
    print_by("Javier")

    today = date.today()

    print_ver(today)

    print("RamaRDL")
    print("Otra vez")
