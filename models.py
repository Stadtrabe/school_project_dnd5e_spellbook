class Spell:
    def __init__(self,
            spell_id=None,
            name=None,
            level=None,
            #school_id=None,
            desc=None,
            higher_level=None,
            #damage_type_id=None,
            dc_type=None,
            dc_success=None,
            #components_id=None,
            material=None,
            range=None,
            casting_time=None,
            ritual=None,
            duration=None,
            concentration=None,
            school_name=None,
            damage_type=None,
            components=None):

        self.spell_id = spell_id
        self.name = name
        self.level = level
        #self.school_id = school_id
        self.desc = desc
        self.higher_level = higher_level
        #self.damage_type_id = damage_type_id
        self.dc_type = dc_type
        self.dc_success = dc_success
        #self.components_id = components_id
        self.material = material
        self.range = range
        self.casting_time = casting_time
        self.ritual = ritual
        self.duration = duration
        self.concentration = concentration
        self.school_name = school_name
        self.damage_type = damage_type
        self.components = components

    def map_from_db(self, row):
        self.spell_id = row[0]
        self.name = row[1]
        self.level = row[2]
        #self.school_id = row[3]
        self.desc = row[4]
        self.higher_level = row[5]
        #self.damage_type_id = row[6]
        self.dc_type = row[7]
        self.dc_success = row[8]
        #self.components_id = row[9]
        self.material = row[10]
        self.range = row[11]
        self.casting_time = row[12]
        self.ritual = row[13]
        self.duration = row[14]
        self.concentration = row[15]
        self.school_name = row[16]
        self.damage_type = row[17]
        self.components = row[18]

    def print_info(self):
        print(f"""
✦══════════════════════════════════════✦
{self.name}
✦══════════════════════════════════════✦
Spell ID:       {self.spell_id}
Level:          {self.level}
School:         {self.school_name}

Description:
{self.desc}
    """)

        if self.higher_level is not None:
            print(f"""On higher Level:
{self.higher_level}
    """)

        print(f"""Components:     {self.components}
    """)

        if self.material is not None:
            print(f"""Material:
{self.material}
    """)

        print(f"""Casting Time:   {self.casting_time}
Ritual:         {"YES" if self.ritual else "NO"}
Range:          {self.range}
Duration:       {self.duration}
Concentration:  {"YES" if self.concentration else "NO"}
    """)

        if self.damage_type is not None:
            print(f"Damage Type:    {self.damage_type}")

        if self.dc_type is not None:
            print(f"DC Type:        {self.dc_type}")

        if self.dc_success is not None:
            print(f"DC Success:     {self.dc_success}")

        print("✦══════════════════════════════════════✦")


class DamageTypes:
    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc

    def map_from_db(self, row):
        self.name = row[1]
        self.desc = row[2]

    def print_info(self):
        print(f"""
✦{self.name}✦

Description:
{self.desc}

        """)


class MagicSchools:
    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc

    def map_from_db(self, row):
        self.name = row[1]
        self.desc = row[2]

    def print_info(self):
        print(f"""
✦{self.name}✦

Description:
{self.desc}

        """)