import sys
import time
from progressbar import ProgressBar, Percentage, Bar

hosts_path = "C:/Windows/System32/drivers/etc/hosts"

redirect = "127.0.0.1"

web_list=['facebook.com', 'www.facebook.com', 'youtube.com', 'www.youtube.com', 'web.whatsapp.com', 'xvideos.com', 'www.xvideos.com']

file = open(hosts_path, 'r+')
content = file.read()

print('\n\n'"Este programa irá bloquear por padrão os seguintes sites: "+str(web_list[0:]),'\n')

pergunta = input('\n'"Gostaría de bloquear outro website? (y/n): ")

if pergunta.lower() == "y":
    opcao = input('\n'"Qual website? (1 website , ex: google.com): "'\n')
    web_list.append(opcao)
    pergunta = input('\n'"Gostaría de bloquear outro website? (y/n): "'\n')
else:
    pass

pergunta2 = input('\n'"Gostaría de excluir algum website da lista? (y/n): "'\n')
if pergunta2.lower() == 'y':
    opcao2 = input('\n'"Qual? (1 website, correspondencia exata): "'\n')
    web_list.remove(opcao2)
    pergunta2 = input('\n'"Gostaría de excluir algum website da lista? (y/n): "'\n')
else:
    pass

print("Bloqueando: \n"+str(web_list[0:])+'\n')

for website in web_list:
    if website in content:
        pass
    else:
        file.write(redirect+" "+website+"\n")


progress = ProgressBar(widgets=[Percentage(), Bar()], maxval = 500000).start()
progvar = 0

for i in range(500000):
    progress.update(progvar + 1)
    progvar += 1

print("\n\nPronto!")

time.sleep(2)
sys.exit()
