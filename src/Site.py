
class Site:

    def __init__(self, num_operations):
        self.location = []
        for i in range(num_operations):
            self.location.append(-1)

    def __str__(self):
        string = str(self.location)
        return string
