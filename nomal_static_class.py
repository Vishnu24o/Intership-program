class car:
    windows = 4
    door = 5
    color = 'red'

    def horn(self):      # (if we make functions in class then (self) is mendetory)
        print(self.door)
        print(self.windows)
        print('above are the properties of car')
obj = car()
print(obj.color)
obj.horn()
