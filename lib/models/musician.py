from models.__init__ import CURSOR, CONN
from models.ensemble import Ensemble

class Musician:

    VALID_INSTRUMENTS = ['guitar', 'piano', 'bass', 'drums', 'vibraphone', 'trumpet', 'trombone', 'bass trombone', 'alto saxophone', 'tenor saxophone', 'baritone saxophone', 'voice']

    def __init__(self, name, instrument, age, audition_score, private_lessons, id=None):
        self.name = name
        self.instrument = instrument
        self.age = age
        self.audition_score = audition_score
        self.private_lessons = private_lessons
        self.id = id

    def __repr__(self):
        return f'Employee {self.id}: {self.name}, {self.instrument}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 15:
            print(f'...setting name to {name}')
            self._name = name
        else: 
            raise ValueError('name must be a non-empty string greater than 2 and less than 15')
        
    @property
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, instrument):
        if type(instrument) != str:
            raise ValueError('needs to be a string')
        elif instrument.lower() not in Musician.VALID_INSTRUMENTS:
            raise ValueError('needs to be in the valid instrument list')
        else:
            print(f'...setting instrument to {instrument}')
            self._instrument = instrument
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 18 <= age <= 99:
            print(f'...setting age to {age}')
            self._age = age
        else:
            raise ValueError('must be an integer and between 18 and 99')
        
    @property
    def audition_score(self):
        return self._audition_score
    
    @audition_score.setter
    def audition_score(self, audition_score):
        if isinstance(audition_score, int) and 1 <= audition_score <=100:
            print(f'...setting audition score to {audition_score}')
            self._audition_score = audition_score
        else:
            raise ValueError('must be an integer between 1 and 100')
        
    @property
    def private_lessons(self):
        return self._private_lessons
    
    @private_lessons.setter
    def private_lessons(self, private_lessons):
        if isinstance(private_lessons, str) and private_lessons.lower() == 'yes' or private_lessons.lower() == 'no':
            print(f'...setting private lesson status to {private_lessons}')
            self._private_lessons = private_lessons
        else:
            raise ValueError('must be a string and yes or no')

    

