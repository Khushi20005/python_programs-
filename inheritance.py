class fruit:
    def __init__(self,color,flavour):
        self.color=color
        self.flavour=flavour

class apple(fruit):
    pass

class grapes(fruit):
    pass

granny_smith= apple("green","tart")
print(granny_smith.flavour)
print(granny_smith.color)