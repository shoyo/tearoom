import sys
import random


class Teacup:
    """An individual teacup that occasionally contains a number.

    A Teacup can do one of two things: be empty, or be counting up from 1 to 9.
    Every Teacup starts by being empty. Whether a Teacup starts counting and
    the pace at which it counts is determined by random chance. After a Teacup
    reaches 9, it becomes empty once again and restarts the cycle.
    """

    def __init__(self):
        """Create an empty teacup.

        value         -- current value contained in Teacup (1 - 9 or None)
        spawn_chance  -- probability that empty Teacup will begin counting
        maturity_rate -- pace at which a Teacup containing a number counts up.
        timer         -- keeps track of time elapsed. Compared with
                         maturity_rate to determine whether to increment value.
        """
        self.value = None
        self._spawn_chance = random.uniform(.0025, .005)
        self._maturity_rate = random.randint(1, 10)
        self._timer = 1

    def update(self):
        """Update the value contained in teacup.

        If the Teacup is empty, it can spawn a 1 according to its spawn chance
        to begin counting. If the Teacup contains a 9, it resets each
        attribute. Otherwise, it increments its value if the timer has matured.
        Note that a Teacup's spawn chance and maturity rate is refreshed each
        time the Teacup resets.
        """
        if self._is_empty():
            if self._should_spawn():
                self.value = 1
        else:
            if self._is_mature():
                if self.value == 9:
                    self._reset()
                else:
                    self._increment_value()
                    self._reset_timer()
            self._increment_timer()

    def _is_empty(self):
        """Return True if teacup is empty, False otherwise."""
        return self.value is None

    def _should_spawn(self):
        """Return True if teacup should start counting, False otherwise."""
        return random.random() < self._spawn_chance

    def _is_mature(self):
        """Return True if teacup is mature, False otherwise.

        Used to check if teacup value should be incremented.
        """
        return self._timer >= self._maturity_rate

    def _reset_timer(self):
        """Reset timer."""
        self._timer = 1

    def _increment_timer(self):
        """Increment timer by 1."""
        self._timer += 1

    def _increment_value(self):
        """Increment value by 1."""
        self.value += 1

    def _reset(self):
        """Reset Teacup by emptying and refreshing parameters."""
        self.value = None
        self._reset_timer()
        self._refresh()

    def _refresh(self):
        """Refresh spawn chance and maturity rate."""
        self._spawn_chance = random.uniform(.0025, .005)
        self._maturity_rate = random.randint(1, 10)


class Tearoom:
    """A collection of teacups.

    A Tearoom contains a square grid of Teacups. Each contained Teacup behaves
    completely independently. A Tearoom has a lifespan which is determined
    randomly when constructed. After a Tearoom "dies", each contained Teacup
    becomes empty and indefinitely stops counting.
    """

    def __init__(self, width):
        """Create a square Tearoom.

        is_alive     -- True if Tearoom is alive
        time_to_live -- number of time steps until Tearoom dies
        width        -- width of square Tearoom
        teacup_count -- total number of Teacups in Tearoom
        teacups      -- list of contained Teacups
        """
        self.is_alive = True
        self.time_to_live = random.randint(1, sys.maxsize)
        self.width = width
        self.teacup_count = self.width * self.width
        self.teacups = []
        self._init_teacups()

    def _init_teacups(self):
        """Initialize Teacups."""
        for i in range(self.teacup_count):
            teacup = Teacup()
            self.teacups.append(teacup)

    def update(self):
        """Update Tearoom and its contained Teacups.

        If the Tearoom is alive, each contained Teacup is updated. Kills
        Tearoom if time_to_live is 0."""
        if self.is_alive:
            if self.time_to_live == 0:
                self.is_alive = False
                for teacup in self.teacups:
                    teacup.value = None
            else:
                for teacup in self.teacups:
                    teacup.update()
                self.time_to_live -= 1
