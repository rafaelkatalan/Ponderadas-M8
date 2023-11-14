import subprocess
import os


cmd = "ros2 run turtlebot3_teleop teleop_keyboard"

terminal =subprocess.Popen(["xterm", "-e", f"{cmd} 2>&1"], stderr=subprocess.STDOUT)

terminal.wait()