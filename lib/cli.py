# lib/cli.py

from helpers import (
    list_ensembles,
    exit_program,
    add_ensemble,
    view_ensemble,
    update_ensemble,
    delete_ensemble
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
    selected_ensemble = None
    while True:
        ensembles_menu()
        choice = input("> ")
        if choice.isdigit():
            selected_ensemble = int(choice)
            view_ensemble(selected_ensemble)
            ensemble_options(selected_ensemble)
        elif choice == "C":
            add_ensemble()    
        elif choice == "B":
            break
        elif choice == "E":
            exit_program()
        else:
            print('Invalid Choice')

def ensembles_menu():
    print("Type the number of the Ensemble to view its details")
    print("Type C to add a new ensemble")
    print("Type B to go back to the main menu")
    print("Type E to exit the program")

def ensemble_options(selected_ensemble):
    while True:
        ensemble_options_menu()
        choice = input("> ")
        if choice == "U":
            update_ensemble(selected_ensemble)
            list_ensembles()
            break
        elif choice == "D":
            delete_ensemble()
        elif choice == "B":
            break
        elif choice == "E":
            exit_program()
        else:
            print('Invalid Choice')
        

def ensemble_options_menu():
    print("Type U to update this ensemble")
    print("Type D to delete this ensemble")
    print("Type B to go back to ensemble menu")
    print("Type E to exit the program")




    





if __name__ == "__main__":
    main()
