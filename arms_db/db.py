
import sqlite3
from dataclasses import dataclass
import os.path

connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'roll_of_arms.db'))
cursor = connection.cursor()


@dataclass
class Arm:
    blazon: str = ""
    name: str = None
    roll: str=None
    year: int = None
    country: str = None
    has_image: bool = False
    img_filename: str = None
    source_name: str = None
    source_url: str=None


    def save_to_db(self):
        try:
            cursor.execute(f"""
                Insert into arms
                values
                (
                    "{self.blazon}",
                    "{self.name}",
                    "{self.roll}",
                    "{self.year}",
                    "{self.country}",
                    {self.has_image},
                    "{self.img_filename or ""}",
                    "{self.source_name}",
                    "{self.source_url}"
                )
                """)
            connection.commit()
            return True
        except sqlite3.IntegrityError:
            # Likely a unique constraint. we already got this one
            return False

def recreate_table(connection, cursor):
    cursor.execute('''Drop TABLE arms''')
    
    cursor.execute('''CREATE TABLE arms
             ( 
              blazon text,
              name text,
              roll text,
              year int,
              country text,
              has_image bool,
              img_filename,
              source_name text,
              source_url text,
              unique(name, blazon, roll))''')

    connection.commit()



# recreate_table(connection, cursor)