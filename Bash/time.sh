#!/bin/bash
timenow=$(date "+%T")
datetoday=$(date +"%m-%d-%y")
timezone=$(date +"%Z")
echo -n "The date is: "
# sleep 1
# banner also displays text
# figlet command also displays text
echo "$line"
toilet $datetoday
# sleep 1
echo "$line"
echo -n "The time is: "
# sleep 1
echo "$line"
toilet $timenow
# sleep 1
echo "$line"
echo -n "The time zone is: "
echo "$line"
toilet $timezone
echo "$line"
