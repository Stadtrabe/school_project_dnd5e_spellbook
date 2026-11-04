from connect_database import connectDatabase
from models import Spell

def search_by_id(password):
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    cursor = connection.cursor()
    cursorPre = connection.cursor(prepared=True)

    # PLATZHALTER TEST
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

    cursor.close()
    cursorPre.close()
    connection.close()