from connect_database import connectDatabase

def create_databases():

    connection = connectDatabase()
    if connection is None:
        return
    
    create_query = """
    CREATE DATABASE IF NOT EXISTS dnd5eSpellbookDB;

    USE dnd5eSpellbookDB;


    CREATE TABLE IF NOT EXISTS components (
        components_id INT NOT NULL,
        components VARCHAR(7),
        PRIMARY KEY (components_id)
    );


    CREATE TABLE IF NOT EXISTS damageTypes (
        damage_type_id INT NOT NULL,
        name VARCHAR(45),
        `desc` TEXT,
        PRIMARY KEY (damage_type_id)
    );


    CREATE TABLE IF NOT EXISTS magicSchools (
        school_id INT NOT NULL,
        name VARCHAR(45),
        `desc` TEXT,
        PRIMARY KEY (school_id)
    );


    CREATE TABLE IF NOT EXISTS spells (
        spell_id INT NOT NULL,
        name VARCHAR(30) NOT NULL,
        level INT NOT NULL,
        school_id INT NOT NULL,
        `desc` TEXT NOT NULL,
        higher_level TEXT,
        damage_type_id INT,
        dc VARCHAR(3),
        dc_success VARCHAR(20),
        components_id INT NOT NULL,
        material TEXT,
        `range` VARCHAR(45) NOT NULL,
        casting_time VARCHAR(45) NOT NULL,
        ritual TINYINT NOT NULL,
        duration VARCHAR(45) NOT NULL,
        concentration TINYINT NOT NULL,

        PRIMARY KEY (spell_id),

        FOREIGN KEY (school_id)
            REFERENCES magicSchools(school_id),

        FOREIGN KEY (damage_type_id)
            REFERENCES damageTypes(damage_type_id),

        FOREIGN KEY (components_id)
            REFERENCES components(components_id)
    );
    """

    cursor = connection.cursor()
    cursor.execute(create_query)
    
    cursor.close()
    connection.close()

    print("Database created")

def delete_databases():
    confirm = input("Do you really want to delete the database? (enter: DELETE) ")

    if confirm == "DELETE":

        connection = connectDatabase()       
        if connection is None:
            return
        
        cursor = connection.cursor()
        cursor.execute("DROP DATABASE IF EXISTS dnd5eSpellbookDB;")

        cursor.close()
        connection.close()

        print("Database deleted!")
    else:
        print("Database not deleted!")

