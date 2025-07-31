import pandas as pd
import re

class InvalidFloorFormatError(Exception):
    """Raised when the floor format in dataset is invalid."""
    def __init__(self, floor_value):
        self.floor_value = floor_value
        super().__init__(f"Invalid floor format: {floor_value}")

def validate_floor(floor_value):
    pattern = r"^(Ground|\d+)\s+out\s+of\s+\d+$"
    if not re.match(pattern, floor_value.strip()):
        raise InvalidFloorFormatError(floor_value)
    return floor_value

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    
    # Validate floor column
    invalid_rows = []
    for index, row in df.iterrows():
        try:
            validate_floor(str(row["Floor"]))
        except InvalidFloorFormatError:
            invalid_rows.append(index)

    print(f"Total invalid floor entries: {len(invalid_rows)}")
    return df

def search_by_city(df, city):
    results = df[df["City"].str.lower() == city.lower()]
    print(results if not results.empty else "No results found.")

def search_by_rent_range(df, min_rent, max_rent):
    results = df[(df["Rent"] >= min_rent) & (df["Rent"] <= max_rent)]
    print(results if not results.empty else "No results found.")

def search_by_bhk(df, bhk):
    results = df[df["BHK"] == bhk]
    print(results if not results.empty else "No results found.")

def search_by_floor(df, floor):
    results = df[df['Floor'] == floor]
    print(results if not results.empty else "No results found.")

def menu():
    df = load_dataset("./data/house_rent.csv")
    
    while True:
        print("\n--- House Rent Search Menu ---")
        print("1. Search by City")
        print("2. Search by Rent Range")
        print("3. Search by BHK")
        print("4. Search by Floor")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city = input("Enter city name: ")
            search_by_city(df, city)
        
        elif choice == "2":
            min_rent = int(input("Enter minimum rent: "))
            max_rent = int(input("Enter maximum rent: "))
            search_by_rent_range(df, min_rent, max_rent)
        
        elif choice == "3":
            bhk = int(input("Enter BHK value: "))
            search_by_bhk(df, bhk)
        
        elif choice == "4":
            floor = validate_floor(input("Enter Floor Value: "))
            search_by_floor(df, floor)

        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
