import cowsay, sys

def main(): 
    if len(sys.argv) == 2:
        cowsay.cow("Hello, " + sys.argv[1])
        cowsay.dragon("Hello, " + sys.argv[1])
        cowsay.trex("Hello, " + sys.argv[1])


if __name__ == "__main__":
    main()
