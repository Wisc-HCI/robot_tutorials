import time
import threading
import argparse
from pathlib import Path

import numpy as np

from robot_motion_interface.interface import Interface
from robot_motion_interface.mujoco.mujoco_browser import MujocoBrowserInterface
from robot_motion_interface.bimanual_interface import BimanualInterface


def configure_interface(interface_str:str) -> Interface:
    """
    Configure the robot interface based on real or sim

    Args:
        interface_str (str): Either "sim" or "real" 
    Returns: 
        (Interface) The specific child interface (MujocoBrowserInterface, BimanualInterface)
    """

    config_dir = Path(__file__).resolve().parents[1] / "libs" / "robot-stack" / "robot_motion_interface" / "config"

    if (interface_str == "sim"):
        config_path = config_dir / "mujoco_config.yaml"
        interface = MujocoBrowserInterface.from_yaml(config_path)
        
    elif (interface_str == "real"):
        config_path = config_dir / "bimanual_arm_config.yaml"
        interface = BimanualInterface.from_yaml(config_path)

    else:
        raise ValueError(f"Unsupported interface: {interface_str}")
    
    return interface


def move_right_arm(robot_interface:Interface, cartesian_pose:np.ndarray):
    """
    This moves the robot at a set velocity.
    I defined this helper function to reduce code duplication.

    Args:
        robot_interface (Interface): The robot interface (sim or real).
        cartesian_pose (np.ndarray): Target pose [x, y, z, qx, qy, qz, qw] in meters/radian
    """
    goal_poses = [np.array(cartesian_pose)]
    trajectories, _ = robot_interface.cartesian_trajectory(
        goal_poses=goal_poses, dt=0.01, velocity=0.005, angular_velocity=0.005, 
        acceleration=0.005, ee_frames=["right_delto_offset_link"])
    
    for waypoint in trajectories[0]:
        robot_interface.set_cartesian_pose(x_list=[waypoint], 
            ee_frames=["right_delto_offset_link"], blocking=True)
    print("Finished executing waypoints.")


def main(interface_str:str):
    """
    One solution to picking up a block either in real
    or sim.

    Args:
        interface_str (str): Either "sim" or "real" 
    """
    
    robot_interface = configure_interface(interface_str)
    
    # Start the simulation/control loop
    robot_interface.start_loop()
    robot_interface.home(blocking=True)


    ########################################################
    #   This is just one solution, there are countless!
    #########################################################

    # 1. Move above the cube
    move_right_arm(robot_interface, np.array([0.1, 0.0, 1.3, 0.0, 1.0, 0.0, 0.0]))

    # 2. Move down to cube
    move_right_arm(robot_interface, np.array([0.1, 0.0,  1.0, 0.0, 1.0, 0.0, 0.0]))

    # 4. Move cube Left
    move_right_arm(robot_interface, np.array([-0.1, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]))

    # 5. Move Up
    move_right_arm(robot_interface, np.array([0.0, 0.0, 1.2, 0.0, 1.0, 0.0, 0.0]))
    


    ########################################################
    ########################################################
    

    # Continuously loop to keep sim up
    try: 
        while(True):
            time.sleep(0.1)
    except (KeyboardInterrupt):
        print("\nStopping Interface.")
    finally:
        robot_interface.stop_loop()  



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run joint oscillation demo for Panda or Isaacsim.")
    parser.add_argument("--interface", type=str, choices=["sim", "real"], required=True)

    args = parser.parse_args()
    main(args.interface)
