# Phase 3 CLI+ORM Project

## :musical_score: Will Cooley's Music School

---

## Instructions

- Fork and clone from https://github.com/CooleyWC/Phase3-project-Cooley
- Run pipenv install and pipenv shell.
- You may initialize the database with sample data (Ensembles and Musicians) by runnning: `python lib/seed.py`
- Type: `python lib/cli.py` to begin the program.
- Follow the prompts to interact with Will Cooley's Music School.

---

## File Structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── ensemble.py
    │   └── musician.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

---

## Main Menu

![display-filter](/Photos/Main_Menu.png)

### Main Options

- Direct to ensembles menu
- Direct to musicians menu

---

## Ensembles Menu

![display-filter](/Photos/Ensemble_Menu.png)

### Ensemble Options

- View an ensembles details
  - Access to sub ensemble menu
- Add a new ensemble
- Find an ensemble by director
- Find an ensemble by level

---

## Sub Ensemble Menu

![display-filter](/Photos/Sub_Ensemble_Menu.png)

### Sub Ensemble Options

- Update an ensemble
- Delete an ensemble
- View the ensemble's musicians
  - Within this selection, you can add , update, or delete a musician.

---

## Musicians Menu

![display-filter](/Photos/Musician_Menu.png)

### Musician Options

- View all musicians
  - Access to sub musicians menu
- Find a musician by name
- View musicians by instrument

---

## Sub Musicians Menu

![display-filter](/Photos/Sub_Musician_Menu.png)

### Sub Musician Options

- Add a musician
- Delete a musician

---

## Support

If you have any questions, you can find me on Discord: cooleywc
