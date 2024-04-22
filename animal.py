class Animal:
    def __init__(self):
        self.fnum_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")


animal = Animal()
nemo = Fish()
nemo.swim()

animals = [animal, nemo]

for i in animals:
    i.breathe()
