# lib/helpers.py
from models.ensemble import Ensemble
from models.musician import Musician
from rich.theme import Theme
from rich.console import Theme
from rich.style import Style

from rich.console import Console
from rich.table import Table

custom_theme = Theme({'success': 'green', 'error': 'bold red'})
console = Console(theme=custom_theme)

def list_ensembles():
    table = Table(title = 'All Ensembles')
    ensembles = Ensemble.get_all()
    table.add_column(' ')
    table.add_column('Ensemble', style='deep_sky_blue1')
    for i, ensemble in enumerate(ensembles, start=1):
        table.add_row(str(i), ensemble.name)
    console = Console()
    console.print(table)

def view_ensemble(num):
    console = Console(theme=custom_theme)
    all_ensembles = Ensemble.get_all()

    if not 1 <= num <= len(all_ensembles):
        console.print("Invalid Choice. Must correspond to a ensemble number. Type B or b to try again.", style='error')
        return

    table = Table(title='Ensemble Details')
    table.add_column(" ")
    table.add_column("Name", style='cyan')
    table.add_column("Director", style='medium_orchid')
    table.add_column("Level")

    ensemble = all_ensembles[num-1]
    if ensemble: 
        table.add_row(str(num), ensemble.name, ensemble.director, ensemble.level)
        console.print(table)
    else:
        console.print("Invalid choice", style='error')


def update_ensemble(num):
    all_ensembles = Ensemble.get_all()
    ensemble = all_ensembles[num-1]

    if ensemble:
        try:
            name = input("Enter the ensemble's new name: ")
            ensemble.name = name
            director = input("Enter the ensemble's new director: ")
            ensemble.director = director
            level = input("Enter the ensemble's new level - must be one of the following all lowercase ('beginner', 'intermediate', 'advanced'): ")
            ensemble.level = level

            ensemble.update()
            console.print(f"{ensemble.name} was successfully updated", style='success')
        except Exception as exc:
            console.print(f"Error updating Ensemble", exc, style='error')
    else:
        console.print("Invalid number selection", style='error')

def delete_ensemble(num):
    all_ensembles = Ensemble.get_all()
    ensemble = all_ensembles[num-1]
    if ensemble:
        ensemble.delete()
        console.print(f"Ensemble: {ensemble.name} was successfully deleted.", style='success')
    else:
        console.print(f"Error: check that you selected a correct number corresponding to an ensemble", style='error')


def exit_program():
    console.print("see ya later", style='spring_green3')
    exit()

def add_ensemble():
    console = Console(theme=custom_theme)
    name = input("Enter the new ensemble's name: ")
    director = input("Enter the new ensemble's director: ")
    level = input("Enter the ensembles level (beginner, intermediate, or advanced): ")
    try:
        ensemble = Ensemble.create(name, director, level)
        console.print(f"Success: {ensemble.name} has been added", style='success')
    except Exception as exc:
        console.print("Uh-Oh: There has been a problem with adding your ensemble", exc, style='error')

def find_ensemble_by_director():
    console = Console(theme=custom_theme)
    name = input("Type the director's name (Include first and last name and titlecase ex: Will Cooley): ")
    ensemble = Ensemble.find_by_director(name)
    if ensemble:
        console.print(f"{ensemble.director} is the director of {ensemble.name}", style='success')
    else:
        console.print(f'Uh oh: {name} was not found', style='error')

def find_ensemble_by_level():
    console = Console(theme=custom_theme)
    level = input("Type the level of the ensemble (must be either beginner, intermediate, or advanced): ")
    ensembles = Ensemble.find_by_level(level)

    table = Table(title=f'Ensembles by Level: {level}')
    table.add_column(" ")
    table.add_column("Name", style='cyan')
    table.add_column("Director", style='magenta')

    if ensembles:
        for i, ensemble in enumerate(ensembles, start=1):
            table.add_row(str(i), ensemble.name, ensemble.director)
        console.print(table)
    else:
        console.print(f'Uh oh - No ensembles found matching {level}', style='error')

def view_ensemble_musicians(num):
    all_ensembles = Ensemble.get_all()
    ensemble = all_ensembles[num-1]

    table = Table(title='Musicians')
    table.add_column(" ")
    table.add_column("Name", justify='left', style='cyan', no_wrap=True)
    table.add_column("Instrument", style="magenta")
    table.add_column("Age")
    table.add_column('Audition Score')
    table.add_column('Enrolled in Private Lessons')

    if ensemble:
        print(f"{ensemble.name}")
        ensemble_musicians = ensemble.musicians()
        for i, musician in enumerate(ensemble_musicians, start=1):
            table.add_row(str(i), musician.name, musician.instrument, str(musician.age), str(musician.audition_score), musician.private_lessons)
    console = Console()
    console.print(table)

