class Calculator:
    @staticmethod  # Static method: not dependent on class or instance, no need for self or cls
    def add(a, b):
        return a + b
    
    @staticmethod  # Static method, does not require self or cls
    def subtract(a, b):
        return a - b
    
    @staticmethod  # Static method, does not require self or cls
    def multiply(a, b):
        return a * b
    
    @staticmethod  # Static method, does not require self or cls; handles division by zero
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b


# Using the class directly without creating an instance
print(Calculator.add(1, 3))       # 4
print(Calculator.subtract(10, 4)) # 6
print(Calculator.multiply(2, 7))  # 14
print(Calculator.divide(8, 2))    # 4.0
print(Calculator.divide(5, 0))    # Error: Division by zero!
