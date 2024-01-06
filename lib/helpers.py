# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician

def list_ensembles():
    ensembles = Ensemble.get_all()
    for i, ensemble in enumerate(ensembles, start=1):
        print(i, ensemble.name)

def view_ensemble(num):
    id_ = num - 1
    ensemble = Ensemble.find_by_id(id_)
    print(f"You selected: {num}\n {ensemble.name} \n Director: {ensemble.director} \n Level: {ensemble.level}")


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
