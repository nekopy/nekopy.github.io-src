Title: Automatic Driver Building with DKMS
Date: 2017-03-03 22:22
Modified: 2017-03-04 01:51
Category: linux
Tags: DKMS, linux, kernel modules, Fedora
Slug: dkms
Authors: neko.py
Summary: Quick intro to setting up DKMS for from-source kernel modules.

Moving to Fedora on my laptop has been a perpetual learning experience. About half a year ago my Windows install died and I wound up getting so mad I left for Fedora. 

```
           /:-------------:\          neko@catbox
        :-------------------::        OS: Fedora 25 TwentyFive
      :-----------/shhOHbmp---:\      Kernel: x86_64 Linux 4.9.12-200.fc25.x86_64
    /-----------omMMMNNNMMD  ---:     Uptime: 3h 49m
   :-----------sMMMMNMNMP.    ---:    Packages: 2423
  :-----------:MMMdP-------    ---\   Shell: zsh 5.2
 ,------------:MMMd--------    ---:   Resolution: 3600x1080
 :------------:MMMd-------    .---:   WM: i3
 :----    oNMMMMMMMMMNho     .----:   CPU: Intel Core i7-4800MQ CPU @ 3.7GHz
 :--     .+shhhMMMmhhy++   .------/   GPU: Gallium 0.4 on NVE6
 :-    -------:MMMd--------------:    RAM: 1529MiB / 15970MiB
 :-   --------/MMMd-------------;    
 :-    ------/hMMMy------------:     
 :-- :dMNdhhdNMMNo------------;      
 :---:sdNMMMMNds:------------:       
 :------:://:-------------::         
 :---------------------://           

```

Since then I've never looked back. I'm set up to dual-boot with windows, so I still have my games if need be. However one of the biggest issues I had was the incompatiblity of my internal wireless card with available drivers. Instead, I wound up buying myself a usb wireless adapter, which is a pretty mean motherfucker, but it needed me to build the kernel module from source. 

With fedora I get very frequent updates to my kernel, however, and this means very frequently I'll boot up and have no internet, because lo and behold, the kernel updated and I need to rebuild my driver. Oh and it doesnt play nice with NetworkManager either. I had to get down and dirty with nm-cli, but that's a story for another day.

So today I finally sucked it up and learned how to use DKMS. What DKMS will do (and I always confuse it with DPKG) is automatically rebuild your kernel modules from source when the kernel upgrades.

Setting it up was extremely simple. I followed a simple tutorial, with only slight modifications.

First off, copy your kernel source to a new folder under /usr/src

```bash
su
mkdir /usr/src/rtl8814AU-4.3.21
cp -R ~/rtl8814AU/* /usr/src/rtl8814AU-4.3.21
```

Where the folder you make is in $(module-name)-$(module-version) format. Then we're gonna add a dkms.conf file at the top level of that folder, and fill it with the appropriate content:

```ini
PACKAGE_NAME="rtl8814AU"
PACKAGE_VERSION="4.3.21"
BUILT_MODULE_NAME[0]="8814au"
DEST_MODULE_LOCATION[0]="/kernel/drivers/net/wireless/"
MAKE[0]="make -j12"
AUTOINSTALL="yes"
```

Probably the most interesting thing going on here is the value of the MAKE[0] key. This is the command that's gonna be called when DKMS enters your module directory to build up your stuff. In my case, the makefile already has everything it needs to build itself. (Except for two lines being backwards which broke DKMS building... in an 1800 line Makefile... took hours to isolate and fix). By default, DKMS will want to build your project with as many jobs as you have cores. Obviously, I know better than the DKMS authors, and the magic job number is 1.5 times the number of cores you have. In my case, that gives us -j12.

Once all that's set, just add that sucker to DKMS with

```bash
dkms add -m rtl8814AU -v 4.3.21
```

and test building...

```bash
dkms build -m rtl8814AU -v 4.3.21
dkms status
```

It's about 2am now. Hopefully next time my kernel builds i wont be totally boned. I'll have to post here to update if I am.
