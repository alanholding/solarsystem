"""
2021-09-02
Rainfall triggers.

Sol ports output mapping:
- CV A: Not used in this script (yet!).
- CV B: Not used in this script (yet!).
- CV C: Not used in this script (yet!).
- CV D: Not used in this script (yet!).
- Gate 1: Might send a trigger every sixteenth note.
- Gate 2: Might send a trigger every sixteenth note.
- Gate 3: Might send a trigger every sixteenth note.
- Gate 4: Might send a trigger every sixteenth note.
"""

import winterbloom_sol as sol

from random import random

# Helper to create a random integer from 0 to maximum_random_countdown_value.
def new_random_countdown_value():
    return int(random() * maximum_random_countdown_value)

# Maximum random countdown value.
# @todo: Change to per trigger value.
# @todo: Value set by MIDI CC message.
maximum_random_countdown_value = 10

# Create and initialise the four countdowns.
countdowns = [new_random_countdown_value(), new_random_countdown_value(), new_random_countdown_value(), new_random_countdown_value()]

def loop(last, state, outputs):

    # Every sixteenth clock tick…
    if sol.should_trigger_clock(state, 16):

        # Loop through the four countdown values.
        # Decrement each countdown by one.
        # If a countdown value is less than zero, send a trigger to its associated output and set a new random countdown value.
        for idx, c in enumerate(countdowns):

            # Decrement this countdown's value by one.
            countdowns[idx] = countdowns[idx] - 1

            # Check if this countdown's value is less than zero.
            if countdowns[idx] < 0:
                # This countdown's value is less than zero so trigger its associated output. Note that we have to increase the idx (index) value by 1 as indexing in the outputs.trigger_gate() method starts at 1, not 0.
                outputs.trigger_gate(idx + 1)

                # Set a new random value for this countdown.
                countdowns[idx] = new_max()

# Ready let's go.
sol.run(loop)
