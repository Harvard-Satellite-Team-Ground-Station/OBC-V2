# state_deploy.py



# ++++++++++++++ Imports/Installs ++++++++++++++ #
import asyncio
from lib.pysquared.protos.burnwire import BurnwireProto



# ++++++++++++++ Functions: Helper ++++++++++++++ #
class StateDeploy:
    def __init__(self, dp_obj):
        """
        Initialize the class object
        """
        self.dp_obj = dp_obj
        self.protos_burnwire = BurnwireProto()
        self._done = False
        self._running = False
    
    async def run(self):
        """
        Run the deployment sequence asynchronously
        """
        # Step 0: set correct parameters
        self._running = True
        burn_duration = 10
        # Step 1: burn the wire to deploy the antenna
        self.protos_burnwire.burn(timeout_duration=burn_duration)
        await asyncio.sleep(burn_duration)
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