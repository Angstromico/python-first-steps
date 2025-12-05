import requests, sys, json

def main(): 
    if len(sys.argv) < 2:
        sys.exit("You must provide a song name as a command-line argument.")

    song_name = " ".join(sys.argv[1:])
    print("Searching for:", song_name)
    url = f"https://itunes.apple.com/search?term={song_name}&limit=1"
    response = requests.get(url)
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print("Response Data:", formatted_data)
    if data["resultCount"] == 0:
        sys.exit("Song not found.")

    print("Artist:", data["results"][0]["artistName"])




if __name__ == "__main__":
    main()