def list_musicians():
    table = Table(title='All Musicians')
    table.add_column("number")
    table.add_column("Name", justify='left', style='cyan', no_wrap=True)
    table.add_column("Instrument", style="magenta")
    table.add_column("Age")
    table.add_column('Audition Score')
    table.add_column('Private Lessons?')
    table.add_column('Ensemble placement', style='green4')

    musicians = Musician.get_all()
    all_ensembles = Ensemble.get_all()

    ensemble_name_dict = {ensemble.id: ensemble.name for ensemble in all_ensembles}

    for i, musician in enumerate(musicians, start=1):
        ensemble_id = musician.ensemble_id
        if ensemble_id in ensemble_name_dict:
            ensemble_name = ensemble_name_dict[ensemble_id]
        else:
            ensemble_name = "Info Not Available"

        table.add_row(str(i), musician.name, musician.instrument, str(musician.age), str(musician.audition_score), musician.private_lessons, ensemble_name)

    console = Console()
    console.print(table)

def add_musician():
    name = input("Type the new musician's name: ")
    if name.isdigit():
        console.print('Invalid input: cannot be a number', style='error')
        return
    instrument = input("Type the new musician's instrument: ")
    age = (input("Type the musician's age: "))
    audition_score = (input("Type the musician's audition_score: "))
    private_lessons = input("Is the musician in enrolled in private lessons? (yes or no): ")
    ensemble_name = input("Confirm the ensemble placement by typing the name of the ensemble the musician is placed in: ")
    found_ensemble = Ensemble.find_by_name(ensemble_name)

    if found_ensemble:
        try:
            musician = Musician.create(name, instrument, int(age), int(audition_score), private_lessons, int(found_ensemble.id))
            console.print(f"Success: {musician.name} was successfully created", style='success')
        except Exception as exc:
            console.print("Uh oh: There was an error creating your musician", exc, style='error')
    else:
        console.print('Uh oh: There was an error creating your musician', style='error')


def find_musician_by_name():
    console = Console(theme=custom_theme)
    name = input("Type the musician's name (Include first and last name and titlecase ex: Will Cooley): ")
    musician = Musician.find_by_name(name)

    table = Table(title='Musician Details')
    table.add_column("Name", justify='right', style='cyan', no_wrap=True)
    table.add_column("Instrument", style="magenta")
    table.add_column("Age")
    table.add_column('Audition Score')
    table.add_column('Enrolled in Private Lessons')
    if musician:
        musician_style_name = Style(color='cyan', bold=True)
        console.print(f"[{musician_style_name}]{musician.name}[/] is enrolled, he plays the {musician.instrument}. Would you like to see more details?")
        answer = input("Type yes or no: ")
        if answer == 'yes':
            table.add_row(musician.name, musician.instrument, str(musician.age), str(musician.audition_score), musician.private_lessons)
            console = Console()
            console.print(table)
        else:
            console.print('Okay - You typed something other than yes - back to Musician menu', style='success')
    else:
        console.print(f"Uh oh - {name} was not found", style='error')

def view_musicians_by_instrument():
    console = Console(theme=custom_theme)
    instrument_select = input("Type an instrument: ")
    table = Table(title='Musicians by Instrument')
    table.add_column("")
    table.add_column("Name", style='cyan')
    table.add_column("Instrument", style='magenta')
    instrument = Musician.find_by_instrument(instrument_select)
    if instrument:
        for i, musician in enumerate(instrument, start=1):
            table.add_row(str(i), musician.name, musician.instrument)
        console.print(table)
    else:
        console.print(f'Uh oh - it appears we do not have any {instrument_select} players here', style='error')


def delete_musician():
    name = input("Enter the musician's name (First and Last and Titlecased): ")
    selected_musician = Musician.find_by_name(name)
    
    if selected_musician:
        confirm = input("Are you sure you want to delete this musician (yes or no)?: ")
        if confirm == 'yes':
            selected_musician.delete()
            console.print(f"{selected_musician.name} was successfully deleted.", style='success')
        else:
            console.print(f"{selected_musician.name} was NOT deleted")
            return
    else:
        console.print('There was an error deleting the selected musician', style='error')

def update_musician():
    console = Console(theme=custom_theme)
    name = input("Confirm the name of the musician you would like to update (First and Last and Titlecased): ")
    musician = Musician.find_by_name(name)

    if musician:
        try:
            name = input("Type the musician's updated name: ")
            musician.name = name
            instrument = input("Type the musician's instrument: ")
            musician.instrument = instrument
            age = input("Type the musician's age: ")
            musician.age = int(age)
            audition_score = input("Type the musician's audition score: ")
            musician.audition_score = int(audition_score)
            private_lessons = input("Is the musician in enrolled in private lessons? (yes or no): ")
            musician.private_lessons = private_lessons
            ensemble = input("Type the name of the ensemble the musician is placed in: ")
            found_ensemble = Ensemble.find_by_name(ensemble)
            musician.ensemble_id = int(found_ensemble.id)

            musician.update()
            console.print(f"{musician.name} was successfully updated.", style='success')
        except Exception as exc:
            console.print(f"Error updating musician", exc)
    else:
        console.print("There was an error confirming your musician - double check spelling and capitalization", style='error')





