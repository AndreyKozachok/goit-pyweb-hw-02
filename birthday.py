from field import Field
from datetime import datetime
from contacts import DATE_FORMAT


# Birthday: 
class Birthday(Field):
    def __init__(self, value):
        try: # перетворення рядка на об'єкт datetime
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self) -> str:
        return f"{self.value.strftime(DATE_FORMAT)}"
    
