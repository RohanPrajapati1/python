class Outer:
    def __init__(self):
        self.name = "Outer"
    
    class Inner:
        def __init__(self):
            self.name = "Inner"
        def display(self):
            print("Hello from inner class")


# accessing inner class from outer class
# outer class object 
outer = Outer()
# inner class object
inner = outer.Inner()
inner.display()