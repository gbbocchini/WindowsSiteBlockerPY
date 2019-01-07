import sys
import time
from progressbar import ProgressBar, Percentage, Bar


hosts_path = "C:/Windows/System32/drivers/etc/hosts"

redirect = "127.0.0.1"

web_list=['facebook.com', 'www.facebook.com', 'youtube.com', 'www.youtube.com', 'web.whatsapp.com', 'xvideos.com', 'www.xvideos.com']

progress = ProgressBar(widgets=[Percentage(), Bar()], maxval = 1000000).start()
progvar = 0

with open(hosts_path, 'r+') as file:
    content = file.read()
    print("Bloqueando: \n"+str(web_list[0:])+'\n')
    for website in web_list:
        if website in content:
            pass
        else:
            file.write(redirect+" "+website+"\n")

    for i in range(1000000):
        progress.update(progvar + 1)
        progvar += 1

print("\n\nPronto!")

time.sleep(3)
sys.exit()
