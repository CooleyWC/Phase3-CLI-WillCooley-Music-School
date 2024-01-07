#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.ensemble import Ensemble
from models.musician import Musician
import ipdb

def reset_database():
    Musician.drop_table()
    Ensemble.drop_table()
    Ensemble.create_table()
    Musician.create_table()

    # seed data
    jazz_ensemble_1 = Ensemble.create('Jazz Ensemble 1', 'basie', 'advanced')
    jazz_combo_1 = Ensemble.create('Jazz Combo 1', 'gunther', 'advanced')
    rock_band_2 = Ensemble.create('Elvis', 'Col. Parker', 'advanced')
    Musician.create('Philly Joe Jones', 'drums', 45, 99, 'no', jazz_ensemble_1.id)
    Musician.create('McCoy Tyner', 'piano', 25, 87, 'yes', jazz_combo_1.id)
    Musician.create('Miles Davis', 'trumpet', 26, 78, 'yes', jazz_combo_1.id)
    Musician.create('Ron Carter', 'bass', 42, 89, 'yes', jazz_ensemble_1.id)
    Musician.create('Charlie Parker', 'alto saxophone', 76, 98, 'no', jazz_ensemble_1.id)
    Musician.create('Tom Morello', 'guitar', 56, 75, 'yes', rock_band_2.id)

reset_database()
ipdb.set_trace()
