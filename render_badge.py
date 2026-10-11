import subprocess, os

# 1. Run build sticker
with open('build_sticker.py', 'r', encoding='utf-8') as f:
    exec(f.read())

# 2. Render screenshot
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\test_badge_out.png'
in_path = os.path.abspath('test_badge_view.html')

subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=500,300',
    in_path
])
print('Successfully rendered test_badge_out.png')
