import webbrowser
import time
import os
import colorama
from colorama import Fore, Back, Style


print("""
       
     /$$$$$$            /$$       /$$                     /$$$$$$/              / $$$$$$$/
    /$$__  $$          | $$      | $$                      | $$                | $$
   | $$  \__/  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$$\  | $$    / $$$$$$$\  | $$     /$$$$$$
   | $$ /$$$$ /$$__  $$| $$ /$$__  $$ /$$__  $$| $$__  $$| | $$   | $$__   $$| | $$$$/ /$$    $$
   | $$|_  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \ $$| | $$   | $$  \  $$| | $$   | $$    $$
   | $$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$  | $$| | $$   | $$  |  $$| | $$   | $$    $$ 
   |  $$$$$$/|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$  | $$|/$$$$$$ | $$  |  $$| | $$   |  $$$$$$/
    \______/  \______/ |__/ \_______/ \_______/|__/  |__//______/ |__/  |___/  |__/    \______/ 
                                                                     
                                               BY Hamza Mourid                           
                                                                     

""")
time.sleep(3)
print("""
                    [1]: google.com
                    [2]: yahoo.com
                    [3]: bing.com
                    [4]: duckduckgo.com
                    [5]: qwant.com
                    [6]: yandex.com
                    [7]: seznam.cz
                    [8]: startpage.com
                    [9]: m.so.com
                    [10]:m5.baidu.com

""")
SEARCH = int(input("CHOOSE A SEARCH ENGINE: "))

