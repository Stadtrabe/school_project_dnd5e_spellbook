import requests
from connect_database import connectDatabase

base_url = "https://www.dnd5eapi.co"

# reading from API

def get_school_data():
    school_url = f"{base_url}/api/2014/magic-schools/"
    response = requests.get(school_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Hat nicht geklappt... {response.status_code}")

def get_damagetype_data():
    damage_url = f"{base_url}/api/2014/damage-types/"
    response = requests.get(damage_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Hat nicht geklappt... {response.status_code}")

def get_spell_data():
    spell_url = f"{base_url}/api/2014/spells/"
    response = requests.get(spell_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Hat nicht geklappt... {response.status_code}")

# Mapping to db

def fill_in(password):
    
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    
    cursor = connection.cursor()
    cursorPre = connection.cursor(prepared=True)
    
    confirm = input(
    "Existing data will be deleted and replaced. Continue? (enter: FILL) "
    )

    if confirm != "FILL":
        print("Tables not filled!")
        return

    cursor.execute("DELETE FROM spells")
    cursor.execute("DELETE FROM components")
    cursor.execute("DELETE FROM damageTypes")
    cursor.execute("DELETE FROM magicSchools")

# damage types
    damagetype_data = get_damagetype_data()
    if damagetype_data:
        max_rows = len(damagetype_data["results"])
        damage_type_ids = {}    #dict for the FK damage_type_id

        for id, damage in enumerate(damagetype_data["results"], start=1):
            response = requests.get(f"{base_url}{damage["url"]}")
            damage_details = response.json()
            
            name = damage["name"]
            desc = damage_details["desc"][0]
            
            damage_query = """
            INSERT INTO damageTypes (damage_type_id, name, `desc`) 
            VALUES (%s, %s, %s)
            """
            
            cursorPre.execute(damage_query, (id, name, desc))

            damage_type_ids[damage["index"]] = id
            
            print(f"\rFilling table 'damageTypes': {id}/{max_rows} rows completed", end="")

    print("\nTable 'damageTypes' finished")
# components

    components_query = """
    INSERT INTO components (components_id, components)
    VALUES (0, NULL),
    (1, 'V, S, M'),
    (2, 'V, S'),
    (3, 'V, M'),
    (4, 'S, M'),
    (5, 'V'),
    (6, 'S'),
    (7, 'M')
    """
    cursor.execute(components_query)
    
    component_ids = {
    "V, S, M": 1,
    "V, S": 2,
    "V, M": 3,
    "S, M": 4,
    "V": 5,
    "S": 6,
    "M": 7
    }
    
    print("Table 'components' finished")


# magic schools
    school_data = get_school_data()
    if school_data:
        max_rows = len(school_data["results"])
        school_ids = {}     #dict for the FK school_id

        for id, school in enumerate(school_data["results"], start=1):
            response = requests.get(f"{base_url}{school["url"]}")
            school_details = response.json()
            
            name = school["name"]
            desc = school_details["desc"]
            
            school_query = """
            INSERT INTO magicSchools (school_id, name, `desc`) 
            VALUES (%s, %s, %s)
            """
            
            cursorPre.execute(school_query, (id, name, desc))
            
            school_ids[school["index"]] = id
            
            print(f"\rFilling table 'magicSchools': {id}/{max_rows} rows completed", end="")
    print("Table 'magicSchools' finished")

# spells
    spell_data = get_spell_data()
    if spell_data:
        max_rows = len(spell_data["results"])

        for id, spell in enumerate(spell_data["results"], start=1):
            response = requests.get(f"{base_url}{spell["url"]}")
            spell_details = response.json() 

            spell_id = id
            name = spell["name"]
            level = spell["level"]
            school_index = spell_details["school"]["index"]
            school_id = school_ids[school_index]
            desc = "\n".join(spell_details["desc"])

            higher_level = spell_details.get("higher_level")
            if higher_level:
                higher_level = "\n".join(higher_level)
            else:
                higher_level = None

            if spell_details["damage"] and "damage_type" in spell_details["damage"][0]:
                damage_index = spell_details["damage"][0]["damage_type"]["index"]
                damage_type_id = damage_type_ids[damage_index]
            else:
                damage_type_id = None

            dc = spell_details.get("dc")
            if dc:
                dc_type = dc["dc_type"]["name"]
                dc_success = dc["dc_success"]
            else:
                dc_type = None
                dc_success = None

            material = spell_details.get("material")
            components = ", ".join(spell_details["components"])
            components_id = component_ids[components]
            material = spell_details.get("material")
            range = spell_details["range"]
            casting_time = spell_details["casting_time"]
            ritual = int(spell_details["ritual"])
            duration = spell_details["duration"]
            concentration = int(spell_details["concentration"])

            
            spell_query = """
            INSERT INTO spells (
                spell_id,
                name,
                level,
                school_id,
                `desc`,
                higher_level,
                damage_type_id,
                dc,
                dc_success,
                components_id,
                material,
                `range`,
                casting_time,
                ritual,
                duration,
                concentration
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursorPre.execute(
            spell_query,(
                spell_id,
                name,
                level,
                school_id,
                desc,
                higher_level,
                damage_type_id,
                dc_type,
                dc_success,
                components_id,
                material,
                range,
                casting_time,
                ritual,
                duration,
                concentration
                )
            )

            print(f"\rFilling table 'magicSchools': {id}/{max_rows} rows completed", end="")

    print("Table 'spells' finished")

# end of fill_in()
    connection.commit()
    print("All tables are filled!")
    cursor.close()
    cursorPre.close()
    connection.close()

# clear
def clear_tables(password):
    connection = connectDatabase(password, "dnd5eSpellbookDB")
    if connection is None:
        return
    cursor = connection.cursor()

    confirm = input(f"Do you really want to delet all datas from the tables? (enter: CLEAR) ")

    if confirm == "CLEAR":
        cursor.execute("DELETE FROM spells;")
        cursor.execute("DELETE FROM components;")
        cursor.execute("DELETE FROM damagetypes;")
        cursor.execute("DELETE FROM magicschools;")

        connection.commit()
        print("All datas deleted!")
    else:
        print("Datas not deleted!")
    
    cursor.close()
    connection.close()