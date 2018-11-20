#####Spyd3r#####
#####Start of Day Checklist#####

import urllib.request
import ssl
import datetime
import urllib.error

#Formating of date and time
now = datetime.datetime.now()

#Context to bypass SSL check on private servers.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Opens file for list of website
file = open('sites.txt')
urls = file.readlines()

#Counter
total_sites = 0
down_sites = 0

#VPN connection verification
input("VERIFY CONNECTION TO VPN, PRESS ENTER TO CONTINUE IF CONNECTED.")
print('\n')

#Prints date and time EX. Monday 11/19/2018 11:10
print(now.strftime("%A %m/%d/%Y %H:%M"), '\n')

#Start of loop
for site in urls:
    total_sites += 1
    
    try:
        resp = urllib.request.urlopen(site, context = ctx)

    except urllib.error.URLError as e:
        print('[-]DOWN: ' + site)
        down_sites += 1
        print(e.reason, '\n')

    else:
        print('[+]OK: ' + site)

#Results final printout
print('\n')
print(' _______________________________')
print('| TASK COMPLETED                |')
print('| ' + str(down_sites) + ' sites down out of ' + str(total_sites)+ ' sites  |')
print('|_______________________________|')

input("PRESS ENTER TO DISMISS.")
