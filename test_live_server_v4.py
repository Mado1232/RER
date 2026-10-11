import subprocess, os, time
from PIL import Image

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# 1. Desktop screenshot
desktop_out = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\preview-v4-desktop.png'
subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={desktop_out}',
    '--window-size=1200,860',
    'http://localhost:3000/'
])
print('Rendered desktop v4:', os.path.exists(desktop_out))

# 2. Mobile clean screenshot
mobile_out = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\preview-v4-mobile.png'
subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={mobile_out}',
    '--window-size=430,940',
    'http://localhost:3000/?view=clean'
])
print('Rendered mobile clean v4:', os.path.exists(mobile_out))

# 3. Update exported_ticket_sample.png and .jpg
if os.path.exists(mobile_out):
    img = Image.open(mobile_out)
    img.save('exported_ticket_sample.png')
    img.convert('RGB').save('exported_ticket_sample.jpg', quality=95)
    print('Updated exported_ticket_sample.png and .jpg')
