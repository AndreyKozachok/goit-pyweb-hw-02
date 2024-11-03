from addressbook import AddressBook
from record import Record
from book_storage import load_data, seve_data


not_found_message = "Contact does not exist, you can add it."


# Декоратор помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return str(error)
    return inner


@input_error
# Функція add_contact призначена для додавання нового контакту до AddressBook.
def add_contact(args, book: AddressBook): 
    name, phone = args # args, який є списком і містить ім'я та телефонний номер
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
# Функція для зміни контакту
def change_contacts(args, book: AddressBook):
    if len(args) != 3:
        return "Exactly 3 arguments [name], [old_number], [new_number] are required."
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return not_found_message
    else:
        record.edit_phone(old_number, new_number)
    return "Phone changed."


@input_error
#
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Exactly 1 argument (name) is required.")
    name = args[0]
    record = book.find(name)
    if record is None:
        return not_found_message
    return record


@input_error
#____________________________________________________
def get_all_contatcs(book: AddressBook):
    if not book:
        return "Contacts are empty."
    else:
        output = "Contacts:"
        for name, phone in book.items():
            output += f"\n{name}: {phone}"
        return output


@input_error
#
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        return "Invalid number arguments. Usage: [name], [date]."
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return not_found_message
    

@input_error
#
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        return "Invalid number arguments. Usage: [name]."
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return "Birthday not added to this contact."
    else:
        return not_found_message
    

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@ input_error
def main():
    book = load_data()
    print("Walcome to the assistense bot !")
    while True:
        command = input("Enter a command: ")
        command, *args = parse_input(command)

        if command in ["close", "exit"]:
            seve_data(book)
            print("Good bay!")
            break
        elif command == "hello":
            print("How can I help you ?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(book.get_upcoming_birthdays())        
        elif command == "change":
            print(change_contacts(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(get_all_contatcs(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()







