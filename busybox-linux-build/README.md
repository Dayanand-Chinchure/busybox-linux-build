         ***Busybox and qemu to up the linux system***

----------------------------------------------------------------------------

What is Buysbox?

BusyBox: The Swiss Army Knife of Embedded Linux

BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides replacements for most of the utilities you
usually find in GNU fileutils, shellutils, etc. The utilities in BusyBox
generally have fewer options than their full-featured GNU cousins; however, the
options that are included provide the expected functionality and behave very
much like their GNU counterparts. BusyBox provides a fairly complete
environment for any small or embedded system.

BusyBox has been written with size-optimization and limited resources in mind.
It is also extremely modular so you can easily include or exclude commands (or
features) at compile time. This makes it easy to customize your embedded
systems. To create a working system, just add some device nodes in /dev, a few
configuration files in /etc, and a Linux kernel.

BusyBox is maintained by Denys Vlasenko, and licensed under the GNU GENERAL
PUBLIC LICENSE version 2.

----------------------------------------------------------------------------

On what hardware it run?

It will run on i386 and x86_64 machines.

----------------------------------------------------------------------------

Documentation:

There is a lot of documentation available both in electronic form on
the Internet and in books. Here are few links to go through.



----------------------------------------------------------------------------

Software requirements:

Compiling and running the busybox 1.* and 3.x kernels requires up-to-date 
versions of various software packages. To run the above scripts below 
software you must have installed in your linux machine, this are,

1. qemu
2. wget
3. gcc
4. python

----------------------------------------------------------------------------

Installtion procedure:

To install throught the script you have to run command :

  python install-busybox-qemu.py <url-file> <target-directory-name>


After installation to up the build linux machine you have to run the script
from yout <target-directory-name>.

  sh start.sh

----------------------------------------------------------------------------

Build directory for the busybox:

This directory will contain 

Tarball: 
	1 . busybox.*.*.tar.gz
	2 . linux-*.*.tar.gz

Directories:

	1. buysbox
	2. linux-kernel
	3. rootfs.img.gz
	4. start.sh

----------------------------------------------------------------------------

Configuring the busybox and linux kernel:

If you want to carry your existing configuration to a new version with minimal 
work, use "make oldconfig", which will only ask you for the answers to new 
questions.

- Alternative configuration commands are:

     "make config"      Plain text interface.

     "make menuconfig"  Text based color menus, radiolists & dialogs.

     "make nconfig"     Enhanced text based color menus.

     "make xconfig"     X windows (Qt) based configuration tool.

     "make gconfig"     X windows (Gtk) based configuration tool.

     "make oldconfig"   Default all questions based on the contents of
                        your existing ./.config file and asking about
                        new config symbols.

     "make silentoldconfig"
                        Like above, but avoids cluttering the screen
                        with questions already answered.
                        Additionally updates the dependencies.

     "make olddefconfig"
                        Like above, but sets new symbols to their default
                        values without prompting.

     "make defconfig"   Create a ./.config file by using the default
                        symbol values from either arch/$ARCH/defconfig
                        or arch/$ARCH/configs/${PLATFORM}_defconfig,
                        depending on the architecture.

--------------------------------------------------------------------------

If something goes wrong:

In case of any problem, *please* tell what kernel and busybox you are 
talking about, and what your setup is (use your common sense). If the 
problem is new, tell me so, and if the problem is old, please try to tell 
me when you first noticed it.

Mail-id : Dayanand Chinchure <dchinchure@gmail.com>

-------------------------------------------------------------------------
