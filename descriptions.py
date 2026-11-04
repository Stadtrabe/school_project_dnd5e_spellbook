from connect_database import connectDatabase
from models import MagicSchools, DamageTypes

def school_description(password):
    
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM magicschools")
    result = cursor.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            school = MagicSchools()
            school.map_from_db(row)
            school.print_info()

    cursor.close()
    connection.close()

def damage_type_description(password):
    
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM damagetypes")
    result = cursor.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            damage_type = DamageTypes()
            damage_type.map_from_db(row)
            damage_type.print_info()

    cursor.close()
    connection.close()
    