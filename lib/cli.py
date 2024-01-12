# lib/cli.py
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({'error': 'bold red'})

console = Console(theme=custom_theme)

from helpers import (
    list_ensembles,
    exit_program,
    add_ensemble,
    view_ensemble,
    update_ensemble,
    delete_ensemble,
    find_ensemble_by_director,
    find_ensemble_by_level,
    view_ensemble_musicians,
    list_musicians,
    add_musician,
    find_musician_by_name,
    view_musicians_by_instrument
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "Ens" or choice == "ens":
            list_ensembles()
            ensembles()
        elif choice == "Mus" or choice == "mus":
            musicians()
        elif choice == "E" or choice == "e":
            exit_program()
        else:
            console.print("Invalid choice", style='error')


def main_menu():
    console.print("Welcome to Will Cooley's Music School", style="bold underline deep_sky_blue1")
    print("Type Ens or ens to see the ensembles")
    print("Type Mus or mus to see the musicians")
    print("Type E or e to exit the program")

def ensembles():
    selected_ensemble = None
    while True:
        ensembles_menu()
        choice = input("> ")
        if choice.isdigit():
            selected_ensemble = int(choice)
            view_ensemble(selected_ensemble)
            ensemble_options(selected_ensemble)
        elif choice == "A" or choice == "a":
            add_ensemble()
        elif choice == "Dir" or choice == "dir":
            find_ensemble_by_director()
            list_ensembles()
        elif choice == "L" or choice == "l":
            find_ensemble_by_level()    
        elif choice == "B" or choice == "b":
            break
        elif choice == "E" or choice == "e":
            exit_program()
        else:
            print('Invalid Choice')

def ensembles_menu():
    print("Type the number of the Ensemble to view its details")
    print("Type A or a to add a new ensemble")
    print("Type Dir or dir to find an ensemble by director")
    print("Type L or l to find an ensemble by level")
    print("Type B or b to go back to the main menu")
    print("Type E or e to exit the program")

def ensemble_options(selected_ensemble):
    while True:
        ensemble_options_menu()
        choice = input("> ")
        if choice == "U" or choice == "u":
            update_ensemble(selected_ensemble)
            list_ensembles()
            break
        elif choice == "D" or choice == "d":
            delete_ensemble(selected_ensemble)
            list_ensembles()
            break
        elif choice == "V" or choice == "v":
            view_ensemble_musicians(selected_ensemble)

        elif choice == "B" or choice ==  "b":
            list_ensembles()
            break
        elif choice == "E" or choice =="e":
            exit_program()
        else:
            console.print('Invalid Choice', style='error')
        

def ensemble_options_menu():
    print("Type U or u to update this ensemble")
    print("Type D or d to delete this ensemble")
    print("Type V or v to view this ensemble's musicians")
    print("Type B or b to go back to ensemble menu")
    print("Type E or e to exit the program")

def musicians():
    while True:
        musicians_menu()
        choice = input("> ")
        if choice == "V" or choice == "v":
            list_musicians()
        elif choice == "A" or choice == "a":
            add_musician()
        elif choice == "N" or choice == "n":
            find_musician_by_name()
        elif choice == "I" or choice == "i":
            view_musicians_by_instrument()
        elif choice == "B" or choice == "b":
            break
        elif choice == "E" or choice =="e":
            exit_program()
        else:
            print('Invalid Choice')

def musicians_menu():
    console.print("Musician Menu", style="bold underline cyan on black")
    print("Type V or v to view all enrolled musicians")
    print("Type A or a to add a musician")
    print("Type N or n to find a musician by name")
    print("Type I or i to view the musicians that play a particular instrument")
    print("Type B or b to go back to ensemble menu")
    print("Type E or e to exit the program")





    





if __name__ == "__main__":
    main()
