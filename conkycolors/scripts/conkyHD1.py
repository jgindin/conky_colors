#!/usr/bin/env python2
import os

def printMountInfo( device, name ):
  print ("${voffset -4}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}"+name+": ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc "+device+"}% free${color}${font}\n")
  print ("${voffset -10}${color0}${fs_bar 4,20 "+device+"}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free "+device+"}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used "+device+"}${color}${font}\n")


# root filesystem
printMountInfo("/", "Root")

# various folders (if they're separate mount points)
if os.path.ismount("/boot"):
  printMountInfo( "/boot", "Boot")

if os.path.ismount("/home"):
  printMountInfo( "/home", "Home")

if os.path.ismount("/home2"):
  printMountInfo( "/home2", "Home2")

if os.path.ismount("/opt"):
  printMountInfo( "/opt", "Opt")

# folder in /media
for device in os.listdir("/media/"):
        if (not device.startswith("cdrom")) and (os.path.ismount('/media/'+device)):
          printMountInfo( "/media/"+device, device)
print ("${voffset -2}")



