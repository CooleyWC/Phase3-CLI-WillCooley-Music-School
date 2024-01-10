# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician

def list_ensembles():
    ensembles = Ensemble.get_all()
    for i, ensemble in enumerate(ensembles, start=1):
        print(i, ensemble.name)

# why do i not need to subtract the number by one?
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

# if the selected ensembles id matches the musicians ensemble_id attribute, return just those matching musicians
def view_ensemble_musicians(num):
    ensemble = Ensemble.find_by_id(num)
    if ensemble:
        print(f"{ensemble.name}")
        ensemble_musicians = ensemble.musicians()
        for i, musician in enumerate(ensemble_musicians, start=1):
            print(f"{i} Name: {musician.name}, Instrument: {musician.instrument}, Age: {musician.age}, Audition Score: {musician.audition_score}, Enrolled in Private Lessons?: {musician.private_lessons}")

def list_musicians():
    musicians = Musician.get_all()
    for i, musician in enumerate(musicians, start=1):
        print(f"{i} Name: {musician.name}, Instrument: {musician.instrument}, Age: {musician.age}, Audition Score: {musician.audition_score}, Enrolled in Private Lessons?: {musician.private_lessons}, Ensemble ID: {musician.ensemble_id}")

def add_musician():
    name = input("Type the new musician's name: ")
    instrument = input("Type the new musician's instrument: ")
    age = int(input("Type the musician's age: "))
    audition_score = int(input("Type the musician's audition_score: "))
    private_lessons = input("Is the musician in enrolled in private lessons? (yes or no): ")
    ensemble_id = int(input("Enter the id of the ensemble the musician was placed in: "))
    try:
        musician = Musician.create(name, instrument, age, audition_score, private_lessons, ensemble_id)
        print(f"Success: {musician.name} was successfully created")
    except Exception as exc:
        print("Uh oh there was an error creating your musician", exc)
