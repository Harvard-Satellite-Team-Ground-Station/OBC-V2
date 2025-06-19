# ///////////////////////////////////////////////////////////////// #
# DATA: BATERY SUBSYSTEM
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

    # DATA: battery percentage
    # keep the battery voltage between 3.5 and 4.1 volts to max li-ion lifespan
    # units: mV
    # output: [DATA_BATTERY_BP]
    v_bat = random.randint(35000, 41000)
    # Not an ideal measurement as discharge curves are nonlinear, we should track current
    battery_percentage = 100 * (v_bat - 35000)/6000 
    # TODO: delete line below, which is just for testing
    battery_percentage = random.randint(0,100)

    output_part1 = "[DATA_BATTERY_BP]"
    padding_length = DATA_OUTPUT_PADDING - len(output_part1)
    padding = " " * padding_length
    output = output_part1 + padding + "[" + str(battery_percentage) + "]"
    print(output, flush=True)

    # DATA: ...
    # description/notes
    # units
    # output: [DATA_BATTERY_...]
    
    # DATA: ...
    # description/notes
    # units
    # output: [DATA_BATTERY_...]

    