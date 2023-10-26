## Name: Jaewon Son
## Date: October 26 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/t3r4iZd_q1k


import math


class Pseudorandom_Number_Generator:

    """Generates pseudorandom numbers based on character pairs read from the War and Peace text file.
    """

    def __init__(self, seed=0, step=100, file_path = "C:\\Users\\LG\\Desktop\\DEPAUL UNIV\\2023 Fall\\Python Programming\\DSC 430 - Week 7\\WarAndPeace.txt"):

        """Default constructor.
        """

        self.seed = seed
        self.step = step
        self.file_path = file_path
        self.character_pair_list = []
        self.file_length = 0


    def read_file(self):

        """Reads the War and Peace text file.
        """

        with open(self.file_path, "r") as infile:
            infile.seek(0, 2)   # Move the file pointer to a specific position
            self.file_length = infile.tell()   # Get the current position of the file pointer


    def character_pair(self, initial_point):

        """Reads character pairs from the text file starting from the initial_point.

        Returns:
            tuple: Returns a tuple containing character1 and character2.
        """

        with open(self.file_path, "r") as infile:
            infile.seek(initial_point % self.file_length)   # If 'initial_point' exceeds the length of the file, it wraps around to the beginning of the file
            character1 = infile.read(1)   # Read one character
            infile.seek((initial_point + self.step) % self.file_length)   # If 'initial_point' exceeds the length of the file, it wraps around to the beginning of the file
            character2 = infile.read(1)   # Read another character

        return character1, character2


    def pseudorandom(self, min_value = 0, max_value = 1):

        """Generates a pseudorandom value.

        Returns:
            float: Returns a pseudorandom value
        """

        self.character_pair_list = []   # Store pairs of characters
        self.read_file()
        r = 0   # Initialize a variable called 'r' to 0
        power = 1   # Initialize a variable called 'power' to 1

        while len(self.character_pair_list) <= 32:
            character1, character2 = self.character_pair(self.seed)
            if character1 != character2:
                self.character_pair_list.append((character1, character2))
            self.seed = (self.seed + self.step) % self.file_length   # Update the 'seed' value

        for (character1, character2) in self.character_pair_list:
            if character1 > character2:
                r += 1 / (2 ** power)   # Calculate the value 'r'
            power += 1

        return r * (max_value - min_value) + min_value


class Point:

    def __init__(self, x = 0, y = 0):

        """Default constructor.
        """

        self.x = x
        self.y = y
   

    def distance(self, point):

        """Calculate the distance between two points.

        Returns:
            float: Returns the distance between two points.
        """

        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)   # Calculate the distance with the Euclidean method


    def __repr__(self):

        """Returns a string of the 'Point'.

        Returns:
            str: Returns a string of the 'Point'.
        """

        return f"Point({self.x}, {self.y})"
      

class Ellipse:

    def __init__(self, focal_point1, focal_point2, width):

        """Default constructor.
        """

        self.p1 = focal_point1
        self.p2 = focal_point2
        self.width = width
    

    def check_point_inside(self, point):

        """Check if the point is inside the ellipse.

        Returns:
            bool: Returns True if the point is inside the ellipse, False otherwise.
        """

        return self.p1.distance(point) + self.p2.distance(point) < self.width


def compute_overlap_of_ellipses(ellipse1, ellipse2):

    """Compute the area of overlap between two ellipses.

    Returns:
        float: Returns the estimated area of overlap between the two ellipses.
    """

    left_x_point = min(ellipse1.p1.x, ellipse2.p1.x) - max(ellipse1.width, ellipse2.width) * 1/2   # Get a left x coordinate of a rectangle
    right_x_point = max(ellipse1.p1.x, ellipse2.p1.x) + max(ellipse1.width, ellipse2.width) * 1/2   # Get a right x coordinate of a rectangle
    bottom_y_point = min(ellipse1.p1.y, ellipse2.p1.y) - max(ellipse1.width, ellipse2.width) * 1/2   # Get a bottom y coordinate of a rectangle
    top_y_point = min(ellipse1.p1.y, ellipse2.p1.y) + max(ellipse1.width, ellipse2.width) * 1/2   # Get a top y coordinate of a rectangle
    rectangle_area = (top_y_point - bottom_y_point) * (right_x_point - left_x_point)   # Calculate a rectangle area   

    pseudorandom_number = Pseudorandom_Number_Generator(1000)   # Seed value is 1,000
    iteration = 10000   # Generate 10,000 random points

    number_of_overlap_point = 0

    for _ in range(iteration):
        
        x = pseudorandom_number.pseudorandom(left_x_point, right_x_point)
        y = pseudorandom_number.pseudorandom(bottom_y_point, top_y_point)
        r_point = Point(x, y)

        if ellipse1.check_point_inside(r_point) and ellipse2.check_point_inside(r_point):   # Check a point is inside the both ellipses
            number_of_overlap_point += 1

    overlap_area = number_of_overlap_point / iteration * rectangle_area   # Calculate estimated overlap area

    return overlap_area

if __name__ == '__main__':
    ellipse1 = Ellipse(Point(0, 0), Point(0, 0), 4)
    ellipse2 = Ellipse(Point(0, 0), Point(0, 0), 4)
    overlap_area = compute_overlap_of_ellipses(ellipse1, ellipse2)
    print(f"Overlap area between two ellipses is {overlap_area}")

    ellipse3 = Ellipse(Point(3, 7), Point(0, 0), 8)
    ellipse4 = Ellipse(Point(7, 3), Point(0, 0), 8)
    overlap_area = compute_overlap_of_ellipses(ellipse3, ellipse4)
    print(f"Overlap area between two ellipses is {overlap_area}")