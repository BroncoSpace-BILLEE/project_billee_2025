import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sam/Documents/code/project_billee_2025/ros2_ws/install/manual_movement'
