import copy
import random


# Consider using the modules imported above.
class Hat:

    def __init__(self, **balls):
        self.contents = []

        """
        writes the number of each colours in a single tuple
        for example blue = 4 or so => [blue, blue, blue, blue]
        """
        for index in balls:
            for j in range(balls[index]):
                self.contents.append(index)

    """
    if you need the original list unchanged when a new list is modified => use the copy() method
    """
    def draw(self, number):
        if number >= len(self.contents):
            return self.contents

        newcontents = []
        for index in range(number):
            n = self.contents.pop(random.randrange(len(self.contents)))
            newcontents.append(n)

        return newcontents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for index in range(num_experiments):
        chat = copy.deepcopy(hat)
        tmp = chat.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if tmp.count(key) < value:
                success = False
                break
        if success:
            count += 1
    return count/num_experiments
