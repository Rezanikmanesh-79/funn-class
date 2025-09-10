class Rectangle:
    def __init__(self, height, width):
        # Using double underscores to make attributes private
        # so they cannot be modified directly from outside.
        self.__height = height
        self.__width = width

    @property
    def height(self):
        # With @property, we control how the attribute is accessed.
        # Here, we simply return the stored value.
        return self.__height

    @height.setter
    def height(self, value):
        # The setter lets us validate the input before assigning it.
        # Without a setter, anyone could assign a negative value directly.
        if value < 0:
            raise ValueError("Height cannot be negative")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self.__width = value

    @property
    def area(self):
        # area is a computed property.
        # Without @property, we'd have to call it like rect.area().
        # With @property, we can use it like a simple attribute: rect.area
        return self.__height * self.__width


# Example usage
rect = Rectangle(5, 10)
print(rect.area)   # looks like a simple attribute, but it's computed internally

rect.height = 7    # setter validates the input
print(rect.area)

# rect.width = -3  # this will raise ValueError thanks to the setter
