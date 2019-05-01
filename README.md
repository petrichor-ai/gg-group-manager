## AWS Greengrass-Group-Manager


### Installation:

```bash
$ pip install git+https://github.com/petrichor-ai/gg-group-manager.git
```

### Commands:

Create an AWS Greengrass Group,
```bash
$ gg-manager group create sample_group.json
```

Update an AWS Greengrass Group,
```bash
$ gg-manager group update sample_group.json
```

Deploy an AWS Greengrass Group,
```bash
$ gg-manager group deploy sample_group.json
```

Remove an AWS Greengrass Group,
```bash
$ gg-manager group remove sample_group.json
```


### Greengrass Core Setup (Raspberry Pi)

#### Requirements:

    - Raspberry Pi with integrated wifi chip - Pi 3
    - Compatible micro SD card - at least 8GB
    - Power source for the Raspberry Pi
    - A wifi access point you want to connect the Pi to


#### Prepare SD card with Raspbian Stretch Lite

Download Raspbian Stretch Lite,
```bash
$ wget https://downloads.raspberrypi.org/raspbian_lite_latest
```

Unzip Raspbian package,
```bash
$ unzip *-raspbian-stretch-lite.zip
```

Find MicroSD,
```bash
$ sudo diskutil list
```

Write image to MicroSD,
```bash
$ sudo diskutil eraseDisk FAT32 RASPBIAN MBRFormat /dev/diskn

$ sudo diskutil unmountDisk /dev/diskn

$ sudo dd bs=1m if=path_of_your_image.img of=/dev/rdiskn conv=sync
```

#### Configure ssh and wifi

```bash
$ cd /Volumes/boot
```

Enable ssh,
```bash
$ touch ssh
```

Connect wifi,
```bash
$ nano wpa_supplicant.conf
```

paste below to "wpa_supplicant.conf"
```txt
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="YOUR_SSID"
    psk="YOUR_WIFI_PASSWORD"
    key_mgmt=WPA-PSK
}
```


sudo wget -O root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem

