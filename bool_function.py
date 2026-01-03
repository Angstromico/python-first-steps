def main(): 
    #Examples of Falsy and Truthy values in Python
    falsy_values = [0, 0.0, "", [], {}, set(), None, False]
    truthy_values = [1, -1, 0.1, "Hello", [1, 2], {"key": "value"}, {1, 2}, True]

    print("Falsy values:")
    for value in falsy_values:
        print(f"  {value} -> {bool(value)}")

    print("\nTruthy values:")
    for value in truthy_values:
        print(f"  {value} -> {bool(value)}")

if __name__ == "__main__":
    main()
