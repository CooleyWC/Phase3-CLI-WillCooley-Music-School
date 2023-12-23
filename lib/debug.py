#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.ensemble import Ensemble
from models.musician import Musician
import ipdb

will = Musician('will', 'drums', 45, 33, False)
print(will)
will.instrument = 'piano'
print(will)
# will.instrument = 'kazoo'

# print(will)

ipdb.set_trace()
