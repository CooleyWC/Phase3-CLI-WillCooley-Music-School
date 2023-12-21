from models.__init__ import CURSOR, CONN
from models.ensemble import Ensemble

class Musician:

    def __init__(self, name, age, grade, audition_score, private_lessons, id=None):
        self.name = name
        self.age = age
        self.grade = grade
        self.audition_score = audition_score
        self.private_lessons = private_lessons
        self.id = id