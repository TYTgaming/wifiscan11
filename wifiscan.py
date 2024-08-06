import subprocess
import re
import sys
 
print('''\033[1;32;40m \n
      

           (    (     (         (                      )  
 (  (      )\ ) )\ )  )\ )      )\ )   (     (      ( /(  
 )\))(   '(()/((()/( (()/(     (()/(   )\    )\     )\()) 
((_)()\ )  /(_))/(_)) /(_))___  /(_))(((_)((((_)(  ((_)\  
_(())\_)()(_)) (_))_|(_)) |___|(_))  )\___ )\ _ )\  _((_) 
\ \((_)/ /|_ _|| |_  |_ _|     / __|((/ __|(_)_\(_)| \| | 
 \ \/\/ /  | | | __|  | |      \__ \ | (__  / _ \  | .` | 
  \_/\_/  |___||_|   |___|     |___/  \___|/_/ \_\ |_|\_| 
                                                          
                                 *V0.1*

BY Henry Nguyễn
      FB: Henry Nguyễn                    ENJOY IT :D
''')
 
def scan_wifi_networks():
   """Scan for available Wi-Fi networks."""
   try:
       print("Đang quét tìm kiếm WI-FI gần nhất..")
       if sys.platform.startswith('win'):
           result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
       elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
           result = subprocess.check_output(['iwlist', 'scan'])
       else:
           print("Unsupported platform")
           return
 
 
       return result.decode('utf-8')
   except subprocess.CalledProcessError as e:
       print(f"Error: Unable to scan Wi-Fi networks. {e}")
       return None
   except Exception as e:
       print(f"Error: {e}")
       return None
 
 
def analyze_network_security(ssid, encryption_type):
   """Analyze the security of a Wi-Fi network."""
   try:
       print(f"Analyzing security for network: {ssid}")
       # Check if encryption type is weak or vulnerable
       if encryption_type.lower() in ['wep', 'wpa', 'tkip']:
           print("Warning: Weak encryption type detected.")
           print("Advice: Consider upgrading to WPA2 or WPA3 for stronger security.")
       else:
           print("FUCK YOUR NETWORK")
           print("FUCK YOUR NETWORK")
       # You can add more checks for specific vulnerabilities here
   except Exception as e:
       print(f"Error: {e}")
 
 
def main():
   wifi_scan_result = scan_wifi_networks()
   if wifi_scan_result:
       print("\nWi-Fi scan result:")
       print(wifi_scan_result)
       networks = re.findall(r'SSID\s\d+\s:\s(.+)', wifi_scan_result)
       for ssid in networks:
           print(f"\nSSID: {ssid}")
           encryption_match = re.search(r'Encryption\s*:\s(.+)', wifi_scan_result)
           if encryption_match:
               encryption_type = encryption_match.group(1).strip()
               print(f"Encryption Type: {encryption_type}")
               analyze_network_security(ssid, encryption_type)
           else:
               print("Error: Unable to retrieve encryption type.")
   else:
       print("No Wi-Fi networks found or error occurred during scanning.")
 
 
if __name__ == "__main__":
   main()