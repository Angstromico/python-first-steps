import sys

def main(): 
    data = sys.argv
    print('Arguments passed to the script: ')
    print(data)
    print(f'Total number of arguments: {len(data)} ')
    print(f'Script name: {data[0]} ')
    if len(data) > 1:
        print(f'First argument: {data[1]} ')


if __name__ == "__main__":
    main()
