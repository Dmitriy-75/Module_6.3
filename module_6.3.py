class Horse():

    def __init__(self):
        self.sound = 'Frrr'
        self.x_distance = 0
        # super().__init__(y_distance)
        # super().__init__(sound)
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle():

    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        return super().run(dx), super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


