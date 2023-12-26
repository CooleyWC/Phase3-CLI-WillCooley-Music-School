# lib/cli.py

from helpers import (
    list_ensembles,
    exit_program,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "M":
            list_ensembles()
        elif choice == "E":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Welcome to Will Cooley's Music School")
    print("Type M to see the ensembles")
    print("Type E to exit the program")


if __name__ == "__main__":
    main()
