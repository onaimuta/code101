import subprocess, platform, re
from colorama import init, Fore

init()
def list_open_networks():
   # Get the name of the operating system.
   os_name = platform.system()
   # Check if the OS is Windows.
   if os_name == "Windows":
       # Command to list Wi-Fi networks on Windows.
       list_networks_command = 'netsh wlan show networks'
       try:
           # Execute the command and capture the output.
           output = subprocess.check_output(list_networks_command, shell=True, text=True)
           networks = []
           # Parse the output to find open Wi-Fi networks.
           for line in output.splitlines():
               if "SSID" in line:
                   # Extract the SSID (Wi-Fi network name).
                   ssid = line.split(":")[1].strip()
               elif "Authentication" in line and "Open" in line:
                   # Check if the Wi-Fi network has open authentication.
                   networks.append(ssid)
           # Check if any open networks were found.
           if len(networks) > 0:
               # Print a message for open networks with colored output.
               print(f'{Fore.LIGHTMAGENTA_EX}[+] Open Wifi networks in range: \n')
               for each_network in networks:
                   print(f"{Fore.GREEN}[+] {each_network}")
           else:
               # Print a message if no open networks were found.
               print(f"{Fore.RED}[-] No open wifi networks in range")
       except subprocess.CalledProcessError as e:
           # Handle any errors that occur during the execution of the command.
           print(f"{Fore.RED}Error: {e}")
           # Return an empty list to indicate that no networks were found.
           return []
    # else:
    #    print(f"{Fore.RED}Unsupported operating system.")
    #    return []

# Call the function.
list_open_networks()