
try:
    with open("names.csv", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'names.csv' was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")