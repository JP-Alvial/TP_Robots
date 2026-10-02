import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/j4ck/0Clases/TP_Robots/ros2_ej/install/turtlesim_ctr'
