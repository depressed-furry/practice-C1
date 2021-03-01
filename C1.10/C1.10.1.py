class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_info(self):
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"


r1, r2 = Rectangle(5, 10, 15, 50), Rectangle(100, 480, 665, 290)
print(r1.get_info(), r2.get_info(), sep="\n")
