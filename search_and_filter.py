from connect_database import connectDatabase
from models import Spell

def search_by_id(password):

    input_ids = input("Which spells do you want to search for? Enter IDs or ranges separated by spaces (e.g. 1 3-6 100): ").split()

    if not input_ids:
        print("No ID entered!")
        return

    searched_ids = []

    try:
        for id in input_ids:

            if "-" in id:

                if id.count("-") != 1:
                    print(f"Invalid range: {id}")
                    return

                start, end = id.split("-")

                start = int(start)
                end = int(end)

                if start > end:
                    print(f"Invalid range: {id}. Start must be smaller than end.")
                    return

                searched_ids.extend(range(start, end + 1))

            else:
                searched_ids.append(int(id))

    except ValueError:
        print("Invalid input! Please enter numbers or ranges.")
        return

    searched_ids = list(set(searched_ids))

    placeholders = ", ".join(["%s"] * len(searched_ids))

    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursorPre = connection.cursor(prepared=True)
    
    search_id_query = f"""
    SELECT
        spells.*,
        magicSchools.name,
        damageTypes.name,
        components.components
    FROM spells
    INNER JOIN magicSchools
        ON spells.school_id = magicSchools.school_id
    LEFT JOIN damageTypes
        ON spells.damage_type_id = damageTypes.damage_type_id
    INNER JOIN components
        ON spells.components_id = components.components_id
    WHERE spells.spell_id IN ({placeholders})
    ORDER BY spells.spell_id
    """

    
    cursorPre.execute(search_id_query, tuple(searched_ids,))
    result = cursorPre.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            spell = Spell()
            spell.map_from_db(row)
            spell.print_info()

    cursorPre.close()
    connection.close()

def search_by_name(password):

    search_input = input(
        "Enter a word to search for in spell names: "
    ).strip()

    if not search_input:
        print("No search term entered!")
        return

    search_word = f"%{search_input}%"

    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursorPre = connection.cursor(prepared=True)
    
    search_name_query = """
    SELECT
        spells.*,
        magicSchools.name,
        damageTypes.name,
        components.components
    FROM spells
    INNER JOIN magicSchools
        ON spells.school_id = magicSchools.school_id
    LEFT JOIN damageTypes
        ON spells.damage_type_id = damageTypes.damage_type_id
    INNER JOIN components
        ON spells.components_id = components.components_id
    WHERE spells.name LIKE %s
    """
    cursorPre.execute(search_name_query, (search_word,))
    result = cursorPre.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            spell = Spell()
            spell.map_from_db(row)
            spell.print_info()


    cursorPre.close()
    connection.close()

def filter_by_level(password):

    try:
        enter_level = int(input("Which spell level do you want to filter by? (Enter 0 to 9): "))
    except ValueError:
        print("Invalid input! Please enter a number from 0 to 9.")
        return

    if not 0 <= enter_level <= 9:
        print("Invalid spell level! Please enter a number from 0 to 9.")
        return

    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursorPre = connection.cursor(prepared=True)
    
    filter_level_query = """
    SELECT
        spells.*,
        magicSchools.name,
        damageTypes.name,
        components.components
    FROM spells
    INNER JOIN magicSchools
        ON spells.school_id = magicSchools.school_id
    LEFT JOIN damageTypes
        ON spells.damage_type_id = damageTypes.damage_type_id
    INNER JOIN components
        ON spells.components_id = components.components_id
    WHERE spells.level = %s
    """
    cursorPre.execute(filter_level_query, (enter_level,))
    result = cursorPre.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            spell = Spell()
            spell.map_from_db(row)
            spell.print_info()


    cursorPre.close()
    connection.close()

def filter_by_school(password):


    print("""
    ✦══════════════════════════════════════✦
                MAGIC SCHOOLS
    ✦══════════════════════════════════════✦

    1 - Abjuration
    2 - Conjuration
    3 - Divination
    4 - Enchantment
    5 - Evocation
    6 - Illusion
    7 - Necromancy
    8 - Transmutation

    ✦══════════════════════════════════════✦
    """)

    try:
        enter_school = int(input("Which magic school do you want to filter by? (Enter 1 to 8): "))
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 8.")
        return

    if not 1 <= enter_school <= 8:
        print("Invalid input! Please enter a number from 1 to 8.")
        return
    
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursorPre = connection.cursor(prepared=True)
    
    filter_school_query = """
    SELECT
        spells.*,
        magicSchools.name,
        damageTypes.name,
        components.components
    FROM spells
    INNER JOIN magicSchools
        ON spells.school_id = magicSchools.school_id
    LEFT JOIN damageTypes
        ON spells.damage_type_id = damageTypes.damage_type_id
    INNER JOIN components
        ON spells.components_id = components.components_id
    WHERE magicSchools.school_id = %s
    """
    cursorPre.execute(filter_school_query, (enter_school,))
    result = cursorPre.fetchall()
    if not result:
        print(f"No spells found!")
    else:
        for row in result:
            spell = Spell()
            spell.map_from_db(row)
            spell.print_info()


    cursorPre.close()
    connection.close()