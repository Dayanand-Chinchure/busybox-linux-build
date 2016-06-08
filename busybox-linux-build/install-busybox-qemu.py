#!/usr/bin/env python
import sys
import subprocess

#Variable Declaration
#-----------------------------------------------------------------------------------------------
COUNT_PARAM             = len(sys.argv)
BUSYBOX_VERSION         = "busybox-1.24.2"
BUSYBOX_EXTENSION       = ".tar.bz2"
KERNEL_VERSION          = "linux-3.18.25"
KERNEL_EXTENSION        = ".tar.gz"
TAR_COMMAND             = "tar -xvf"
CONFIG_FILES_DIRECTORY  = "config-files"
BUSYBOX_CONFIG          = "busybox-config"
KERNEL_CONFIG           = "kernel-config"
SLASH                   = "/"
#-------------------------------------------------------------------------------------------------

#Checking Parameters
#-------------------------------------------------------------------------------------------------
if COUNT_PARAM == 1:
        sys.exit("URL file is missing (containing url of busybox and linux kernel)")
if COUNT_PARAM == 2:
        sys.exit("Downloading directory is missing. Mention path to store downloaded files")
        
FILE = sys.argv[1]
DOWNLOAD_DIRECTORY_NAME=sys.argv[2]
#---------------------------------------------------------------------------------------------------    

#Downloading the neccesary files
#---------------------------------------------------------------------------------------------------
subprocess.call("echo Creating directory to download and store all necessary file ... ",shell=True)
subprocess.call("mkdir " + DOWNLOAD_DIRECTORY_NAME ,shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME,shell=True)
subprocess.call("echo Downloading the necessary file ...",shell=True)

URLFILE=open(FILE,"r")

for link in URLFILE:
        subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME + " ; " + "wget -c "+ link,shell=True)


subprocess.call("echo Download completed,Lets start the action ...",shell=True)
#-----------------------------------------------------------------------------------------------------

# Configure Busybox
#-----------------------------------------------------------------------------------------------------
subprocess.call("echo Let's configure and build the busybox ...",shell=True)
subprocess.call("cd "+ DOWNLOAD_DIRECTORY_NAME + " ;" + TAR_COMMAND+BUSYBOX_VERSION+BUSYBOX_EXTENSION,shell=True)
subprocess.call("cp "+ CONFIG_FILES_DIRECTORY+SLASH+BUSYBOX_CONFIG + " " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH,shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH +" ;" + "mv "+ BUSYBOX_CONFIG + " " + ".config",shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH +" ;" + "make oldconfig" + " ;" +" make" + " ; " + "make install",shell=True)
#-----------------------------------------------------------------------------------------------------

#Configure Linux Kernel
#-----------------------------------------------------------------------------------------------------
subprocess.call("echo Let's configure and build the linux kernel ...",shell=True)
subprocess.call("cd "+ DOWNLOAD_DIRECTORY_NAME + " ;" + TAR_COMMAND+KERNEL_VERSION+KERNEL_EXTENSION,shell=True) 
subprocess.call("cp "+ CONFIG_FILES_DIRECTORY+SLASH+KERNEL_CONFIG + " " + DOWNLOAD_DIRECTORY_NAME+SLASH+KERNEL_VERSION+SLASH,shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+KERNEL_VERSION+SLASH +" ;" + "mv "+ KERNEL_CONFIG + " " + ".config",shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+KERNEL_VERSION+SLASH +" ;" + "make oldconfig" + " ; " + "make",shell=True)
#---------------------------------------------------------------------------------------------------

#Create a file system directories in busybox source
#---------------------------------------------------------------------------------------------------
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH + "_install" + " ;" + "mkdir -p proc sys dev etc etc/init.d",shell=True)
#---------------------------------------------------------------------------------------------------

#Adding bash script to mount some devices automatically after the boot.
#---------------------------------------------------------------------------------------------------
subprocess.call("cp "+CONFIG_FILES_DIRECTORY+SLASH+"rcS" + " " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH+"_install/etc/init.d/",shell=True)
subprocess.call("chmod +x " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH + "_install/etc/init.d/rcS",shell=True)
#---------------------------------------------------------------------------------------------------

#Compressing the rootfs.img file
#---------------------------------------------------------------------------------------------------
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH + "_install/" + " ; " + "find . | cpio -o --format=newc > ../rootfs.img",shell=True)
subprocess.call("cd " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH + " ; " + " gzip -c rootfs.img > rootfs.img.gz",shell=True)
subprocess.call("cp " + DOWNLOAD_DIRECTORY_NAME+SLASH+BUSYBOX_VERSION+SLASH+"rootfs.img.gz" + " " + DOWNLOAD_DIRECTORY_NAME+SLASH ,shell=True)
#---------------------------------------------------------------------------------------------------

#Final Step
#---------------------------------------------------------------------------------------------------
subprocess.call("cp " + CONFIG_FILES_DIRECTORY+SLASH+"start.sh" + " " + DOWNLOAD_DIRECTORY_NAME+SLASH ,shell=True)
subprocess.call("echo Your rootfs and kernel bzImage is ready",shell=True)
subprocess.call("echo Now run the script './start.sh' from "+ DOWNLOAD_DIRECTORY_NAME,shell=True)
#---------------------------------------------------------------------------------------------------
