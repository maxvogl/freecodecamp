class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(1/2)

    def get_picture(self):
        if self.width > 50:
            return "Too big for picture."
        else:
            line = ""
            for row in range(self.height):
                line += "*" * self.width + "\n"
            return line

    def get_amount_inside(self, other):
        return (self.width//other.width) * (self.height//other.height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={})".format(self.width)
