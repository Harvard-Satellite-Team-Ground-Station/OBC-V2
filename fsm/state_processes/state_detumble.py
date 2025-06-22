# state_detumble.py


# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateDetumble:
    def __init__(self, shared_data):
        self.data = shared_data
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