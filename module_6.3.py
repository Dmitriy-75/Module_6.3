class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def run(self,dx):
        Horse.x_distance += self.dx
        return Horse.x_distance

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, dx,dy):
        self.dx = dx
        self.dy = dy

    def fly(self,dx):
        Eagle.y_distance += self.dy
        return Eagle.y_distance

class Pegasus(Horse,Eagle):
    def __init__(self, dx, dy):
        Horse.__init__(self, dx, dy)
        Eagle.__init__(self, dx, dy)

    def voice (self):
        print(Pegasus.sound)

    def move(self, dx, dy):
        return super().run(self.dx), super().fly(self.dy)


    def get_pos(self):
        return super().x_distance, super().y_distance


p1 = Pegasus(0,0)
print(p1.get_pos())


p1 = Pegasus(10,15)
p1.move(10, 15)
print(p1.get_pos())

p1 = Pegasus(-5,20)
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()