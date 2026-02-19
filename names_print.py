def main(): 
    names = []
    with open("name.txt", "r") as file:
        texts = file.readlines()
        for name in texts:
            names.append(name.strip())

    for name in sorted(names, reverse=True):
            print(name)


if __name__ == "__main__":
    main()
