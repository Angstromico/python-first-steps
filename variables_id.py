def main():
    # Example 1: Aliasing vs Copying
    a = [1, 2, 3]
    b = a              # b points to the same list
    c = a.copy()       # c is a new list with same content

    print("Aliasing vs Copying:")
    print("id(a):", id(a))
    print("id(b):", id(b), "→ same as a")
    print("id(c):", id(c), "→ different from a")

    # Example 2: Mutability
    x = 10
    print("\nInteger immutability:")
    print("id(x):", id(x))
    x += 1
    print("id(x after +=1):", id(x), "→ new id because integers are immutable")

    lst = [1, 2]
    print("\nList mutability:")
    print("id(lst):", id(lst))
    lst.append(3)
    print("id(lst after append):", id(lst), "→ same id because lists are mutable")

    # Example 3: String interning
    s1 = "hello"
    s2 = "hello"
    print("\nString interning:")
    print("id(s1):", id(s1))
    print("id(s2):", id(s2), "→ often same because Python interns small strings")

    # Example 4: Debugging references
    d1 = {"key": "value"}
    d2 = d1
    print("\nDictionary aliasing:")
    print("id(d1):", id(d1))
    print("id(d2):", id(d2), "→ same object")

if __name__ == "__main__":
    main()

