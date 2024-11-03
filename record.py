from phone import Phone
from name import Name
from birthday import Birthday



# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name): # ініціалізація за допомогою імені та порожнього списку
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self): # повертає рядкове представлення Record
        contact_info = f"Contact name: {self.name.value}, phones: {";".join(p.value for p in self.phones)}"
        
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info
              
    def add_phone(self, number: str): # Додавання номеру телефона до запису Record
        self.phones.append(Phone(number))

    def remove_phone(self, number): # Видалення номера телефона з запису.
        self.phone = number
        self.phones = list(filter(lambda phone: phone == number, self.phone))

    def edit_phone(self, old_number, new_number): # Редагування номеру телефона.
        self.old_number = old_number
        self.new_number = new_number
        self.phones = list(map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones))
    
    def find_phone(self, number): # Пошук телефону.
        for phone in self.phones:
            if phone.value == number:
                return phone        
    
    def add_birthday(self, date): # add_birthday, додає дату народження до контакту
        self.birthday = Birthday(date)