# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician

def list_ensembles():
    ensembles = Ensemble.get_all()
    for i, ensemble in enumerate(ensembles, start=1):
        print(i, ensemble.name)

def view_ensemble(num):
    id_ = num
    ensemble = Ensemble.find_by_id(id_)
    print(f"You selected: {num}\n {ensemble.name} \n Director: {ensemble.director} \n Level: {ensemble.level}")

def update_ensemble(num):
    id_ = num
    if ensemble := Ensemble.find_by_id(id_):
        try:
            name = input("Enter the ensemble's new name: ")
            ensemble.name = name
            director = input("Enter the ensemble's new director: ")
            ensemble.director = director
            level = input("Enter the ensemble's new level - must be one of the following all lowercase ('beginner', 'intermediate', 'advanced'): ")
            ensemble.level = level

            ensemble.update()
            print(f"{ensemble.name} was successfully updated")
        except Exception as exc:
            print(f"Error updating Ensemble", exc)
    else:
        print("Invalid number selection")

def delete_ensemble(num):
    id_ = num
    if ensemble := Ensemble.find_by_id(id_):
        ensemble.delete()
        print(f"Ensemble {id_} was successfully deleted.")
    else:
        print(f"Error: check that you selected a correct number corresponding to an ensemble")


def exit_program():
    print("see ya later")
    exit()

def add_ensemble():
    name = input("Enter the new ensemble's name: ")
    director = input("Enter the new ensemble's director: ")
    level = input("Enter the ensembles level (beginniner, intermediate, or advanced): ")
    try:
        ensemble = Ensemble.create(name, director, level)
        print(f"Success: {ensemble.name} has been added")
    except Exception as exc:
        print("Uh-Oh: There has been a problem with adding your ensemble", exc)

# find a way to make this case insensitive
def find_ensemble_by_director():
    name = input("Type the director's name: ")
    ensemble = Ensemble.find_by_director(name)
    if ensemble:
        print(f"{ensemble.director} is the director of {ensemble.name}")
    else:
        print('director not found')

# this currently only finds just the first instance that matches the level but not all
def find_ensemble_by_level():
    level = input("Type the level of the ensemble: ")
    ensemble = Ensemble.find_by_level(level)
    if ensemble:
        print(f"{ensemble.name} is {ensemble.level}")
    else:
        print('no ensembles match the entered level')
