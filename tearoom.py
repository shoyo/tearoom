import sys
import random


class Teacup:
    """An individual teacup that occasionally contains a number.

    -- Further description. --
    """

    def __init__(self):
        """Initializes a teacup.

        value   -- current value (1-9) contained in the teacup. None if teacup
                   is empty.
        """
        self.value = None
        self._spawn_chance = random.uniform(.0025, .005)
        self._maturity_rate = random.randint(1, 10)
        self._timer = 1

    def update(self):
        if self.value is None:
            if self._should_spawn():
                self.value = 1
        else:
            if self._is_mature():
                if self.value == 9:
                    self.value = None
                    self._refresh()
                else:
                    self._increment_value()
                self._reset_timer()
            self._increment_timer()

    def _should_spawn(self):
        """Return True if teacup should start counting, False otherwise."""
        return random.random() < self._spawn_chance

    def _is_mature(self):
        """Return True if teacup is mature, False otherwise.

        Used to check if teacup value should be updated.
        """
        return self._timer >= self._maturity_rate

    def _reset_timer(self):
        """Reset the timer."""
        self._timer = 1

    def _increment_timer(self):
        """Increment the timer by 1."""
        self._timer += 1

    def _increment_value(self):
        """Increment value by 1."""
        self.value += 1

    def _refresh(self):
        """Refresh spawn chance and maturity rate."""
        self._spawn_chance = random.uniform(.005, .02)
        self._maturity_rate = random.randint(1, 10)


class Tearoom:
    """A collection of teacups.

    --Further description. --
    """

    def __init__(self, width):
        """Initializes a square tearoom and the contained teacups.

        Attributes:

        -- attribute descriptions. --
        """
        self.is_alive = True
        self.time_to_live = random.randint(1, sys.maxsize)
        self.width = width
        self.teacup_count = self.width * self.width
        self.teacups = []
        self._init_teacups()

    def _init_teacups(self):
        for i in range(self.teacup_count):
            teacup = Teacup()
            self.teacups.append(teacup)

    def update(self):
        if self.is_alive and self.time_to_live == 0:
            self.is_alive = False
            for teacup in self.teacups:
                teacup.value = None
        else:
            for teacup in self.teacups:
                teacup.update()
            self.time_to_live -= 1
