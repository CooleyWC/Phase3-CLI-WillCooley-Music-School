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
    Musician.create('Philly Joe Jones', 'drums', 45, 99, 'no', 1)
    Musician.create('McCoy Tyner', 'piano', 25, 87, 'yes', 2)
    Musician.create('Miles Davis', 'trumpet', 26, 78, 'yes', 2)
    Musician.create('Ron Carter', 'bass', 42, 89, 'yes', 1)
    Musician.create('Charlie Parker', 'alto saxophone', 76, 98, 'no', 1)

reset_database()
ipdb.set_trace()