while True:

    def TYPES(x):
        if TYPE == 1:
            b = str("(.txt|.pdf|.lit|.doc|.zip|.rar|.pps|.odt|.rtf)")
            return b
        elif TYPE == 2:
            n = str("(.mp3|.wma|.ogg)")
            return n
        elif TYPE == 3:
            g = str("(.exe|.rar|.zip|.dll|.apk)")
            return g
        elif TYPE == 4:
            e = str("(.mpg|.mp4|.wmv|.divx|.flv)")
            return e

    def simple(v):
        if SEARCH == 1 :
            v = "http://google.com"
            return v
        elif SEARCH == 2 :
            c = "http://yahoo.com"
            return c
        elif SEARCH == 3 :
            a = "http://bing.com"
            return a
        elif SEARCH == 4 :
            b = "http://duckduckgo.com"
            return b
        elif SEARCH == 5 :
            d = "http://qwant.com"
            return d
        elif SEARCH == 6 :
            f = "http://yandex.com"
            return f
        elif SEARCH == 7 :
            x = "http://seznam.cz"
            return x
        elif SEARCH == 8 :
            z = "http://startpage.com"
            return z
        elif SEARCH == 9 :
            y = "http://m.so.com"
            return y
        elif SEARCH == 10 :
            m = str("http://m5.baidu.com")
            return m
        


    print(Fore.WHITE+"""
                    [1]: books
                    [2]: music
                    [3]: Application
                    [4]: video
                    [5]: Hacks
                    [6]: web archive (Cache)
                    [7]: web hosting
                    [8]: Torrent
                    [9]: phone search
                    [10]: back
    """)
    TYPE = int(input("WHAT DO YOU LOOK FOR choose number: "))
    search = str(input("looking for: "))
    
        
    if TYPE == 5:
        v1 = "/search?q=inurl:passlist.txt | allinurl:auth_user_file.txt site:"
        v2 = "| allinurl:auth_user_file.txt site:"
        v3 = "Index of"
        v4 = " | intitle:"+v3+"config.php site:"
        j = v1+search+v2+search+v4+search
        webbrowser.open(simple(1)+j)

    elif TYPE == 6:
        webbrowser.open("http://web.archive.org/web/*/http://"+search)

    elif TYPE == 8:
        webbrowser.open(simple(1)+"/search?q="+search+"&btnG=Search&q=filetype%3Atorrent")

    elif TYPE == 7:
        webbrowser.open(simple(2)+"/search?q="+search+"""&btnG=Search&q=%28&q=bigupload.com%2Fd+%7C&q=filefactory.com%2Ffile+%7C&q=dl-1.free.fr+%7C&q=gigasize.com%2Fget.php+%7C&q=d01.megashares.com%2F%3Fd01+%7C&q=megaupload.com%2F%3Fd+%7C&q=rapidshare.com%2Ffiles+%7C&q=rapidshare.de%2Ffiles+%7C&q=rapidupload.com%2Fd.php+%7C&q=sendspace.com%2Ffi
                        le+%7C&q=sexuploader.com%2F%3Fd+%7C&q=uploading.com%2F%3Fget+%7C&q=uploadport.com%2Frequest%2F%3Ffid+%7C&q=zupload.com%2Fdownload.php+%7C&q=%29""")    

    elif TYPE == 1 or TYPE == 2 or TYPE == 3 or TYPE == 4:
        cot = str('"')
        space = str("%20")
        func = TYPES(1)
        webbrowser.open(simple(1)+'''/search?q=-inurl:(htm|html|php) intitle:"index of" %2b "last modified" %2b "parent directory" %2b description %2b size %2b'''+func+space+cot+search+cot)
    
      
    if TYPE == 9:
        for var in search:
            try:
                int(search)
            except:
                ValueError
                break
        time.sleep(3)
        print("[i] scanning phone number "+search)
        print("[i] running scan ...")
        time.sleep(7)
        cote = ('"')
        print("[i] Generating Google search dork requests...")
        print(Fore.RED+"     [i] Social media footprints")
        print(Fore.GREEN+"[+] Link: "+simple(1)+"/search?q=intext%3A"+cote+search+cote+"+OR+intext%3A%2B"+cote+search+cote+"+OR+intext%3A"+cote+search+cote+"&go=Rechercher&qs=ds&form=QBRE")
        print("[+] Link: "+simple(2)+"/search?q=site%3Afacebook.com+intext%3A%22"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Atwitter.com+intext%3A%22"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Alinkedin.com+intext%3A%22"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Ainstagram.com+intext%3A%22"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Avk.com+intext%3A%22"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%"+cote+search+cote+"%22")
        time.sleep(4)
        print(Fore.RED+"     [i] Individual footprints")
        print(Fore.GREEN+"[+] Link: "+simple(2)+"/search?q=site%3Anuminfo.net+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Async.me+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Awhocallsyou.de+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Apastebin.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Awhycall.me+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Alocatefamily.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Aspytox.com+intext%3A%220"+cote+search[3:]+cote+"%22")
        time.sleep(4)
        print(Fore.RED+"     [i] Reputation footprints")
        print(Fore.GREEN+"[+] Link: "+simple(2)+"/search?q=site%3Awhosesearch.info+intext%3A%22%2B"+cote+search+cote+"%22+intitle%3A%22who+called%22")
        print("[+] Link: "+simple(2)+"/search?q=intitle%3A%22Phone+Fraud%22+intext%3A%22"+cote+search+cote+"%22+OR+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Afindwhocallsme.com+intext%3A%22%2B"+cote+search+cote+"%22+OR+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Ayellowpages.ca+intext%3A%22%2B"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Aphonesearchs.ie+intext%3A%22%2B"+cote+search+cote+"%22")
        time.sleep(4)      
        print(Fore.RED+"      [i] Temporary search providers footprints")
        print(Fore.GREEN+"[+] Link: "+simple(2)+"/search?q=site%3Ahs3x.com+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceive-sms-now.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asmslisten.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asmssearchsonline.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Afreesmscode.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Acatchsms.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asmstibo.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asmsreceiving.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Agetfreesmssearch.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asellaite.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceive-sms-online.info+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceivesmsonline.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceive-a-sms.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asms-receive.net+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceivefreesms.com+intext%3A%22"+cote+search+cote+"%22+OR+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"+/search?q=site%3Areceive-sms.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceivetxt.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Afreephonenum.com+intext%3A%22"+cote+search+cote+"%22+OR+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Afreesmsverification.com+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Areceive-sms-online.com+intext%3A%22"+cote+search+cote+"%22+OR+intext%3A%220"+cote+search[3:]+cote+"%22")
        print("[+] Link: "+simple(2)+"/search?q=site%3Asmslive.co+intext%3A%220"+cote+search[3:]+cote+"%22+OR+intext%3A%22"+cote+search+cote+"%22")












    
