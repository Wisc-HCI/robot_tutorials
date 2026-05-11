# Tutorial 1: Controlling Panda Bimanual Setup

## 1. Requirements

## 2. Setup
Make sure your terminal is in this directory (`robot_tutorials`).

First, pull in the submodules:
```bash
git submodule init
git submodule update
```

Next, build and start the docker container. This will take ~6 minutes and ~6.3GB of space.
```bash
docker compose -f docker/compose.mujoco.yaml build
docker compose -f docker/compose.mujoco.yaml run --rm mujoco-base
```

## 3. Test your setup in sim
Run the following to test your system in Mujoco. Then go to [http://localhost:7000](http://localhost:7000).
```bash
python3 -m  robot_motion_interface.examples.oscillating_ex --interface mujoco_browser
```

If you see the robot "dancing", as shown below, your system is setup correctly. You are ready to move on to the next step. If you're curious what the script that runs this looks like, you can check it out at <TODO>.

