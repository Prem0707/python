class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def rest(self):
        self.x = 0
        self.y = 0

a = Point(1, 1)
b = Point()

print(a.x, a.y)
print(b.x, b.y)