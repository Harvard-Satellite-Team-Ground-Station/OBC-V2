# state_bootup.py



# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateBootup:
    def __init__(self, dp_obj):
        """
        Initialize the class object
        """
        self.dp_obj = dp_obj
        self._done = False
        self._running = False
    
    async def run(self):
        """
        Run the deployment sequence asynchronously
        """
        self._running = True
        # TODO: tasks
        await asyncio.sleep(10)
        self._done = True

    def stop(self):
        """
        Manually stop the run()
        """
        self._running = False

    def is_done(self):
        """
        Check if the run() completed on its own
        """
        return self._done