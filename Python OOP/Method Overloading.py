from multipledispatch import dispatch

class Multiplication:

    # For two integer parameters
    @dispatch(int, int)
    def product(self, a, b):
        print("Product of two integers:", a * b)

    # For three integer parameters
    @dispatch(int, int, int)
    def product(self, a, b, c):
        print("Product of three integers:", a * b * c)

    # For two float parameters
    @dispatch(float, float)
    def product(self, a, b):
        print("Product of two floats:", a * b)


# Example usage
obj = Multiplication()

obj.product(2, 3)          # Calls the (int, int) version
obj.product(2, 3, 4)       # Calls the (int, int, int) version
obj.product(2.5, 4.0)      # Calls the (float, float) version
