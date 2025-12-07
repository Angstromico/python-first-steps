def main(): 
    hello_world = "Hello, World!"
    substring_hello = hello_world[0:5]
    substring_world = hello_world[7:]

    print("Original string:", hello_world)
    print("Substring 'Hello':", substring_hello)
    print("Substring 'World':", substring_world)

    email = "user@example.com"
    email_index = email.index("@")
    username = email.split("@")[0]
    domain = email.split("@")[1]

    print("Email:", email)
    print("Email index:", email_index)
    print("Username:", username)
    print("Domain:", domain)

    chain_to_search = "Find the needle in the haystack."
    substring_to_find = "needle"
    substring_to_exchange = "haystack"
    substring_to_replace = "stack"
    found_index = chain_to_search.find(substring_to_find)
    new_chain = chain_to_search.replace(substring_to_exchange, substring_to_replace)

    print("Chain to search:", chain_to_search)
    print("Substring to find:", substring_to_find)
    print("Found index:", found_index)
    print("Substring to exchange:", substring_to_exchange)
    print("Substring to replace:", substring_to_replace)
    print("New chain after replacement:", new_chain)

    hello = 'Hello '
    hello_five_times = hello * 5

    print("Original string:", hello)
    print("String repeated five times:", hello_five_times)


if __name__ == "__main__":
    main()
