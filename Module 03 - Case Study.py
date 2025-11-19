# ---
# Name: Zohaib Tunio
# File: Module 03 Lab - Case Study: Lists, Functions, and Classes
# Description: This Python program will use classes, inheritance, functions, and lists to create a simple vehicle information app.
# ---

# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# Function to gather user input and return an Automobile object
def create_automobile():
    print("Enter the details of your car:\n")

    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter roof type (solid or sun roof): ")

    # Vehicle type is always car for this assignment
    return Automobile("car", year, make, model, doors, roof)


# Function to display automobile information
def display_info(auto):
    print("\nVehicle Information")
    print("---------------------")
    print(f"Vehicle type: {auto.vehicle_type}")
    print(f"Year: {auto.year}")
    print(f"Make: {auto.make}")
    print(f"Model: {auto.model}")
    print(f"Number of doors: {auto.doors}")
    print(f"Type of roof: {auto.roof}")


# Main program using a list to store automobiles
def main():
    automobiles = []  # list to store multiple Automobile objects

    car = create_automobile()
    automobiles.append(car)

    # Print info for all stored automobiles
    for auto in automobiles:
        display_info(auto)


# Run the program
if __name__ == "__main__":
    main()
