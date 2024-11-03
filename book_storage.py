import pickle

from addressbook import AddressBook

PKL_FILE = "addressbook.pkl"

def seve_data(book, filename=PKL_FILE):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_data(filename=PKL_FILE):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
 
