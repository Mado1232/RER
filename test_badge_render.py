import subprocess

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
</style>
</head>
<body>
  <div>
    <h4>Reference</h4>
    <img src="ref_sticker_detail.png" style="width: 58px;">
  </div>
  <div>
    <h4>Vector SVG in Badge</h4>
    <div class="badge">
      <img src="cat_badge.svg" style="width: 36px; height: 38px;">
    </div>
  </div>
</body>
</html>
'''

with open('test_badge_view.html', 'w', encoding='utf-8') as f:
    f.write(html)

subprocess.run([
    'msedge.exe',
    '--headless',
    '--disable-gpu',
    '--screenshot=test_badge_out.png',
    '--window-size=500,300',
    'test_badge_view.html'
])
print('Rendered test_badge_out.png')
