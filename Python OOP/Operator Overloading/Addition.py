class Math:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x) + (self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x) + (self.y - other.y)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def __truediv__(self, other):
        return (self.x / other.x) + (self.y / other.y)

    def __gt__(self, other):
        if (self.x + self.y) > (other.x + other.y):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.x + self.y) < (other.x + other.y):
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.x + self.y) == (other.x + other.y):
            return True
        else:
            return False

#test part        
a = Math(15, 20)
b = Math(30, 20)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("a > b ?", a > b)
print("a < b ?", a < b)
print("a == b ?", a == b)
