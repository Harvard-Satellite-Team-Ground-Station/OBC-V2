# ///////////////////////////////////////////////////////////////// #
# DATA: STAR TRACKER SUBSYSTEM
# ///////////////////////////////////////////////////////////////// #


# IMPORTS
import time
import random
from config import DATA_OUTPUT_PADDING


# SETUP CONNECTIONS
# ...


# PRINT DATA
while True:
    # Interval to run measurements on
    time.sleep(1) 

    # DATA: position
    # we should keep the battery voltage between 3.5 and 4.1 volts if possible to maximize the lifespan of our li-ions
    # units: x, y, z
    # output: [DATA_STARTRACKER_POS]
    # TODO: delete line below, which is just for testing
    startracker_position = [random.randint(90,100), random.randint(90,100), random.randint(90,100)]

    output_part1 = "[DATA_STARTRACKER_POS]"
    padding_length = DATA_OUTPUT_PADDING - len(output_part1)
    padding = " " * padding_length
    output = output_part1 + padding + str(startracker_position)
    print(output, flush=True)


    # DATA: ...
    # description/notes
    # units
    # output: [DATA_STARTRACKER_...]

    
    # DATA: ...
    # description/notes
    # units
    # output: [DATA_STARTRACKER_...]
