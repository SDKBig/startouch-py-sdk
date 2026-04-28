> 后来lft应该更新了几版 在https://github.com/StarTouch-dhu/startouch-v1 之后有用到可看

## CAN连接
sudo ip link set can0 up type can bitrate 1000000

ip link show can0

## 编译（注意，编译和运行时的python版本要对应）
conda create -n startouch python=3.10

conda activate startouch

<!-- sudo apt-get install pybind11-dev -->

mkdir build

cd build

cmake .. -DCMAKE_BUILD_TYPE=Release

make -j&(nproc)

## test运行

cd interface_py

python test0825fasttest
