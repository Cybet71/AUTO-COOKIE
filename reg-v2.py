#!usr/bin/python3.11
import requests
import random,os
import time
import re
import urllib
from bs4 import BeautifulSoup as bxs
from bs4 import BeautifulSoup as bs
from fake_email import Email
# Random User Agent
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)

xyz = requests.Session()
ua = random_ua()
head1 = {'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9','cache-control':'max-age=0','referer':f'https://mbasic.facebook.com/reg/','sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android','sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':ua}
def footo():
  r = random.choice(['https://i.pinimg.com/736x/47/cb/b4/47cbb446dd61bfb03308af7dbefdba06.jpg','https://i.pinimg.com/736x/b5/13/22/b51322eeaa2b35fac59444ebde6d8d2f.jpg','https://raw.githubusercontent.com/Cybet71/Pic/main/hi.jpg','https://raw.githubusercontent.com/Cybet71/Pic/main/hlw.jpg','https://raw.githubusercontent.com/Cybet71/Pic/main/ic.png','https://raw.githubusercontent.com/Cybet71/Pic/main/ic_launcher.png','https://raw.githubusercontent.com/Cybet71/Pic/main/jii.jpg','https://raw.githubusercontent.com/Cybet71/Pic/main/n3.png','https://i.pinimg.com/736x/58/07/ba/5807ba1c263caaa5bbe0639d24ada8e2.jpg','https://i.pinimg.com/736x/72/bd/33/72bd338d114cec8922c14bd98322cf8a.jpg','https://i.pinimg.com/736x/c1/3d/21/c13d2188ceed1679fa2b8963031bc3e6.jpg'])
  return r
nm = 'Auto Create By Shishir Ahmed :)'

