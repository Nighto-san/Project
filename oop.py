class Point:
    color = 'red'
    circle = 2
    def __init__(self, x=0, y=0):
        print("вызов инициализации")
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs):
        print('щас создадим обьект')
        return super().__new__(cls)
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        return self.x, self.y

    def __del__(self):
        print("вызов деструктора")


pt = Point(15,14)

print(pt.__dict__)