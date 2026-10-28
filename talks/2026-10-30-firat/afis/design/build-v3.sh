set -e
/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/venv/bin/python -I - <<'PY'
import re, subprocess
D='/Users/polat/DEV/civilization-2-0/design'
col=subprocess.run(['/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/venv/bin/python','-I','/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/column.py'],capture_output=True,text=True,check=True).stdout
svg=open(D+'/qr.svg').read(); svg=re.sub(r'<\?xml[^>]*\?>','',svg).replace('width="29mm" height="29mm" ','').strip()
h=open(D+'/poster-v3.template.html').read().replace('<!--COLUMN-->',col).replace('<!--QR-->',svg)
open(D+'/poster-v3.html','w').write(h)
PY
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --user-data-dir=/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/chrome-prof --allow-file-access-from-files --force-device-scale-factor=2 --window-size=1240,1754 --virtual-time-budget=4000 --screenshot=/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/v3.png "file:///Users/polat/DEV/civilization-2-0/design/poster-v3.html" >/dev/null 2>&1
/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/venv/bin/python -I -c "from PIL import Image; im=Image.open('/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/v3.png'); im.resize((1240,1754), Image.LANCZOS).save('/private/tmp/claude-501/-Users-polat-DEV-civilization-2-0/ea4c7c1a-b9d1-4414-a7fd-b436d1746aa7/scratchpad/v3_small.png')"
