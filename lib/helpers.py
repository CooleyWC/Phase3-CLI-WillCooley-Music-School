# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician

from rich.console import Console
from rich.table import Table

# table = Table(title='All Musicians')

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

def view_ensemble_musicians(num):
    ensemble = Ensemble.find_by_id(num)
    if ensemble:
        print(f"{ensemble.name}")
        ensemble_musicians = ensemble.musicians()
        for i, musician in enumerate(ensemble_musicians, start=1):
            print(f"{i} Name: {musician.name}, Instrument: {musician.instrument}, Age: {musician.age}, Audition Score: {musician.audition_score}, Enrolled in Private Lessons?: {musician.private_lessons}")

def list_musicians():
    musicians = Musician.get_all()
    table = Table(title='All Musicians')
    table.add_column("number")
    table.add_column("Name", justify='right', style='cyan', no_wrap=True)
    table.add_column("Instrument", style="magenta")
    table.add_column("Age")
    table.add_column('Audition Score')
    table.add_column('Enrolled in Private Lessons')
    for i, musician in enumerate(musicians, start=1):
        table.add_row(str(i), musician.name, musician.instrument, str(musician.age), str(musician.audition_score), musician.private_lessons)

    console = Console()
    console.print(table)

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

def find_musician_by_name():
    name = input("Type the musician's name: ")
    musician = Musician.find_by_name(name)

    table = Table(title='Musician Details')
    table.add_column("Name", justify='right', style='cyan', no_wrap=True)
    table.add_column("Instrument", style="magenta")
    table.add_column("Age")
    table.add_column('Audition Score')
    table.add_column('Enrolled in Private Lessons')
    if musician:
        print(f"{musician.name} is enrolled, he plays the {musician.instrument}. Would you like to see more details?")
        answer = input("Type yes or no: ")
        if answer == 'yes':
            table.add_row(musician.name, musician.instrument, str(musician.age), str(musician.audition_score), musician.private_lessons)
            console = Console()
            console.print(table)
        else:
            print('okay')
    else:
        print(f"{name} was not found")

def view_musicians_by_instrument():
    pass
    instrument_select = input("Type an instrument: ")
    instrument = Musician.find_by_instrument(instrument_select)
    for i, musician in enumerate(instrument, start=1):
        print(f"{i} Name: {musician.name}, Instrument: {musician.instrument}")
    else:
        if not instrument:
            print(f'Uh oh - we do not have any {instrument_select} players here' )


