#!/usr/bin/env bash

#
# 1 - the interface (e.g., ${iface})
# 2 - the type of the interface (e.g., 'Wireless')
function displayNetwork() {

  local iface=$1
  local iface_type=$2

	echo "\${color0}\${font Liberation Sans:style=Bold:size=14}${iface_type}\${color}\${font}"
	echo "\${color0}\${font ConkyColors:size=16}s\${font}\${color}\${goto 32}\${voffset 0}Up: \${font Liberation Sans:style=Bold:size=14}\${color1}\${upspeed ${iface}}\${color}\${font} \${alignr}\${color2}\${upspeedgraph ${iface} 8,60 E07A1F CE5C00}\${color}"
	echo "\${goto 32}Total: \${font Liberation Sans:style=Bold:size=14}\${color2}\${totalup ${iface}}\${color}\${font}"
	echo "\${voffset 2}\${color0}\${font ConkyColors:size=16}t\${font}\${color}\${goto 32}\${voffset 0}Down: \${font Liberation Sans:style=Bold:size=14}\${color1}\${downspeed ${iface}}\${color}\${font} \${alignr}\${color2}\${downspeedgraph ${iface} 8,60 E07A1F CE5C00}\${color}"
	echo "\${goto 32}Total: \${font Liberation Sans:style=Bold:size=14}\${color2}\${totaldown ${iface}}\${color}\${font}"

	if [ $iface_type == "Wireless" ]; then
	  echo "\${color0}\${font ConkyColors:size=16}j\${font}\${color}\${voffset 0}\${goto 32}Signal: \${font Liberation Sans:style=Bold:size=14}\${color1}\${wireless_link_qual_perc ${iface}}%\${color}\${font} \${alignr}\${color2}\${wireless_link_bar 8,60 ${iface}}\${color}"
	fi

	echo "\${voffset 2}\${color0}\${font ConkyColors:size=16}B\${font}\${color}\${goto 32}\${voffset 0}Local IP: \${alignr}\${color2}\${addr ${iface}}\${color}"

	DIR=$(conky-colors --finddir=bin/conkyIp)
	echo "\${goto 32}Public IP: \${alignr}\${color2}\${execi 10800 ${DIR}/bin/conkyIp}\${color}"
}



avail=`ifconfig -s | tail -n +2 | awk '{print \$1}'`
for iface in $avail; do
  type_prefix=${iface:0:1}
  if [ $type_prefix == 'w' ]; then
    displayNetwork $iface "Wireless"
  elif [ $type_prefix == 'e' ]; then
    displayNetwork $iface "Wired"
  elif [ $type_prefix == 'l' ]; then
    #skip this
    echo
  elif [ $type_prefix == 't' ]; then
    displayNetwork $iface "VPN"
  fi

done


