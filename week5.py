#Question 1
# Define the Superhero class
class Superhero:
    # Constructor to initialize the attributes of the superhero
    def __init__(self, name, power, city):
        self.name = name   # Name of the superhero
        self.power = power # Superpower of the superhero
        self.city = city   # City where the superhero operates

    # Method to simulate using the superhero's power
    def use_power(self):
        return f"{self.name} uses {self.power} to save the day in {self.city}!"

# Define the Sidekick class that inherits from Superhero
class Sidekick(Superhero):
    # Constructor to initialize the attributes of the sidekick
    def __init__(self, name, power, city, sidekick_name):
        super().__init__(name, power, city) # Initialize the parent class attributes
        self.sidekick_name = sidekick_name   # Name of the sidekick

    # Method for the sidekick to assist the superhero
    def assist(self):
        return f"{self.sidekick_name} assists {self.name} with their powers!"

#usage
hero = Superhero("Captain Swift", "super speed", "Metropolis") # Create a Superhero object
sidekick = Sidekick("Captain Swift", "super speed", "Metropolis", "Speedy") # Create a Sidekick object

# Print the result of using the superhero's power
print(hero.use_power())
# Print the result of the sidekick assisting the superhero
print(sidekick.assist())
#---------------------------------------------------End of Question 1-----------------------------------------------------

#QUESTION 2
# Define the base class Vehicle
class Vehicle:
    # Method to be implemented by subclasses
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Define the Car class that inherits from Vehicle
class Car(Vehicle):
    # Implement the move method for Car
    def move(self):
        return "Driving 🚗" # Describe the action of moving

# Define the Plane class that inherits from Vehicle
class Plane(Vehicle):
    # Implement the move method for Plane
    def move(self):
        return "Flying ✈️" # Describe the action of moving

# Define the Bicycle class that inherits from Vehicle
class Bicycle(Vehicle):
    # Implement the move method for Bicycle
    def move(self):
        return "Pedaling 🚲" # Describe the action of moving

#usage
vehicles = [Car(), Plane(), Bicycle()] # Create a list of vehicle objects

# Loop through each vehicle and print its move action
for vehicle in vehicles:
    print(vehicle.move()) # Call the move method and print the result