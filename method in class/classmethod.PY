class Person:
    # Class variable shared across all instances
    instances = 0  
    
    def __init__(self, name):
        self.name = name
        # Each time a new Person object is created, increment the counter
        Person.instances += 1

    @classmethod
    def get_count(cls):
        """
        A class method:
        - Takes 'cls' (the class itself) as the first argument instead of 'self' (the instance).
        - Can access or modify class variables (like 'instances').
        - Does not require creating an object first (you can call it directly from the class).
        """
        return cls.instances


# Create two Person objects
p1 = Person("Reza")
p2 = Person("Ali")

# Call the class method directly from the class (no object needed)
print(Person.get_count())  # Output: 2
