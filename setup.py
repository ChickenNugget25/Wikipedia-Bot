import subprocess
import sys

print('starting installs')

try:
    from bs4 import BeautifulSoup
except:
    try:
        subprocess.call([sys.executable,'-m pip install beautifulsoup4'])
    except:
        print('installing beautifulsoup4 failed, you might have to install it from a wheel file')
        quit()

try:
    import requests
except:
    try:
        subprocess.call([sys.executable,'pip install requests'])
    except:
        print('installing requests failed, you might have to install it from a wheel file')
        quit()

try:
    import pyttsx3
except:
    try:
        subprocess.call([sys.executable,'pip install pyttsx3'])
    except:
        print('installing pyttsx3 failed, you might have to install it from a wheel file')
        quit()

print('worked succesfully')
                    