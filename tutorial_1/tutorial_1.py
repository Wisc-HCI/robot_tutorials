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
        config_path = config_dir / "bimanual_interface.yaml"
        interface = BimanualInterface.from_yaml(config_path)

    else:
        raise ValueError(f"Unsupported interface: {interface_str}")
    
    return interface


def main(interface_str:str):
    """
    Fill in the TODO's to try to move the block. Once you do it in sim,
    try running it on the real robot system.

    Args:
        interface_str (str): Either "sim" or "real" 
    """
    
    robot_interface = configure_interface(interface_str)
    
    # Start the simulation/control loop
    robot_interface.start_loop()
    robot_interface.home(blocking=True)


    ########################################################
    #                   TODO:
    #   Make your changes here to pick up the block!
    #   Try uncommenting out the below functions to see
    #   what they do and then adapt them to do what you want.
    #########################################################


    """Get current joint positions and velocities: [rads; velocities]"""
    # joint_state = robot_interface.joint_state()
    # print("JOINT STATE:", joint_state)

    """Get the ordered joint names"""
    # names = robot_interface.joint_names()
    # print("JOINT NAMES:", names)

    """Set joint positions by name (radians)"""
    # robot_interface.set_joint_positions(
    #     q=np.array([ 0.0, 0.0, 2.0, 0.2,
    #                 -1.0, 0.0, 2.0, 0.2,
    #                  1.0, 0.0, 2.0, 0.2]),
    #     joint_names=["right_F1M1", "right_F1M2", "right_F1M3", "right_F1M4", 
    #                  "right_F2M1", "right_F2M2", "right_F2M3", "right_F2M4", 
    #                  "right_F3M1", "right_F3M2", "right_F3M3", "right_F3M4"],
    #     blocking=True)

    """Get current Cartesian pose of end-effector(s): [x, y, z, qx, qy, qz, qw]"""
    # poses, frames = robot_interface.cartesian_pose()
    # print("FRAMES:", frames, "\nPOSES:", poses)

    """ Set Cartesian pose of end-effector(s) [x, y, z, qx, qy, qz, qw] in meters/radians"""
    # robot_interface.set_cartesian_pose(
    #     x_list=[np.array([-0.3, 0.2, 1.3, 1.0, 0.0, 0.0, 0.0])],
    #     ee_frames=["left_delto_offset_link"], blocking=True)

    """Generate a smooth Cartesian trajectory to a goal pose at a set velocity"""
    # goal_poses = [np.array([0.2, 0.2, 1.2, 0.0, 1.0, 0.0, 0.0])]
    # trajectories, frames = robot_interface.cartesian_trajectory(
    #     goal_poses=goal_poses, dt=0.01, velocity=0.1, angular_velocity=0.5, 
    #     acceleration=0.5, ee_frames=["right_delto_offset_link"])
    # for waypoint in trajectories[0]:
    #     robot_interface.set_cartesian_pose(x_list=[waypoint], 
    #         ee_frames=["right_delto_offset_link"], blocking=True)
    # print("Finished executing waypoints.")


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
