# fsm.py



# ++++++++++++++++++ Imports and Installs ++++++++++++++++++ #
import asyncio
from fsm.state_processes.state_comms import StateComms
from fsm.state_processes.state_deploy import StateDeploy
from fsm.state_processes.state_bootup import StateBootup
from fsm.state_processes.state_charge import StateCharge
from fsm.state_processes.state_orient import StateOrient
from fsm.state_processes.state_antennas import StateAntennas
from fsm.state_processes.state_detumble import StateDetumble


# ++++++++++++++++++++ Class Definition ++++++++++++++++++++ #
class FSM:
    def __init__(self, dp_obj):
        self.dp_obj = dp_obj    # object of type DataProcess
        self.state_objects = {
            "bootup"    : StateBootup(dp_obj),
            "detumble"  : StateDetumble(dp_obj),
            "charge"    : StateCharge(dp_obj),
            "antennas"  : StateAntennas(dp_obj),
            "comms"     : StateComms(dp_obj),
            "deploy"    : StateDeploy(dp_obj),
            "orient"    : StateOrient(dp_obj),
        }
        self.curr_state_name = "bootup"
        self.curr_state_object = self.state_objects["bootup"]
        self.curr_state_run_asyncio_task = None
        self.deployed_already = False
        self.checkpoint = False

    def set_state(self, new_state_name):
        """
        This function is called when we switch states from execute_fsm()
        """
        print(f"✅ {self.curr_state_name} complete → {new_state_name}")

        # Stop current state's background task
        if self.curr_state_run_asyncio_task is not None:
            self.curr_state_object.stop()
            self.curr_state_run_asyncio_task.cancel()
            self.curr_state_run_asyncio_task = None

        self.curr_state_name = new_state_name
        self.curr_state_object = self.state_objects[new_state_name]
        self.curr_state_run_asyncio_task = asyncio.create_task(self.curr_state_object.run())

    def execute_fsm_step(self):
        """
        This function runs a single execution of the finite state machine (fsm)
        It checks its current state and data points and sees if we 
        need to change state, take action, etc.
        Note: because we pass in db_obj, its data variable will update 
        automatically if any changes are made for that db_obj
        """
        
        # Emergency override: low battery
        if self.dp_obj.data["data_bp"] <= 20 and self.curr_state_name != "charge":
            self.set_state("charge")
            return

        # Startup → Detumble
        if self.curr_state_name == "bootup" and self.curr_state_object.is_done():
            self.set_state("detumble")
            return

        # Detumble → Charge
        if self.curr_state_name == "detumble" and self.dp_obj.data["data_imu_av_magnitude"] <= 0:
            self.set_state("charge")
            return

        # Charge → Antennas
        if self.curr_state_name == "charge" and self.dp_obj.data["data_bp"] >= 75:
            self.set_state("antennas")
            return

        # Antennas → Comms
        if self.curr_state_name == "antennas":
            if self.dp_obj.data["data_bp"] >= 50:
                self.checkpoint = True
            if self.checkpoint and all(val > 90 for val in self.dp_obj.data["imu_pos"]):
                self.checkpoint = False
                self.set_state("comms")
                return

        # Comms → Deploy or Orient
        if self.curr_state_name == "comms":
            if self.dp_obj.data["data_bp"] >= 50:
                self.checkpoint = True
            if self.checkpoint and self.dp_obj.data["data_imu_av_magnitude"] <= 1:
                self.checkpoint = False
                if not self.deployed_already:
                    self.deployed_already = True
                    self.set_state("deploy")
                else:
                    self.set_state("orient")
                return

        # Deploy → Orient
        if self.curr_state_name == "deploy" and self.curr_state_object.is_done() and self.dp_obj.data["data_bp"] >= 30:
            self.set_state("orient")
            return

        # Orient → Comms
        if self.curr_state_name == "orient":
            if all(val > 90 for val in self.dp_obj.data["imu_pos"]):
                self.set_state("comms")
                return
        
