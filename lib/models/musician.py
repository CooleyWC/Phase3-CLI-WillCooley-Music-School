from models.__init__ import CURSOR, CONN
from models.ensemble import Ensemble

class Musician:

    VALID_INSTRUMENTS = ['guitar', 'piano', 'bass', 'drums', 'vibraphone', 'trumpet', 'trombone', 'bass trombone', 'alto saxophone', 'tenor saxophone', 'baritone saxophone', 'voice']

    all = {}

    def __init__(self, name, instrument, age, audition_score, private_lessons, ensemble_id, id=None):
        self.name = name
        self.instrument = instrument
        self.age = age
        self.audition_score = audition_score
        self.private_lessons = private_lessons
        self.id = id
        self.ensemble_id = ensemble_id

    def __repr__(self):
        return f'Musician {self.id}: {self.name}, {self.instrument}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 < len(name) <= 20:
            self._name = name
        else: 
            raise ValueError('name must be a non-empty string greater than 2 and less than 20')
        
    @property
    def instrument(self):
        return self._instrument
    
    @instrument.setter
    def instrument(self, instrument):
        if instrument.lower() not in Musician.VALID_INSTRUMENTS:
            raise ValueError('needs to be in the valid instrument list')
        else:
            self._instrument = instrument
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('must be an integer and between 18 and 99')
        
    @property
    def audition_score(self):
        return self._audition_score
    
    @audition_score.setter
    def audition_score(self, audition_score):
        if isinstance(audition_score, int) and 1 <= audition_score <=100:
            self._audition_score = audition_score
        else:
            raise ValueError('must be an integer between 1 and 100')
        
    @property
    def private_lessons(self):
        return self._private_lessons
    
    @private_lessons.setter
    def private_lessons(self, private_lessons):
        if isinstance(private_lessons, str) and private_lessons.lower() == 'yes' or private_lessons.lower() == 'no':
            self._private_lessons = private_lessons
        else:
            raise ValueError('must be a string and yes or no')


    @property
    def ensemble_id(self):
        return self._ensemble_id

    @ensemble_id.setter
    def ensemble_id(self, ensemble_id):
        if type(ensemble_id) is int and Ensemble.find_by_id(ensemble_id):
            self._ensemble_id = ensemble_id
        else: 
            raise ValueError('ensemble id must reference the ensemble in the database')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS musicians (
            id INTEGER PRIMARY KEY,
            name TEXT,
            instrument TEXT,
            age INTEGER,
            audition_score INTEGER,
            private_lessons TEXT,
            ensemble_id INTEGER,
            FOREIGN KEY (ensemble_id) REFERENCES ensembles(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS musicians;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO musicians (name, instrument, age, audition_score, private_lessons, ensemble_id)
            VALUES (?, ? , ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.instrument, self.age, self.audition_score, self.private_lessons, self.ensemble_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE musicians
            SET name = ?, instrument = ?, age = ?, audition_score = ?, private_lessons = ?, ensemble_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.instrument, self.age, self.audition_score, self.private_lessons, self.ensemble_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM musicians
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, instrument, age, audition_score, private_lessons, ensemble_id):
        musician = cls(name, instrument, age, audition_score, private_lessons, ensemble_id)
        musician.save()
        return musician
    
    @classmethod
    def instance_from_db(cls, row):
        musician = cls.all.get(row[0])
        if musician:
            musician.name = row[1]
            musician.instrument = row[2]
            musician.age = row[3]
            musician.audition_score = row[4]
            musician.private_lessons = row[5]
            musician.ensemble_id = row[6]
        else:
            musician = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            musician.id = row[0]
            cls.all[musician.id] = musician
        return musician
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM musicians
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM musicians
            WHERE id = ?
        """ 
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM musicians
            WHERE name is ?
        """ 
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_instrument(cls, instrument):
        sql = """
            SELECT *
            FROM musicians
            WHERE instrument is ?
        """ 
        rows = CURSOR.execute(sql, (instrument,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    # new
    def ensemble(self):
        sql = """
            SELECT *
            FROM ensembles
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.ensemble_id, ),)
        row = CURSOR.fetchone()
        return Ensemble.instance_from_db(row) if row else None