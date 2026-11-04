import getpass

from create_delete_databases import create_databases, delete_databases
from fill_tables import fill_in, clear_tables
from connect_database import connectDatabase

def main():

    password = getpass.getpass(
        "MySQL password: ",
        echo_char="*"
    )

    # Connection Test
    connection = connectDatabase(password)
    if connection is None:
        print("Program closed!")
        return
    connection.close()

    running = True

    while running:
        
        print("""
        \n
        ---   DnD 5e (2014) Spellbook   ---
        ===         Main menu           ===
        1 - Create & Delete databases
        2 - Fill & clear tables
        0 - Exit
        """)

        choice = input("Choose an option: ")

        match choice:
            case "1":
                createAndDeleteMenu(password)
            case "2":
                fillAndClearMenu(password)
            case "0":
                print("Programm closed!")
                running = False
            case _:
                print("Invalid input!")

def createAndDeleteMenu(password):
    running = True
    
    while running:
        print("""
        \n
        ---   DnD 5e (2014) Spellbook   ---
        === Create and Delete Databases ===
        1 - Create databases
        2 - Delete databases
        0 - Exit
        """)

        choice = input("Choose an option: ")

        match choice:
            case "1":
                create_databases(password)
            case "2":
                delete_databases(password)
            case "0":
                print("Menu closed!")
                running = False
            case _:
                print("Invalid input!")

def fillAndClearMenu(password):
    running = True
    
    while running:
        print("""
        \n
        ---   DnD 5e (2014) Spellbook   ---
        ===     Fill & clear tables     ===
        1 - Fill tables
        2 - Clear tables
        0 - Exit
        """)

        choice = input("Choose an option: ")

        match choice:
            case "1":
                fill_in(password)
            case "2":
                clear_tables(password)
            case "0":
                print("Menue closed!")
                running = False
            case _:
                print("Invalid input!")
    
main()

