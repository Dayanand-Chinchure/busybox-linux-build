#                      ** Start script for busybox build linux **
#-----------------------------------------------------------------------------------------
# Few details about the script content :
# 1. bzImage            : kernel image
# 2. rootfs.img.gz      : our file system
# 3. root=/dev/ram      : our root, normally root is '/'
# 4  rdinit=/sbin/init  : using our init which is symbolic link to /lib/systemd/systemd
#-------------------------------------------------------------------------------------------

qemu-system-i386 -kernel linux-3.18.25/arch/x86/boot/bzImage -initrd rootfs.img.gz -append "root=/dev/ram rdinit=/sbin/init"
