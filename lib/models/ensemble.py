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
            self._name = name
        else:
            raise ValueError('must be a string and between 4 and 12 characters')
        
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, director):
        if isinstance(director, str) and 2 <= len(director) <= 20:
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

    @classmethod
    def create(cls, name, director, level):
        ensemble = cls(name, director, level)
        ensemble.save()
        return ensemble
    
    def update(self):
        sql = """
            UPDATE ensembles
            SET name = ?, director = ?, level = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.director, self.level, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM ensembles
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        ensemble = cls.all.get(row[0])
        if ensemble:
            ensemble.name = row[1]
            ensemble.director = row[2]
            ensemble.level = row[3]
        else:
            ensemble = cls(row[1], row[2], row[3])
            ensemble.id = row[0]
            cls.all[ensemble.id] = ensemble
        return ensemble
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM ensembles
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM ensembles
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM ensembles
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_director(cls, director):
        sql = """
            SELECT *
            FROM ensembles
            WHERE director is ?
        """

        row = CURSOR.execute(sql, (director, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_level(cls, level):
        sql = """
            SELECT *
            FROM ensembles
            WHERE level is ?
        """

        row = CURSOR.execute(sql, (level, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def musicians(self):
        from models.musician import Musician
        sql = """
            SELECT *
            FROM musicians
            WHERE ensemble_id = ?
        """
        CURSOR.execute(sql, (self.id, ),)

        rows = CURSOR.fetchall()
        return [
            Musician.instance_from_db(row) for row in rows
        ]