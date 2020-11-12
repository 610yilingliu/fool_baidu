import os
import hashlib
from mp3_tagger import MP3File

files = os.listdir('./')
mp3s = []
md5s = []

def check_md5(fname):
    with open(fname, 'rb') as f:
        data = f.read()
        m5 = hashlib.md5(data).hexdigest()
        return m5

for f in files:
    if f.endswith('.mp3'):
        mp3s.append(f)
        md5s.append(check_md5(f))

md5s_after = []

for mp3fname in mp3s:
    mp3 = MP3File(mp3fname)
    mp3.comment = 'sb baidu'
    mp3.save()
    md5s_after.append(check_md5(mp3fname))

for i in range(len(mp3s)):
    print("File " + mp3s[i] + ' md5 code ' + md5s[i] + ' --> ' + md5s_after[i])

print("Press any key to quit...")
input()