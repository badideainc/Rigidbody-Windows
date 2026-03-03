class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def Distance(v1, v2):
        return ((v1.x - v2.x)**2 + (v1.y - v2.y)**2)**0.5