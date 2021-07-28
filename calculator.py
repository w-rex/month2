class Plus:
    def add(self, *args):
        return sum(args)

class Min:
    def sub(self, a, b):
        self.a = a
        self.b = b
        return a -b

class Del:
    def div(self, a, b):
        self.a = a
        self.b = b
        return a / b


class Umn:
    def mult(self, a, b):
        self.a = a
        self.b = b
        return a * b