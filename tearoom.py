import sys
import random


class Teacup:
    """An individual teacup that occasionally contains a number.

    -- Further description. --
    """
    def __init__(self, increment_rate):
        """Initializes a teacup.

        Attributes:
        value - current number (1-9) contained in the teacup. None if teacup
                is empty.
        """
        self.value = None
        self.increment_rate = increment_rate
        self.timer = 0

    def update(self):
        if self.value is None:
            if random.random() < .1:
                self.value = 1
                self.timer = self.increment_rate
        else:
            if self.timer == self.increment_rate:
                if self.value == 9:
                    self.value = None
                    self.timer = 0
                else:
                    self.value += 1
            self.timer += 1


class Tearoom:
    """A collection of teacups.

    --Further description. --
    """
    def __init__(self, size):
        """Initializes a square tearoom.

        Attributes:

        -- attribute descriptions. --
        """
        self.time_to_live = random.randint(1, sys.maxsize)
        self.size = size
        self.max_size = self.size * self.size
        self.teacups = []
        self.init_teacups()

    def init_teacups(self):
        for i in range(self.max_size):
            teacup = Teacup(random.randint(1, sys.maxsize))
            self.teacups.append(teacup)

    def update(self):
        for teacup in self.teacups:
            teacup.update()
