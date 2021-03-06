import copy
import random

class Hat():
    def __init__(self, **kwargs):
        self.contents = list()
        self.selection = list()
        for key, value in kwargs.items():       # convert arguments from {"red": 2, "blue": 1} format into a list such as ["red", "red", "blue"]
            for _ in range(value):
                self.contents.append(key)

    def draw(self, draw_num):
        if draw_num > len(self.contents):       # If the number of balls to draw exceeds the available quantity, return all the balls.
            return self.contents
        else:
            for _ in range(draw_num):
                contents_length = len(self.contents)
                index = random.randint(0, contents_length-1)
                self.selection.append(self.contents[index])                 # Add the ball at that random index to the selection list
                del self.contents[index]                                    # Remove that ball from the hat
            return self.selection
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0   # number of 'successful' experiments where the expected balls were drawn
    for _ in range(num_experiments):            # This loop represents a single experiment. It executes the number of times specified by the num_experiments argument
        hat_copy = copy.deepcopy(hat)           # Create fresh copy of the hat (& its contents) for each experiment (this is necessary because the draw method deletes the members that it "draws" from the contents list)
        sel = hat_copy.draw(num_balls_drawn)          # Draw random balls from the hat contents, and return the selection list
        selection_dict = dict()                 # Convert selection list into a dictionary of counts for easier comparison against expected balls dictionary
        for elem in sel:         # Iterate over elements in the selection list
            if elem not in selection_dict:      # If the color name doesn't already exist in the dictionary
                selection_dict[elem] = 1            # Add it to the dictionary and initialize its value to 1
            else:                               # If the color name is already in the dictionary
                selection_dict[elem] += 1           # Increment its value
        # Begin comparing the expected_balls against what was actually drawn in this experiment
        success = len(expected_balls.keys())    
        i = 0
        for color in expected_balls.keys():
            if color not in selection_dict.keys() or expected_balls[color] > selection_dict[color]:
                break
            else:
                i += 1
        if i == success:
            m += 1      # If the experiment was a success, increment m
    prob = m/num_experiments          # Calculate and return the probability of success
    return prob