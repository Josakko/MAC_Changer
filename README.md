# MAC_Changer
Python script made for changing MAC address on linux machines

## Usage

To get interface name (witch is required to change MAC address) follow these steps:
1. Run `ifconfig` command in bash terminal, after you do so you should get output like shown on example down below.

<p align="center">
  <img alt="issue" src="https://github.com/Josakko/MAC_Changer/blob/main/screenshot.png?raw=true" width="650px">
</p>

In this example "eth0" an "lo" are interface names that you want to remember, one more example down below where there is only one interface.

        eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255
                inet6 fe80::a00:27ff:fe8f:15cb  prefixlen 64  scopeid 0x20<link>
                ether 08:00:27:8f:15:cb  txqueuelen 1000  (Ethernet)
                RX packets 0  bytes 0 (0.0 B)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 0  bytes 0 (0.0 B)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

2. Now once you now the name of the interface that you want to change MAC address run `main.sh` file that you downloaded from this repo.

## Need Help?

If you need help contact me on my [discord server](https://discord.gg/xgET5epJE6).

## Contributors

Big thanks to all of the amazing people (only me) who have helped by contributing to this project!
