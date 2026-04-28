from startouchclass import SingleArm
import time
# 创建机械臂连接  连接接口为"can0"
arm_controller = SingleArm(can_interface_ = "can0")

try:
    while True:
        arm_controller.gravity_compensation()
except KeyboardInterrupt:
    print("\n程序被用户中断")
finally:
    arm_controller.cleanup()

