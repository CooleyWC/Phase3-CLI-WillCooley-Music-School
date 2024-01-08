#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.ensemble import Ensemble
from models.musician import Musician

def seed_database():
    Musician.drop_table()
    Ensemble.drop_table()
    Ensemble.create_table()
    Musician.create_table()

    # seed data
    jazz_ensemble_1 = Ensemble.create('Jazz Ensemble 1', 'Count Basie', 'beginner')
    jazz_combo_1 = Ensemble.create('Jazz Combo 1', 'John Gunther', 'beginner')
    jazz_orchestra_3 = Ensemble.create('Jazz Orchestra 3', 'Antonio Sanchez', 'advanced')
    chamber_ensemble_2 = Ensemble.create('Percussion Ensemble', 'Will Cooley', 'intermediate')

    Musician.create('Philly Joe Jones', 'drums', 45, 99, 'no', jazz_ensemble_1.id)
    Musician.create('McCoy Tyner', 'piano', 25, 87, 'yes', jazz_combo_1.id)
    Musician.create('Miles Davis', 'trumpet', 26, 78, 'yes', jazz_combo_1.id)
    Musician.create('Ron Carter', 'bass', 42, 89, 'yes', jazz_ensemble_1.id)
    Musician.create('Charlie Parker', 'alto saxophone', 76, 98, 'no', jazz_ensemble_1.id)
    Musician.create('Tom Morello', 'guitar', 56, 75, 'yes', jazz_orchestra_3.id)
    Musician.create('Adam Cowger', 'drums', 34, 54, 'no', chamber_ensemble_2.id) 

seed_database()
print('seeded database')