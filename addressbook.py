from collections import UserDict
from datetime import datetime, date, timedelta
from contacts import DATE_FORMAT

def is_weekend_day(day: int) -> bool:
    return day > 4

# AddressBook: Клас для зберігання та управління записами.
class AddressBook(UserDict):
    def __str__(self) -> str:
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)
    
    def add_record(self, record): # Додавання записів
        if record.name.value in self.data:
            raise KeyError(f"Record with name {record.name.value}, already exists!")
        self.data[record.name.value] = record

    def find(self, name): # Пошук записів за іменем.
        return self.data.get(name)
       

    def delete(self, name): # Видалення записів за іменем.
        del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        congratulation_day = None
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday_date = record.birthday.value.replace(year=today.year).date()
                timedelta_days = (birthday_date - today).days

                if 0 <= timedelta_days <= 7:
                    if is_weekend_day(birthday_date.weekday()):
                        days_delta = 2
                        if birthday_date.weekday() == 5:
                            congratulation_day = birthday_date + timedelta(days=days_delta)
                        else:
                            return 1 
                    else:
                        congratulation_day = birthday_date
                    
                    upcoming_birthdays.append({"name": name, "congratulation_day": congratulation_day.strftime(DATE_FORMAT)})
        
        return upcoming_birthdays


