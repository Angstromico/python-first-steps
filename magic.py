def main(): 
    # Dictionary of students and their powers (key: student, value: power)
    students = {
        "Aria Flameheart": "Pyromancy",
        "Luna Shadowweaver": "Umbramancy",
        "Orion Starfall": "Astral Magic",
        "Seraphina Moonsong": "Lunar Magic",
        "Kai Oceanstrider": "Hydromancy",
        "Zephyr Windwhisper": "Aeromancy",
        "Terra Stoneheart": "Geomancy",
        "Elara Lightbringer": "Photomancy",
        "Draven Ironwood": "Phytomancy",
        "Nova Spark": "Electromancy",
        "Cora Frostveil": "Cryomancy",
        "Silas Ravenwood": "Necromancy",
        "Lyra Dreamweaver": "Oneiromancy",
        "Jax Thunderclap": "Sonomancy",
        "Maya Timewalker": "Chronomancy",
        "Finn Goldenspell": "Alchemy",
        "Ivy Vinethorn": "Nature Magic",
        "Rex Ironfist": "Telekinesis",
        "Zara Mindbender": "Telepathy",
        "Leo Sunforge": "Solar Magic",
        # Adding more students with repeated powers
        "Blaze Emberheart": "Pyromancy",
        "Frost Winterborn": "Cryomancy",
        "Storm Cloudbreaker": "Aeromancy",
        "Gaia Earthshaper": "Geomancy",
        "Mindy Thoughtweaver": "Telepathy",
        "Golem Rockfist": "Telekinesis",
        "Alchemist Goldfinder": "Alchemy",
        "Dreamer Nightwhisper": "Oneiromancy"
    }
    
    print("Welcome to the Student Magic School!")
    print("Here are the students who have chosen their magic path:\n")
    
    # Loop through dictionary with keys and values
    for i, (student, power) in enumerate(students.items(), 1):
        print(f"{i}. {student} - {power}")
    
    print("\n" + "="*50)
    print("STUDENTS BY MAGIC SPECIALTY:")
    print("="*50)
    
    # Find students with specific powers
    target_powers = ["Pyromancy", "Cryomancy", "Telepathy", "Alchemy"]
    
    for power in target_powers:
        print(f"\n🔥 {power} Specialists:")
        found_students = [student for student, pwr in students.items() if pwr == power]
        if found_students:
            for student in found_students:
                print(f"   • {student}")
        else:
            print("   No students found with this power")


if __name__ == "__main__":
    main()