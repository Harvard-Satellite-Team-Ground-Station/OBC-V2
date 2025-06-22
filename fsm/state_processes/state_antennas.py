# state_antennas.py


# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateAntennas:
    def __init__(self, data):
        self.data = data
        self._running = False

    def update(self):
        """
        This function gets executed each time the FSM is called 
        """
        pass
    
    async def run(self):
        self._running = True
        while self._running:
            # TODO: do background tasks
            await asyncio.sleep(2)

    def stop(self):
        self._running = False