from project.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return super(Elf, self).__repr__()
