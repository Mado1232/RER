import subprocess, os

html = '''<!DOCTYPE html>
<html>
<body style="font-size: 28px; padding: 20px; font-family: sans-serif;">
  <div style="font-family: sans-serif; margin-bottom: 12px;">Standard: № 375</div>
  <div style="margin-bottom: 12px;">Authentic Cyrillic: <span style="font-weight: 700; letter-spacing: -0.5px;">№</span> 375</div>
  <div>Custom underlined glyph: <span style="display: inline-flex; align-items: baseline; font-weight: 700;">N<span style="display: inline-flex; flex-direction: column; align-items: center; line-height: 1; transform: translateY(-0.25em); margin-left: 1px;"><span style="font-size: 0.58em; font-weight: 700;">o</span><span style="width: 100%; height: 1.5px; background: currentColor; margin-top: 1px;"></span></span></span> 375</div>
</body>
</html>'''

with open('test_no.html', 'w', encoding='utf-8') as f:
    f.write(html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\test_no.png'

subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=500,240',
    os.path.abspath('test_no.html')
])
print('Rendered test_no.png')
