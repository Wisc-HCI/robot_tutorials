# Tutorial 1: Controlling Panda Bimanual Setup

## 1. Requirements
* If you are only running the simulation, you will need Docker Desktop or Docker Engine+Compose. Below are the instructions for each operating system:
    * 
* If you are running on the actual hardware, you will need additionally to setup your computer (`COMPUTER 1`) and the robots according to instructions in [instructions/bimanual_system_setup.md](../instructions/bimanual_system_setup.md). Note: this requires your computer be Ubuntu with a realtime kernel patch.

## 2. Setup
Make sure your terminal is in root of this repo (`robot_tutorials`).

First, pull in the submodules:
```bash
git submodule init
git submodule update
```

Next, build and start the docker container. This will take ~6 minutes and ~6.3GB of space.
```bash
docker compose -f docker/compose.bimanual.yaml build
docker compose -f docker/compose.bimanual.yaml run --rm bimanual-base
```

## 3. Test your setup in sim
Run the following to test your system in Mujoco. Then go to [http://localhost:7000](http://localhost:7000).
```bash
python3 -m  robot_motion_interface.examples.oscillating_ex --interface mujoco_browser
```

If you see the robot "dancing" in your browser, as shown below, your system is setup correctly. You are ready to move on to the next step. If you're curious what the script that runs this looks like, you can check it out at [libs/robot-stack/robot_motion_interface/src/robot_motion_interface/examples/oscillating_ex.py](../libs/robot-stack/robot_motion_interface/src/robot_motion_interface/examples/oscillating_ex.py).

<video src="assets/tutorial-1-system-check.mp4" controls></video>

## 4. Try writing code yourself

TODO