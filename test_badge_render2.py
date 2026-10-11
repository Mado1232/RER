import subprocess, os

html = '''<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: #f2f4f7;
  padding: 40px;
  display: flex;
  gap: 30px;
  align-items: center;
  font-family: sans-serif;
}
.badge {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(135deg, #a15fd2 0%, #e44c81 100%);
  border: 3.5px solid #ffffff;
  box-shadow: 0 4px 14px rgba(123, 44, 191, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
}
.sticker-img {
  width: 38px;
  height: 42px;
  object-fit: contain;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.2));
}
</style>
</head>
<body>
  <div>
    <h4>Reference</h4>
    <img src="ref_sticker_detail.png" style="width: 58px;">
  </div>
  <div>
    <h4>Badge with Extracted Sticker</h4>
    <div class="badge">
      <img src="clean_extracted_sticker.png" class="sticker-img">
    </div>
  </div>
</body>
</html>
'''

with open('test_badge_view.html', 'w', encoding='utf-8') as f:
    f.write(html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\test_badge_out2.png'
in_path = os.path.abspath('test_badge_view.html')

subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=500,300',
    in_path
])
print('Rendered test_badge_out2.png')
