class MyClass:
    def __init__(self, name):
        
        self.name = name

    def public_method(self):
        print("This is a public method.")
        self.__private_method()

    def __private_method(self):
        
        print(f"This is a private method. Hello, {self.name}!")


obj = MyClass("Alice")
obj.public_method()  


