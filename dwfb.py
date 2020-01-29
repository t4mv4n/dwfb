#python 3.7.1
#colors
s="\033[91m"
b="\033[92m"
c="\033[93m"
d="\33[36;1m"
bl = '\033[30m'
lb = '\033[94m'
lc = '\033[96m'
lr = '\033[91m'
lg = '\033[92m'
a  = '\033[93m'
j  = '\033[90m'
x  = '\033[0m'

print('''\033[92m
                                
                                
          ▄                  ▄      
          █▀▄              ▄▀█      
          █  ▀▄          ▄▀  █      
          █   ▀▀▀▀▀▀▀▀▀▀▀▀   █      
          █    ▄        ▄    █      
          █  ▄▀ ▀▄ ▄▄ ▄▀ ▀▄  █  █▀▀█
          █      ▄▄▄▄▄▄      █ █▀  ▄
          ▀▀▄▄▄▄▄▄▀██▀   ▄▄▄▀▀ █  ▄█
              ▀▀▀█▀▀▀▀▀▀▀▄     █  █ 
                ▄▀        ▀▄▄  █  █ 
                █  ▄   ▄    ▀▄▄█  █ 
                █  █   ██    ██  █▀ 
                █ ▄█▄ ▄█▀    █▄█▀▀  
                ▀▀▀ ▀▀▀▀▀▀▀▀▀ 
\033[93m          
       ______                __                __  
      / ____/___ _________  / /_  ____  ____  / /__
     / /_  / __ `/ ___/ _ \/ __ \/ __ \/ __ \/ //_/
    / __/ / /_/ / /__/  __/ /_/ / /_/ / /_/ / ,<   
   /_/    \__,_/\___/\___/_.___/\____/\____/_/|_|  
                                                   \033[92m   CODE BY: Pangusty Karjok         
                                                     RECODE BY: ANGGA    
    / __ \____ _      ______  / /___  ____ _____/ /__  _____
   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /    
 /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/
\033[92m________________________________________________  \033[0m         
 ''')
from requests import *
import re, os
             
def dl(url):
        r = get(url)
        urlv = re.search(r'\"(http[s]\:\/\/video.*?\.mp4\?.*?)\"',r.text)
        if urlv:
                print(b+"_____________________")
                print(b+"(sedang mendownload)")
                print(b+"_____________________")
                urlv = urlv.group(1).replace(";","&")             
                import random
                random_name = "videos"+ str(random.randint(1000,4444)) + ".mp4"
                konten = get(urlv).content
                file = open(random_name,"wb")
                file.write(konten)
                print(b+"_____________________")
                print(b+"(download berhasil)")
                print(b+"_____________________")
        else:
                print(s+"(video tidak di temukan)")
 
if __name__=='__main__':
        url = input(d+"(masukkan url video): ")
        dl(url)
    