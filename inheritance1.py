class animal():
    sound=""
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("{sound} i'm {name}, ! {sound}".format(name=self.name, sound=self.sound))


class piglet(animal):
    sound="oink"

hamlete=piglet("hemlete")
hamlete.speak()

