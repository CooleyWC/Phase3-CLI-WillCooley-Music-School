#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.ensemble import Ensemble
from models.musician import Musician
import ipdb

# will = Musician('will', 'drums', 45, 33, 'yes')
# print(will)

jazz_ensemble_1 = Ensemble('jazz ensemble 1', 'basie', 'advanced')
print(jazz_ensemble_1)



ipdb.set_trace()
