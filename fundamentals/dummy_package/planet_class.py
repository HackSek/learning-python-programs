class Planet:

    shape = 'sphere'

    def __init__(self, name, radius, gravity, system):

        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def define_shape(cls):
        return f'All planets share the fact of having a {cls.shape}-like shape due to gravity'

    @staticmethod
    def define_speed(speed = 'a very high speet'):
        return f'The planet spins at a speed of {speed}'
