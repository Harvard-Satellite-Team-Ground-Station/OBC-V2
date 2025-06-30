# state_comms.py



# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateComms:
    def __init__(self, dp_obj, logger):
        self.dp_obj = dp_obj
        self.logger = logger
        self.running = False
        self.done = True
    
    async def run(self):
        self._running = True
        while self._running:
            await asyncio.sleep(2)
            # Step 1: if we need to orient, orient
            # Step 2: create custom data to send to the beacon()  
            # This should differ than what is normally send in main() loop         

    def stop(self):
        """
        Used by FSM to manually stop run()
        """
        self.running = False

    def is_done(self):
        """
        Checked by FSM to see if the run() completed on its own
        If it did complete, it shuts down the async task run()
        """
        return self.done