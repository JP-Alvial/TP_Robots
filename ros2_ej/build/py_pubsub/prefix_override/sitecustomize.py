import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jack/Clases/TP_Robots/ros2_ej/install/py_pubsub'
