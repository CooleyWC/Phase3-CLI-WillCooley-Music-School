from models.__init__ import CURSOR, CONN


class Ensemble:

    ENSEMBLE_LEVELS = ['beginner', 'intermediate', 'advanced']

    all = {}
    
    def __init__(self, name, director, level, id=None):
        self.id = id
        self.name = name
        self.director = director
        self.level = level
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 4 <= len(name) <= 20:
            print(f'...setting ensemble name to: {name}')
            self._name = name
        else:
            raise ValueError('must be a string and between 4 and 12 characters')
        
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, director):
        if isinstance(director, str) and 2 <= len(director) <= 20:
            print(f'...setting director to: {director}')
            self._director = director
        else:
            raise ValueError('must be a string and between 2 and 20 characters')
        
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        if type(level) != str:
            raise ValueError('needs to be a string')
        elif level not in Ensemble.ENSEMBLE_LEVELS:
            raise ValueError('needs to be an acceptable ensemble level')
        else:
            print(f'...setting level to: {level}')
            self._level = level
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS ensembles (
            id INTEGER PRIMARY KEY,
            name TEXT,
            director TEXT,
            level TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS ensembles;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO ensembles (name, director, level)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.director, self.level))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self