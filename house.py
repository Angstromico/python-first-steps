def main():
    # -------------------------------------------------
    # Harry Potter characters (first + last name) and house
    # -------------------------------------------------
    hogwarts = [
        {"first": "Harry",      "last": "Potter",    "house": "Gryffindor"},
        {"first": "Hermione",   "last": "Granger",   "house": "Gryffindor"},
        {"first": "Ron",        "last": "Weasley",   "house": "Gryffindor"},
        {"first": "Draco",      "last": "Malfoy",    "house": "Slytherin"},
        {"first": "Luna",       "last": "Lovegood",  "house": "Ravenclaw"},
        {"first": "Cedric",     "last": "Diggory",   "house": "Hufflepuff"},
        {"first": "Neville",    "last": "Longbottom","house": "Gryffindor"},
        {"first": "Cho",        "last": "Chang",     "house": "Ravenclaw"},
        {"first": "Ginny",      "last": "Weasley",   "house": "Gryffindor"},
        {"first": "Albus",      "last": "Dumbledore","house": "Gryffindor"},
        {"first": "Severus",    "last": "Snape",     "house": "Slytherin"},
        {"first": "Minerva",    "last": "McGonagall","house": "Gryffindor"},
        {"first": "Filius",     "last": "Flitwick",  "house": "Ravenclaw"},
        {"first": "Pomona",     "last": "Sprout",    "house": "Hufflepuff"},
        {"first": "Rubeus",     "last": "Hagrid",    "house": "Gryffindor"},
        # add more characters here if you like
    ]

    query = input("Enter the name (first, last, or full) of a Harry Potter character: ").strip()

    # -----------------------------------------------------------------
    # 1. Try an exact full-name match first
    # -----------------------------------------------------------------
    for char in hogwarts:
        full = f"{char['first']} {char['last']}"
        if query.lower() == full.lower():
            print(f"{full} belongs to {char['house']}!")
            return

    # -----------------------------------------------------------------
    # 2. Split the input into tokens (first / last)
    # -----------------------------------------------------------------
    tokens = query.split()
    matches = []

    for char in hogwarts:
        # match if *any* token equals first name OR last name (case-insensitive)
        if any(t.lower() == char['first'].lower() for t in tokens) or \
           any(t.lower() == char['last'].lower()  for t in tokens):
            matches.append(char)

    # -----------------------------------------------------------------
    # 3. Decide what to show
    # -----------------------------------------------------------------
    if not matches:
        print(f"Error: No character found for '{query}'.")
        return

    if len(matches) == 1:
        m = matches[0]
        print(f"{m['first']} {m['last']} belongs to {m['house']}!")
    else:
        # more than one character shares the entered name → show list
        print(f"Multiple characters match '{query}':")
        for m in matches:
            print(f"  • {m['first']} {m['last']} – {m['house']}")


if __name__ == "__main__":
    main()