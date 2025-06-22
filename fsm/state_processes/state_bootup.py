# state_bootup.py



# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateBootup:
    def __init__(self, dp_obj):
        self.dp_obj = dp_obj
        self._running = False
    
    async def run(self):
        self._running = True
        while self._running:
            # TODO: do background tasks
            await asyncio.sleep(2)

    def stop(self):
        self._running = False