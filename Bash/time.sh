#!/bin/bash

timenow=$(date "+%T")
datetoday=$(date +"%m-%d-%y")
timezone=$(date +"%Z")

echo -n "The date is: "
sleep 1

#banner also displays text
#figlet command also displays text

toilet $datetoday
sleep 1

echo -n "The time is: "
sleep 1

toilet $timenow
sleep 1

echo -n "The time zone is: "

toilet $timezone

exit
