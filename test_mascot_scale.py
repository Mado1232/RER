import subprocess, os, re, base64
from PIL import Image

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const AUTHENTIC_CAT_STICKER_BASE64 = "(data:image/png;base64,[^"]+)"', text)
if m:
    data_url = m.group(1)
    b64 = data_url.split(',')[1]
    with open('test_cat.png', 'wb') as f:
        f.write(base64.b64decode(b64))

html = """<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="styles.css">
<style>
  body { background: #f2f4f7; padding: 20px; display: flex; justify-content: center; }
  .ticket-top-emblem {
    width: 58px;
    height: 58px;
    border-radius: 50%;
    background: linear-gradient(145deg, #ff3366 0%, #7928ca 100%);
    border: 3.5px solid #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(121, 40, 202, 0.28);
  }
  .test-sticker {
    width: 25px;
    height: 29px;
    object-fit: contain;
    display: block;
  }
</style>
</head>
<body>
  <div class="ticket-top-emblem">
    <img src="test_cat.png" class="test-sticker" />
  </div>
</body>
</html>
"""

with open('test_cat_circle.html', 'w', encoding='utf-8') as f:
    f.write(html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
subprocess.run([
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--screenshot=' + os.path.abspath('test_cat_circle.png'),
    '--window-size=200,150',
    os.path.abspath('test_cat_circle.html')
], check=True)

user_im = Image.open(r'C:\Users\Admin\.gemini\antigravity\brain\18c7e0a4-71bc-4cb2-954e-ac526294117a\.user_uploaded\media_1791669603168.png')
orig_mascot = user_im.crop((740, 95, 805, 175))
gen_mascot = Image.open('test_cat_circle.png').crop((65, 15, 135, 95))

comp = Image.new('RGB', (orig_mascot.width + gen_mascot.width + 10, max(orig_mascot.height, gen_mascot.height)), (220, 220, 220))
comp.paste(orig_mascot, (0, 0))
comp.paste(gen_mascot, (orig_mascot.width + 10, 0))
comp.save('compare_mascot_scale.png')
print('Saved compare_mascot_scale.png')