def profil(coki):
        try:
            fot = urllib.request.urlopen(footo())
            cookie = {'cookie': coki}
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bxs(xyz.get(url,cookies=cookie,headers=head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Simpan'}
            fil = {'pic' : fot}
            pos = bxs(xyz.post(raq['action'],data=dat,files=fil,cookies=cookie,headers=head1).content,'html.parser')
        except Exception as e:
            print(str(e))
def cover(coki):
        try:
            fot = urllib.request.urlopen(footo())
            cookie = {'cookie': coki}
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bxs(xyz.get(url,cookies=cookie,headers=head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Unggah'}
            fil = {'file1' : fot}
            pos = bxs(xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil,cookies=cookie,headers=head1).content,'html.parser')
        except Exception as e:
            pass
def bio(coki):
        try:
            cookie = {'cookie': coki}
            url = 'https://mbasic.facebook.com/profile/basic/intro/bio/'
            req = bxs(xyz.get(url,cookies=cookie,headers=head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : nm,
                'publish_to_feed' : True,
                'submit'          : 'Simpan'}
            pos = bxs(xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=cookie,headers=head1).content,'html.parser')
        except Exception as e:
            pass

def website(coki):
        try:
            cookie = {'cookie': coki}
            url = 'https://mbasic.facebook.com/editprofile.php?type=contact&edit=website'
            req = bxs(xyz.get(url,cookies=cookie,headers=head1).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'type'       : 'contact',
                'edit'       : 'website',
                'add_website': '1',
                'new_info'   : 'https://github.com/Shishir-Ahmed',
                'save'       : 'Tambahkan'}
            pos = bxs(xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=cookie,headers=head1).content,'html.parser')
        except Exception as e:
            pass
            
# Def For Ids Create
logo = """Author: Shishir Ahmed \nTelegram: @TataCuto\n"""
os.system('clear')
print(logo)
def create():
  #try:
    # Get Email And Genarate Number 
    mmail=Email().Mail();new_mail=mmail['mail'];xyz = requests.Session()
    number = str(random.choice(['+88016','+88017','+88013','+88019','+88018'])) + str(random.randrange(10000000,99999999))
    # Request Get Mbasic Facebook To Get Cookie
    cookies = {'datr': 'lMflZkPaRmNTh67eRAcGAf50','sb': 'lMflZgrh5P2nCUL5QUa0Ir2t','ps_l': '1','ps_n': '1','locale': 'en_US','vpd': 'v1%3B795x421x2.5687501430511475','m_pixel_ratio': '2.5687501430511475','x-referer': 'eyJyIjoiL3JlZy8%2FYXBwX2lkPTQ5MDEwNTI2NDc5NzkxMiZsb2dnZXJfaWQ9Mzk5Y2UxZjYtNmZmNC00MjQzLTliNzEtMzRlMGE4ZWU3MTJjJmlzX3R3b19zdGVwc19sb2dpbj0wJmNpZD0xMDMmbmV4dD1odHRwcyUzQSUyRiUyRm0uZmFjZWJvb2suY29tJTJGdjMuMiUyRmRpYWxvZyUyRm9hdXRoJTNGY2N0X3ByZWZldGNoaW5nJTNEMCUyNmNsaWVudF9pZCUzRDQ5MDEwNTI2NDc5NzkxMiUyNmNidCUzRDE3MTAwMTA5Mjg3MTklMjZlMmUlM0QlMjU3QiUyNTIyaW5pdCUyNTIyJTI1M0ExNzEwMDEwOTI4NzE5JTI1N0QlMjZpZXMlM0QwJTI2c2RrJTNEYW5kcm9pZC0xNC4xLjElMjZzc28lM0RjaHJvbWVfY3VzdG9tX3RhYiUyNm5vbmNlJTNENzgyM2NiZWQtYWRiMy00MWQxLTg1YmEtNDk0NzFmNWZmYzNiJTI2c2NvcGUlM0RvcGVuaWQlMjUyQ3B1YmxpY19wcm9maWxlJTI1MkN1c2VyX2ZyaWVuZHMlMjZzdGF0ZSUzRCUyNTdCJTI1MjIwX2F1dGhfbG9nZ2VyX2lkJTI1MjIlMjUzQSUyNTIyMzk5Y2UxZjYtNmZmNC00MjQzLTliNzEtMzRlMGE4ZWU3MTJjJTI1MjIlMjUyQyUyNTIyM19tZXRob2QlMjUyMiUyNTNBJTI1MjJjdXN0b21fdGFiJTI1MjIlMjUyQyUyNTIyN19jaGFsbGVuZ2UlMjUyMiUyNTNBJTI1MjJwZjYwa3Bia29lZmxwOTcxdjJjaSUyNTIyJTI1N0QlMjZjb2RlX2NoYWxsZW5nZV9tZXRob2QlM0RTMjU2JTI2ZGVmYXVsdF9hdWRpZW5jZSUzRGZyaWVuZHMlMjZsb2dpbl9iZWhhdmlvciUzRE5BVElWRV9XSVRIX0ZBTExCQUNLJTI2cmVkaXJlY3RfdXJpJTNEZmJjb25uZWN0JTI1M0ElMjUyRiUyNTJGY2N0LmNvbS5taW5pY2xpcC5jYXJyb20lMjZhdXRoX3R5cGUlM0RyZXJlcXVlc3QlMjZyZXNwb25zZV90eXBlJTNEaWRfdG9rZW4lMjUyQ3Rva2VuJTI1MkNzaWduZWRfcmVxdWVzdCUyNTJDZ3JhcGhfZG9tYWluJTI2cmV0dXJuX3Njb3BlcyUzRHRydWUlMjZjb2RlX2NoYWxsZW5nZSUzRFBuLUJPN25UWElyWFNzMkpUY3d6UHp6OWI1OWhUUzg4QkRtSHBzZWR6LVUlMjZyZXQlM0Rsb2dpbiUyNmZiYXBwXy4uLiIsImgiOiIvcmVnLz9hcHBfaWQ9NDkwMTA1MjY0Nzk3OTEyJmxvZ2dlcl9pZD0zOTljZTFmNi02ZmY0LTQyNDMtOWI3MS0zNGUwYThlZTcxMmMmaXNfdHdvX3N0ZXBzX2xvZ2luPTAmY2lkPTEwMyZuZXh0PWh0dHBzJTNBJTJGJTJGbS5mYWNlYm9vay5jb20lMkZ2My4yJTJGZGlhbG9nJTJGb2F1dGglM0ZjY3RfcHJlZmV0Y2hpbmclM0QwJTI2Y2xpZW50X2lkJTNENDkwMTA1MjY0Nzk3OTEyJTI2Y2J0JTNEMTcxMDAxMDkyODcxOSUyNmUyZSUzRCUyNTdCJTI1MjJpbml0JTI1MjIlMjUzQTE3MTAwMTA5Mjg3MTklMjU3RCUyNmllcyUzRDAlMjZzZGslM0RhbmRyb2lkLTE0LjEuMSUyNnNzbyUzRGNocm9tZV9jdXN0b21fdGFiJTI2bm9uY2UlM0Q3ODIzY2JlZC1hZGIzLTQxZDEtODViYS00OTQ3MWY1ZmZjM2IlMjZzY29wZSUzRG9wZW5pZCUyNTJDcHVibGljX3Byb2ZpbGUlMjUyQ3VzZXJfZnJpZW5kcyUyNnN0YXRlJTNEJTI1N0IlMjUyMjBfYXV0aF9sb2dnZXJfaWQlMjUyMiUyNTNBJTI1MjIzOTljZTFmNi02ZmY0LTQyNDMtOWI3MS0zNGUwYThlZTcxMmMlMjUyMiUyNTJDJTI1MjIzX21ldGhvZCUyNTIyJTI1M0ElMjUyMmN1c3RvbV90YWIlMjUyMiUyNTJDJTI1MjI3X2NoYWxsZW5nZSUyNTIyJTI1M0ElMjUyMnBmNjBrcGJrb2VmbHA5NzF2MmNpJTI1MjIlMjU3RCUyNmNvZGVfY2hhbGxlbmdlX21ldGhvZCUzRFMyNTYlMjZkZWZhdWx0X2F1ZGllbmNlJTNEZnJpZW5kcyUyNmxvZ2luX2JlaGF2aW9yJTNETkFUSVZFX1dJVEhfRkFMTEJBQ0slMjZyZWRpcmVjdF91cmklM0RmYmNvbm5lY3QlMjUzQSUyNTJGJTI1MkZjY3QuY29tLm1pbmljbGlwLmNhcnJvbSUyNmF1dGhfdHlwZSUzRHJlcmVxdWVzdCUyNnJlc3BvbnNlX3R5cGUlM0RpZF90b2tlbiUyNTJDdG9rZW4lMjUyQ3NpZ25lZF9yZXF1ZXN0JTI1MkNncmFwaF9kb21haW4lMjZyZXR1cm5fc2NvcGVzJTNEdHJ1ZSUyNmNvZGVfY2hhbGxlbmdlJTNEUG4tQk83blRYSXJYU3MySlRjd3pQeno5YjU5aFRTODhCRG1IcHNlZHotVSUyNnJldCUzRGxvZ2luJTI2ZmJhcHBfcHJlcyUzRDAlMjZsb2dnZXJfaWQlM0QzOTljZTFmNi02ZmY0LTQyNDMtOWI3MS0zNGUwYThlZTcxMmMlMjZ0cCUzRHVuc3BlY2lmaWVkJmxvY2FsZTI9ZW5fR0ImcmVmc3JjPWRlcHJlY2F0ZWQmc29mdD1oamsiLCJzIjoibWJhc2ljIn0%3D','wd': '421x795','fr': '0AJr3QVf3gLy2v8CT.AWXjmKZSQpMJ6eAbjvCcpOJPYGY.Bm5LhS..AAA.0.0.Bm6Ve-.AWWR9O8wfbc'}
    headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2.5687501430511475','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"23129RAA4G"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"14.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','viewport-width': '980'}
    response = xyz.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1710010928719%26e2e%3D%257B%2522init%2522%253A1710010928719%257D%26ies%3D0%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D7823cbed-adb3-41d1-85ba-49471f5ffc3b%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DPn-BO7nTXIrXSs2JTcwzPzz9b59hTS88BDmHpsedz-U%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D399ce1f6-6ff4-4243-9b71-34e0a8ee712c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522399ce1f6-6ff4-4243-9b71-34e0a8ee712c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522pf60kpbkoeflp971v2ci%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',cookies=cookies,headers=headers).text
    soup = bs(response,'html.parser')
    for ku in soup.find_all('a'):
         if "Create" in ku.text:
           link=ku['href'].replace('amp;','')
    url = "https://mbasic.facebook.com"+link
    res1 = bxs(xyz.get(url,headers=headers).text,'html.parser')
    # Reg Data And Submit Process 
    headers = {"Host": "mbasic.facebook.com","User-Agent": random_ua(), "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  "Accept-Language": "en-US,en;q=0.5","Referer": "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr","Content-Type": "application/x-www-form-urlencoded", "Content-Length": "547","Origin": "https://mbasic.facebook.com","Dnt": "1","Upgrade-Insecure-Requests": "1","Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin","Sec-Fetch-User": "?1","Te": "trailers"}
    name = input('Put Name : ')
    name1 = name.split(' ')[0] #random.choice(['Mohammad Abir','Md Sefat Khan','Hasibul Hassan Rabbi','Sh Akash Dash','Robiul Islam','Tasniya Tisha','Mustafizur Rahman','Sami Ahmed','Rafi Ahmed','Mis Sadiya','Md Ashik','Salman Muqtadir','Robiul Islam Topu','Tabassum Akhter','Saimunnesa Saimun']);name1 = name.split(' ')[0]
    try:name2 = name.split(' ')[1]+' '+name.split(' ')[2]
    except:name2 = name.split(' ')[1]
    paswed = input('Put Password : ')
    lsd = res1.select_one('input[name=lsd]')['value']
    jjj = res1.select_one('input[name=jazoest]')['value']
    ccp = res1.select_one('input[name=ccp]')['value']
    reg = res1.select_one('input[name=reg_instance]')['value']
    sub = res1.select_one('input[name=submission_request]')['value']
    imp = res1.select_one('input[name=reg_impression_id]')['value']
    data = f"lsd={lsd}&jazoest={jjj}&ccp={ccp}&reg_instance={reg}&submission_request={sub}&helper=&reg_impression_id={imp}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names%5B%5D=firstname&field_names%5B%5D=reg_email__&field_names%5B%5D=sex&field_names%5B%5D=birthday_wrapper&field_names%5B%5D=reg_passwd__&firstname={name1}&lastname={name2}&reg_email__={number}&sex=2&custom_gender=&did_use_age=false&birthday_month={str(random.randrange(0,12))}&birthday_day={str(random.randrange(1,29))}&birthday_year={str(random.randrange(1980,1999))}&age_step_input=&reg_passwd__={paswed}&submit=Sign+Up"
    res2 = xyz.post('https://mbasic.facebook.com/reg/submit/', data=data,headers=headers)
    res3 = xyz.get('https://mbasic.facebook.com/')
    cok =  (";").join([f"{key}={value}" for key,value in xyz.cookies.get_dict().items()])
    if "Enter confirmation code" in res3.text:st="ok"
    elif "checkpoint" in res3.text:st="cp"
    elif "There was an error with your registration. Please try registering again." in res3.text:st="cp"
    else:st="ok"
    if st == "ok":
       print('\nAccount Is Live ')
       cok = {'cookie': cok}
       res = xyz.get('https://mbasic.facebook.com',cookies=cok)
       soup = bxs(res.text,'html.parser')
       link = 'https://mbasic.facebook.com'+soup.find('a',class_="be bf bg bh bi bj")['href']
       data = {'fb_dtsg': soup.find('input', type="hidden")['value'],'jazoest': soup.find('input', type="hidden")['value'],'next': '','old_email': soup.find('span',dir="ltr").text.replace('-','').replace(' ','').strip(),'reg_instance': xyz.cookies['datr'],'new': new_mail,'submit': 'Add'}
       res = bxs(xyz.post(link,data=data,cookies=cok).text,'html.parser')
       link = 'https://mbasic.facebook.com'+res.find('form',{'method':'post'})['action']
       res = xyz.post(link,data=data,cookies=cok).text
       while True:
          h=Email(mmail["session"]).inbox()
          if h:
             j = h['topic'].split('-')[1];hh = j.split(' ')[0];cd = hh
             break
       try:uid = cok['cookie'].split('c_user=')[1].split(';')[0]
       except:uid = new_mail
       print(f'Code: {cd}')
       r = xyz.get('https://mbasic.facebook.com',cookies=cok).text
       res1 = bs(r,'html.parser')
       dtsg = res1.select_one('input[name=fb_dtsg]')['value']
       jjjj = res1.select_one('input[name=jazoest]')['value']
       headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"','sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': '11.0.0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': random_ua()}
       data = {'contact': new_mail,'type': 'submit','is_soft_cliff': False,'medium': 'email','code': cd,'fb_dtsg': dtsg,'jazoest': jjjj,'__user': uid}
       url = 'https://m.facebook.com/confirmation_cliff/'
       res = xyz.post(url,data=data,headers=headers).text
       print('OK ID : '+uid+'|'+paswed)
       profil(coki=cok['cookie']);cover(coki=cok['cookie'])
       bio(coki=cok['cookie']);website(coki=cok['cookie'])
       open('/sdcard/fb_reg_ok_cookie.txt','a').write(uid+'|'+paswed+'|'+cok['cookie']+'\n')
       print('Created Successfully ')
    else:exit('Try Again Bro :)')
  #except requests.exceptions.ConnectionError:print('\033[0m[\033[1;31m-\033[0m] Internet Connection Error ! ');print("\033[0m[\033[1;31m-\033[0m] Try To Account Create Again ");print('----------------------------------------');time.sleep(5);create()
  #except Exception as e:print('\033[0m[\033[1;31m-\033[0m] Error Createing Account ! '+str(e));print("\033[0m[\033[1;31m-\033[0m] Try To Account Create Again ");print('----------------------------------------');time.sleep(5);create()

create()
