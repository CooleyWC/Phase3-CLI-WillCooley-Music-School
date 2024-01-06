# lib/cli.py

from helpers import (
    list_ensembles,
    exit_program,
    add_ensemble,
    view_ensemble
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "M":
            list_ensembles()
            ensembles()
        elif choice == "E":
            exit_program()
        else:
            print("Invalid choice")


def main_menu():
    print("Welcome to Will Cooley's Music School")
    print("Type M to see the ensembles")
    print("Type E to exit the program")

def ensembles():
    while True:
        ensembles_menu()
        choice = input("> ")
        if choice.isdigit():
            view_ensemble(int(choice))
        elif choice == "C":
            add_ensemble()    
        elif choice == "B":
            break
        else:
            print('Invalid Choice')

def ensembles_menu():
    print("Type the number of the Ensemble to view its details")
    print("Type C to add a new ensemble")
    print("Type B to go back to the main menu")




    





if __name__ == "__main__":
    main()
