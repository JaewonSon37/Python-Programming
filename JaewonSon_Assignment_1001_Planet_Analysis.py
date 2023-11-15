## Name: Jaewon Son
## Date: November 12 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/ccX8pXerW4Q


import math
import numpy as np
import matplotlib.pyplot as plt


# The first part of the assignment
class Planet:

    """ A class representing a planet.
    """

    def __init__(self, name, radius, year_length):

        """Initialize a planet with a name, radius, and year length.
        """

        self.name = name
        self.radius = radius
        self.year_length = year_length

    def position(self, day):

        """Calculate a position of the planet on a given day.

        Returns:
            tuple: Returns the 'x' and 'y' coordinates of the planet.
        """

        angle = (2 * math.pi * day) / self.year_length   # Compute an angle 
        coordinate_x = self.radius * math.cos(angle)   # Calculate X coordinate
        coordinate_y = self.radius * math.sin(angle)   # Calculate Y coordinate

        return coordinate_x, coordinate_y
    
    def __repr__(self):
        
        return f"{self.name}"


# Name of planets, orbital radius and year length
mercury = Planet("Mercury", 3.5, 88)
venus = Planet("Venus", 6.7, 225)
earth = Planet("Earth", 9.3, 365)
mars = Planet("Mars", 14.2, 687)
jupiter = Planet("Jupiter", 48.4, 4333)
saturn = Planet("Saturn", 88.9, 10759)
uranus = Planet("Uranus", 179, 30687)
neptune = Planet("Neptune", 288, 60190)


def distance(planet1, planet2, day):

    """Calculate the distance between two planets  a given day.

    Returns:
        float: Returns the distance between the two planets.
    """

    coordinate_x1, coordinate_y1 = planet1.position(day)   # Find a coordinate of 'planet1'
    coordinate_x2, coordinate_y2 = planet2.position(day)   # Find a coordinate of 'planet2'
    distance = math.sqrt((coordinate_x1 - coordinate_x2) ** 2 + (coordinate_y1 - coordinate_y2) ** 2)   # Calculate the Euclidean distance
    
    return distance


# Find the distance between Earth and Mars on day 732
planet1 = earth
planet2 = mars
day = 732
d = distance(planet1, planet2, day)
print(f"\nThe distance between {planet1} and {planet2} on day {day} is {d} million miles.\n")


# The second part of the assignment
def simulate_distance1(planet1, planet2, num_days, noisy = False):

    """Simulate the distance between two planets over a specified number of days with Zero-mean normal distribution with an STD = 0.5.

    Returns:
        list: Returns a list of simulated distances between the two planets.
    """
    
    np.random.seed(10)
    distances = []   # A list of distances between the two planets
    std = 0.5

    for day in range(num_days):
        if noisy:
            noise = np.random.normal(0, std)   # Zero-mean normal distribution with a STD = 0.5
        else:
            noise = 0   # Case of noiseless
        distances.append(distance(planet1, planet2, day) + noise)
    
    return distances


def simulate_distance2(planet1, planet2, num_days, noisy = True):

    """Simulate the distance between two planets over a specified number of days with Zero-mean normal distribution with an STD = 1.

    Returns:
        list: Returns a list of simulated distances between the two planets.
    """
    
    np.random.seed(10)
    distances = []   # A list of distances between the two planets
    std = 1

    for day in range(num_days):
        if noisy:
            noise = np.random.normal(0, std)   # Zero-mean normal distribution with a STD = 1
        distances.append(distance(planet1, planet2, day) + noise)
    
    return distances


# Find and plot the distances between Earth to Mercury, Venus, and Mars for 1,000 days without noise
planets = [mercury, venus, mars]
colors = ['cornflowerblue', 'forestgreen', 'crimson']
labels = ['Mercury', 'Venus', 'Mars']
num_days = 1000

for i, planet in enumerate(planets):
    noiseless_distances = simulate_distance1(earth, planet, num_days, noisy = False)
    plt.plot(noiseless_distances, label = f"Earth & {labels[i]}",alpha = 0.7, color = colors[i])
    plt.axhline(np.mean(noiseless_distances), linestyle = 'dashed', color = colors[i], label = f'Earth & {labels[i]} Average')

plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (CM)")
plt.title("Noiseless Distances Change over 1,000 days")
plt.show()


# Find and plot the distances between Earth to Mercury, Venus, and Mars for 1,000 days with noise (STD = 0.5)
planets = [mercury, venus, mars]
colors = ['cornflowerblue', 'forestgreen', 'crimson']
labels = ['Mercury', 'Venus', 'Mars']
num_days = 1000

for i, planet in enumerate(planets):
    noisy_distances = simulate_distance1(earth, planet, num_days, noisy = True)
    plt.plot(noisy_distances, label = f"Earth & {labels[i]}", alpha = 0.5, color = colors[i])
    plt.axhline(np.mean(noisy_distances), linestyle = 'solid', alpha = 1, color = colors[i], label = f'Earth & {labels[i]} Average')

plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (CM)")
plt.title("Noisy Distances (STD = 0.5) Change over 1,000 days")
plt.show()


# Find and plot the distances between Earth to Mercury, Venus, and Mars for 1,000 days with noise (STD = 1)
planets = [mercury, venus, mars]
colors = ['cornflowerblue', 'forestgreen', 'crimson']
labels = ['Mercury', 'Venus', 'Mars']
num_days = 1000

for i, planet in enumerate(planets):
    noisy_distances = simulate_distance2(earth, planet, num_days, noisy = True)
    plt.plot(noisy_distances, label = f"Earth & {labels[i]}", alpha = 0.5, color = colors[i])
    plt.axhline(np.mean(noisy_distances), linestyle = 'solid', alpha = 1, color = colors[i], label = f'Earth & {labels[i]} Average')

plt.legend()
plt.xlabel("Days")
plt.ylabel("Distance (CM)")
plt.title("Noisy Distances (STD = 1) Change over 1,000 days")
plt.show()


# Compute the average daily distances for all pairs of planets and create an 8x8 matrix
num_years = 1000
average_distances_matrix = np.zeros((8, 8))   # Create an 8x8 matrix
planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

for planet1 in range(len(planet_list)):
    for planet2 in range(len(planet_list)):
        average_distance = np.mean(simulate_distance1(planet_list[planet1], planet_list[planet2], num_years * 365, noisy = False))   # Compute the average distances
        average_distances_matrix[planet1, planet2] = np.around(average_distance, decimals = 2)   # Append a value to the matrix

print("Average Daily Distance for All Pairs of Planets:")
print(f"{average_distances_matrix}\n")