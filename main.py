from create_delete_databases import create_databases, delete_databases
from fill_tables import fill_in, clear_tables

def main():
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
                createAndDelete()
            case "2":
                fillAndClear()
            case "0":
                print("Programm closed!")
                running = False
            case _:
                print("Invalid input!")

def createAndDelete():
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
                create_databases()
            case "2":
                delete_databases()
            case "0":
                print("Menu closed!")
                running = False
            case _:
                print("Invalid input!")

def fillAndClear():
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
                fill_in()
            case "2":
                clear_tables()
            case "0":
                print("Menue closed!")
                running = False
            case _:
                print("Invalid input!")
    
main()

