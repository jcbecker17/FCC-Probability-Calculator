import copy
import random

class Hat():
    def __init__(self, **kwargs):
        # convert arguments from {"red": 2, "blue": 1} format into a list such as ["red", "red", "blue"]
        self.contents = list()
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, draw_num):
        if draw_num > len(self.contents):       # If the number of balls to draw exceeds the available quantity, return all the balls.
            return self.contents
        else:
            self.selection = list()
            for _ in range(draw_num):
                contents_length = len(self.contents)
                index = int(round((contents_length-1) * random.random()))
                print('LEN: ',contents_length, 'INDEX: ', index)
                self.selection.append(self.contents[index])
                del self.contents[index]
            return self.selection
    
# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):