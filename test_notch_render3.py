import subprocess, os

html = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {
  background: #f2f4f7;
  padding: 40px;
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.test-container {
  display: flex;
  gap: 30px;
  align-items: flex-start;
}
.ref-box {
  width: 212px;
}
.ref-box img {
  width: 100%;
  display: block;
}

/* Implementation wrapper */
.card-wrapper {
  position: relative;
  width: 212px;
  padding-top: 38px;
}

.top-bar {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  position: absolute;
  top: 10px;
  right: 0;
  width: 100%;
  height: 28px;
  z-index: 20;
}

.badge-anchor {
  position: absolute;
  top: -38px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}

.badge {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(135deg, #9a55d1 0%, #e02874 100%);
  border: 3.5px solid #ffffff;
  box-shadow: 0 4px 14px rgba(123, 44, 191, 0.28);
  display: flex;
  align-items: center;
  justify-content: center;
}

.sticker-img {
  width: 44px;
  height: 48px;
  object-fit: contain;
}

.info-btn {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 1.5px solid #9ca3af;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
  font-family: serif;
  font-size: 13px;
  font-weight: 600;
  font-style: italic;
  margin-right: 2px;
  background: transparent;
  cursor: pointer;
}

.white-card {
  background: #ffffff;
  border-radius: 26px 26px 0 0;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  padding-top: 24px;
  position: relative;
  height: 120px;
}

.notch-cutout {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 106px;
  height: 28px;
  z-index: 3;
  pointer-events: none;
}

.ticker-sample {
  background: #ebf5fb;
  color: #0284c7;
  font-size: 11px;
  padding: 6px 10px;
  margin-top: 10px;
  white-space: nowrap;
  overflow: hidden;
}
</style>
</head>
<body>
  <div class="test-container">
    <div class="ref-box">
      <h4>Reference</h4>
      <img src="user_badge_notch_ref.png">
    </div>
    <div class="card-wrapper">
      <h4>Our Implementation</h4>
      <div class="top-bar">
        <div class="info-btn" title="Інформація">i</div>
      </div>
      <div class="white-card">
        <div class="badge-anchor">
          <div class="badge">
            <img src="clean_extracted_sticker.png" class="sticker-img">
          </div>
        </div>
        <div class="notch-cutout">
          <svg viewBox="0 0 106 28" width="100%" height="100%" preserveAspectRatio="none">
            <path d="M 0 0 L 14 0 C 23 0 28 3.5 32 8 C 38 15.5 45 22 53 22 C 61 22 68 15.5 74 8 C 78 3.5 83 0 92 0 L 106 0 Z" fill="#f2f4f7" />
          </svg>
        </div>
        <div class="ticker-sample">Життя — цікаве, і мотивація то є сильн ◆</div>
      </div>
    </div>
  </div>
</body>
</html>
'''

with open('test_notch_view.html', 'w', encoding='utf-8') as f:
    f.write(html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\test_notch_out3.png'
in_path = os.path.abspath('test_notch_view.html')

subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=650,380',
    in_path
])
print('Rendered test_notch_out3.png')
