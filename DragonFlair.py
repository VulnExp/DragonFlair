import os
import time
import requests

os.system('clear')

text = '''
 (                                    (
 )\ )                                 )\ )  (
(()/(   (       )  (  (              (()/(  )\    )  (   (
 /(_))  )(   ( /(  )\))(  (    (      /(_))((_)( /(  )\  )(
(_))_  (()\  )(_))((_))\  )\   )\ )  (_))_| _  )(_))((_)(()\
 |   \  ((_)((_)_  (()(_)((_) _(_/(  | |_  | |((_)_  (_) ((_)
 | |) || '_|/ _` |/ _` |/ _ \| ' \)) | __| | |/ _` | | || '_|
 |___/ |_|  \__,_|\__, |\___/|_||_|  |_|   |_|\__,_| |_||_|
                  |___/
                            --𝐏𝐞𝐧𝐞𝐭𝐫𝐚𝐭𝐢𝐨𝐧 𝐭𝐨𝐨𝐥𝐤𝐢𝐭
                                    𝐦𝐚𝐝𝐞 𝐛𝐲 𝐕𝐮𝐥𝐧𝐄𝐱𝐩--
 [𝘧𝘰𝘳 𝘩𝘦𝘭𝘱, 𝘵𝘺𝘱𝘦 𝘩𝘦𝘭𝘱 𝘪𝘯 𝘵𝘦𝘳𝘮𝘪𝘯𝘢𝘭]
'''
print(text)
log_name = ["VulnExp"]
log_pass = ["VulnExploit"]
login_name = input("Username: ")
login_pass = input("Password: ")
if login_name in log_name:
    print("")
else:
    exit()
help = 'help'
ifconfig = 'ifconfig'
clear = 'clear'
cd = 'cd'
ls = 'ls'
ping = 'ping'
banner = 'banner'
nmap = 'nmap'
metasploit = 'metasploit'
adminpanel = 'panel_f'
while True:
   terminal = input("DragonFlair > ")
   try:
      if terminal in help:
         text2 = '''
 ------------
 | Commands |
 ------------
 - ifconfig = ifconfig gives you informations about your network and 
              you're ip address.

 - banner = You can Select a banner for the DragonFlair.

 - clear = You can clear the DragonFlair terminal.

 - ping = With the command ping you can find an ip address of a site.

 - help = help command gives you all the commands you can 
          type in the DragonFlair.

 - ls = With the ls command you can see the files that are in the 
        directory you're.


 ---------
 | Tools |
 ---------
 - nmap = nmap help you scan servers for possible vulnerabilities.

 - metasploit = With metasploit you can exploit vulnerabilities.

 - panel_f = panel_f helps you find hidden directory's and admin 
             panels of a site.

 
- MORE TOOLS COMING...
         '''
         print(text2)
      if terminal in ifconfig:
         os.system('ifconfig')

      if terminal in ls:
         os.system('ls')

      if terminal in clear:
         os.system('clear')

      if terminal in ping:
         ping_site = input("Enter a Site to ping > ")
         os.system('ping ' + ping_site)

      if terminal in adminpanel:
         try:
            name = input(str("url to find admin panel: "))
            wordlist = open("wordlist.txt","r")
            def findPanel(url):
               for words in wordlist:
                  words = words.strip()
                  response = requests.get(url+"/"+words)
                  print("")
                  if response.status_code == 200:
                     print(response.url)
                     continue
                  if response.status_code == 404:
                     print("nothing, continue searching")
                     continue
            findPanel(name)
         except:
            print("An error have been found, correct the url and try again")

      if terminal in nmap:
         nmap_commands = input("Enter Options for Nmap > ")
         nmap_host = input ("Enter Host for Nmap > ")
         os.system('nmap ' + nmap_commands + nmap_host)

      if terminal in metasploit:
         print("Starting Metasploit...")
         print("")
         os.system('msfconsole')

      if terminal in banner:
         one = 'banner 1'
         two = 'banner 2'
         three = 'banner 3'
         text3 = '''
         
         1) banner 1
         2) banner 2
         3) banner 3
         '''
         print(text3)

         select_banner = input("Select Banner > ")
         if select_banner in one:
            text4 = '''
█    ____                                  ________      _     
   / __ \_________ _____ _____  ____     / ____/ /___ _(_)____
  / / / / ___/ __ `/ __ `/ __ \/ __ \   / /_  / / __ `/ / ___/
 / /_/ / /  / /_/ / /_/ / /_/ / / / /  / __/ / / /_/ / / /    
/_____/_/   \__,_/\__, /\____/_/ /_/  /_/   /_/\__,_/_/_/     
                 /____/                                       
              '''
            print(text4)

         if select_banner in two:
            text5 = '''
 __ \                               ____| |      _)      
 |   |  __| _` |  _` |  _ \  __ \   |     |  _` | |  __| 
 |   | |   (   | (   | (   | |   |  __|   | (   | | |    
____/ _|  \__,_|\__, |\___/ _|  _| _|    _|\__,_|_|_|    
                |___/                                    
   '''
            print(text5)

         if select_banner in three:
            text6 = '''
 ___                           ___ _      _     
|   \ _ _ __ _ __ _ ___ _ _   | __| |__ _(_)_ _ 
| |) | '_/ _` / _` / _ \ ' \  | _|| / _` | | '_|
|___/|_| \__,_\__, \___/_||_| |_| |_\__,_|_|_|  
               |___/                             
'''    
            print(text6)                                                                                                                                                                                                             
   except:
      print("Error, Try again")