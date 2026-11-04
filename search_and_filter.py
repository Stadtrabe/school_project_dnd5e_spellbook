class Spell:
    def __init__(self,
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
                concentration):

        self.spell_id = spell_id
        self.name = name
        self.level = level
        self.school_id = school_id
        self.desc = desc
        self.higher_level = higher_level
        self.damage_type_id = damage_type_id
        self.dc_type = dc_type
        self.dc_success = dc_success
        self.components_id = components_id
        self.material = material
        self.range = range
        self.casting_time = casting_time
        self.ritual = ritual
        self.duration = duration
        self.concentration = concentration

    def map_from_db(self, row):
        self.spell_id = row[0]
        self.name = row[1]
        self.level = row[2]
        self.school_id = row[3]
        self.desc = row[4]
        self.higher_level = row[5]
        self.damage_type_id = row[6]
        self.dc_type = row[7]
        self.dc_success = row[8]
        self.components_id = row[9]
        self.material = row[10]
        self.range = row[11]
        self.casting_time = row[12]
        self.ritual = row[13]
        self.duration = row[14]
        self.concentration = row[15]

    def print_info(self):
        print(f"""
    ========================================
    {self.name}
    ========================================
    ID:             {self.spell_id}
    Level:          {self.level}
    School ID:      {self.school_id}

    Casting Time:   {self.casting_time}
    Range:          {self.range}
    Duration:       {self.duration}
    Components ID:  {self.components_id}

    Ritual:         {self.ritual}
    Concentration:  {self.concentration}

    Damage Type ID: {self.damage_type_id}
    DC Type:        {self.dc_type}
    DC Success:     {self.dc_success}

    Material:
    {self.material}

    Description:
    {self.desc}

    Higher Level:
    {self.higher_level}
    ========================================
    """)

def search_by_id():
    
    
