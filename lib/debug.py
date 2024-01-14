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
    jazz_ensemble_1 = Ensemble.create('Jazz Ensemble 1', 'Count Basie', 'beginner')
    jazz_combo_1 = Ensemble.create('Jazz Combo 1', 'Miles Davis', 'beginner')
    jazz_orchestra_3 = Ensemble.create('Jazz Orchestra 3', 'Diana Krall', 'advanced')
    chamber_ensemble_2 = Ensemble.create('Percussion Ensemble', 'Al Payson', 'intermediate')
    rock_band_1 = Ensemble.create('Rock Band 1', 'Jimmy Page', 'intermediate')
    symphonic_winds = Ensemble.create('Symphonic Winds', 'Ray Cramer', 'advanced')

    Musician.create('Philly Joe Jones', 'drums', 45, 99, 'no', jazz_ensemble_1.id)
    Musician.create('McCoy Tyner', 'piano', 25, 87, 'yes', jazz_combo_1.id)
    Musician.create('Chet Baker', 'trumpet', 26, 78, 'yes', jazz_combo_1.id)
    Musician.create('Norah Jones', 'piano', 40, 91, 'yes', jazz_ensemble_1.id)
    Musician.create('Ron Carter', 'bass', 42, 89, 'yes', jazz_ensemble_1.id)
    Musician.create('Charlie Parker', 'alto saxophone', 76, 98, 'no', jazz_ensemble_1.id)
    Musician.create('Tom Morello', 'guitar', 56, 75, 'yes', rock_band_1.id)
    Musician.create('Taylor Swift', 'guitar', 31, 89, 'no', jazz_combo_1.id)
    Musician.create('Jim Ross', 'drums', 34, 54, 'no', chamber_ensemble_2.id)
    Musician.create('Chris Cornell', 'voice', 34, 53, 'no', rock_band_1.id)
    Musician.create('Chuck Mangione', 'trumpet', 45, 78, 'yes', jazz_ensemble_1.id)
    Musician.create('Red Garland', 'piano', 19, 56, 'yes', jazz_combo_1.id)
    Musician.create('Chris Lamb', 'drums', 34, 78, 'yes', chamber_ensemble_2.id)
    Musician.create('Jack Johnson', 'trombone', 46, 87, 'yes', jazz_orchestra_3.id)
    Musician.create('Chris Marton', 'trumpet', 44, 89, 'no', symphonic_winds.id)
    Musician.create('Patsy Dash', 'drums', 78, 97, 'no', symphonic_winds.id)

reset_database()
ipdb.set_trace()
