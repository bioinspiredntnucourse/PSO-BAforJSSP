from Site import Site

class Bee:

    def __init__(self, num_operations, scout_bee = False):
        self.scout_bee = scout_bee
        self.site = Site(num_operations)

    def __str__(self):
        string = 'Scout bee: {}'.format(self.scout_bee) + '\n'
        string += str(self.site.__str__())
        return string

    def set_site(site):
        if len(site) == len(self.site):
            self.site = site
        else:
            print("Error: Invalid site lenght")
