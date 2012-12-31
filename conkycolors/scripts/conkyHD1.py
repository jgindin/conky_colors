#!/usr/bin/env python2
import os

# root filesystem
print ("${voffset -2}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}Root: ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /}% free${color}${font}\n")
print ("${voffset -12}${color0}${fs_bar 4,20 /}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /}${color}${font}\n")

# various folders (if they're separate mount points)
if os.path.ismount("/boot"):
        print ("${voffset -12}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}Boot: ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /home}% free${color}${font}\n")
        print ("${voffset -12}${color0}${fs_bar 4,20 /home}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /boot}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /boot}${color}${font}\n")

if os.path.ismount("/home"):
        print ("${voffset -12}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}Home: ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /home}% free${color}${font}\n")
        print ("${voffset -12}${color0}${fs_bar 4,20 /home}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /home}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /home}${color}${font}\n")

if os.path.ismount("/home2"):
        print ("${voffset -12}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}Home2: ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /home2}% free${color}${font}\n")
        print ("${voffset -12}${color0}${fs_bar 4,20 /home2}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /home2}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /home2}${color}${font}\n")

if os.path.ismount("/opt"):
        print ("${voffset -12}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}Opt: ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /opt}% free${color}${font}\n")
        print ("${voffset -12}${color0}${fs_bar 4,20 /opt}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /opt}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /opt}${color}${font}\n")

# folder in /media
for device in os.listdir("/media/"):
        if (not device.startswith("cdrom")) and (os.path.ismount('/media/'+device)):
                print ("${voffset -12}${color0}${font Poky:size=15}y${font}${color}${offset 6}${voffset -7}"+device.capitalize()+": ${font Ubuntu:style=Bold:size=8}${color1}${fs_free_perc /media/"+device+"}% free${color}${font}\n")
                print ("${voffset -12}${color0}${fs_bar 4,20 /media/"+device+"}${color}${offset 8}${voffset -2}F: ${font Ubuntu:style=Bold:size=8}${color2}${fs_free /media/"+device+"}${color}${font} U: ${font Ubuntu:style=Bold:size=8}${color2}${fs_used /media/"+device+"}${color}${font}\n")
print ("${voffset -12}")

