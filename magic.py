def main(): 
    # Array of dictionaries - each student has name, power, and house
    students = [
        {"name": "Aria Flameheart", "power": "Pyromancy", "house": "Ignis"},
        {"name": "Luna Shadowweaver", "power": "Umbramancy", "house": "Nocturna"},
        {"name": "Orion Starfall", "power": "Astral Magic", "house": "Celestia"},
        {"name": "Seraphina Moonsong", "power": "Lunar Magic", "house": "Lunaria"},
        {"name": "Kai Oceanstrider", "power": "Hydromancy", "house": "Aquaria"},
        {"name": "Zephyr Windwhisper", "power": "Aeromancy", "house": "Ventus"},
        {"name": "Terra Stoneheart", "power": "Geomancy", "house": "Terram"},
        {"name": "Elara Lightbringer", "power": "Photomancy", "house": "Lux"},
        {"name": "Draven Ironwood", "power": "Phytomancy", "house": "Silva"},
        {"name": "Nova Spark", "power": "Electromancy", "house": "Fulmen"},
        {"name": "Cora Frostveil", "power": "Cryomancy", "house": "Glacies"},
        {"name": "Silas Ravenwood", "power": "Necromancy", "house": "Umbra"},
        {"name": "Lyra Dreamweaver", "power": "Oneiromancy", "house": "Somnus"},
        {"name": "Jax Thunderclap", "power": "Sonomancy", "house": "Tonitrus"},
        {"name": "Maya Timewalker", "power": "Chronomancy", "house": "Tempus"},
        {"name": "Finn Goldenspell", "power": "Alchemy", "house": "Aurum"},
        {"name": "Ivy Vinethorn", "power": "Nature Magic", "house": "Viridia"},
        {"name": "Rex Ironfist", "power": "Telekinesis", "house": "Motus"},
        {"name": "Zara Mindbender", "power": "Telepathy", "house": "Mens"},
        {"name": "Leo Sunforge", "power": "Solar Magic", "house": "Sol"},
        # Adding more students with repeated powers but different houses
        {"name": "Blaze Emberheart", "power": "Pyromancy", "house": "Ignis"},
        {"name": "Frost Winterborn", "power": "Cryomancy", "house": "Glacies"},
        {"name": "Storm Cloudbreaker", "power": "Aeromancy", "house": "Ventus"},
        {"name": "Gaia Earthshaper", "power": "Geomancy", "house": "Terram"},
        {"name": "Mindy Thoughtweaver", "power": "Telepathy", "house": "Mens"},
        {"name": "Golem Rockfist", "power": "Telekinesis", "house": "Motus"},
        {"name": "Alchemist Goldfinder", "power": "Alchemy", "house": "Aurum"},
        {"name": "Dreamer Nightwhisper", "power": "Oneiromancy", "house": "Somnus"}
    ]
    
    print("Welcome to the Student Magic School!")
    print("Here are the students who have chosen their magic path:\n")
    
    # Loop through array of dictionaries
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} - {student['power']} - House: {student['house']}")
    
    print("\n" + "="*60)
    print("STUDENTS BY MAGIC SPECIALTY:")
    print("="*60)
    
    # Find students with specific powers
    target_powers = ["Pyromancy", "Cryomancy", "Telepathy", "Alchemy"]
    
    for power in target_powers:
        print(f"\n🔥 {power} Specialists:")
        found_students = [s for s in students if s["power"] == power]
        if found_students:
            for student in found_students:
                print(f"   • {student['name']} (House: {student['house']})")
        else:
            print("   No students found with this power")
    
    print("\n" + "="*60)
    print("STUDENTS BY HOUSE:")
    print("="*60)
    
    # Group students by house
    houses = {}
    for student in students:
        house = student["house"]
        if house not in houses:
            houses[house] = []
        houses[house].append(student)
    
    for house, members in houses.items():
        print(f"\n🏰 House {house}:")
        for student in members:
            print(f"   • {student['name']} - {student['power']}")

if __name__ == "__main__":
    main()