# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician

def list_ensembles():
    ensembles = Ensemble.get_all()
    for ensemble in ensembles:
        print(ensemble)


def exit_program():
    print("see ya later")
    exit()


