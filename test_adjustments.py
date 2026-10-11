import subprocess, os
from PIL import Image

# Test script to render:
# 1. Smaller mascot sticker inside pink circle
# 2. Smaller digit 1
# 3. Bigger validity pill
# 4. Lavender marquee strip

test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<style>
  body { background: #f2f4f7; padding: 20px; display: flex; justify-content: center; }
  .test-wrap { width: 432px; }
  
  /* Adjusted mascot */
  .test-emblem {
    width: 58px;
    height: 58px;
    border-radius: 50%;
    background: linear-gradient(145deg, #ff3366 0%, #7928ca 100%);
    border: 3.5px solid #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(121, 40, 202, 0.28);
    margin: 0 auto;
    position: relative;
    z-index: 10;
  }
  .test-sticker-img {
    width: 29px;
    height: 33px;
    object-fit: contain;
    display: block;
  }

  /* Adjusted pill */
  .test-pill {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    background: linear-gradient(90deg, #d7f5e4 0%, #d8edfb 100%);
    padding: 8.5px 28px;
    border-radius: 9999px;
  }
  .test-circle {
    width: 14.5px;
    height: 14.5px;
    border-radius: 50%;
    border: 1.6px solid #34d399;
    background: transparent;
  }
  .test-validity-text {
    font-size: 16.5px;
    font-weight: 500;
    color: #1f2937;
    font-variant-numeric: tabular-nums;
  }

  /* Adjusted digit 1 */
  .test-digit-one {
    width: 17px;
    height: 31px;
    fill: #111827;
    display: block;
    margin-right: 6px;
  }
  .test-qty-word {
    font-size: 35px;
    font-weight: 600;
    color: #111827;
    letter-spacing: -0.4px;
    transform: translateY(2px);
  }

  /* Lavender marquee strip */
  .test-marquee {
    background: #f7e9f6;
    color: #8c5995;
    padding: 6px 0;
    font-size: 13.5px;
    font-weight: 500;
    text-align: center;
    border-top: 1px solid #f0daf0;
    border-bottom: 1px solid #f0daf0;
  }
</style>
</head>
<body>
  <div class="test-wrap">
    <div class="test-emblem">
      <img src="data:image/png;base64,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" class="test-sticker-img" />
    </div>

    <div class="card" style="background:#fff; border-radius: 26px; padding: 20px 24px; margin-top: -24px;">
      <div class="test-marquee">
        і. Я живий! ◆ Життя — цікаве, і мотивація то є сил
      </div>

      <div style="text-align: center; margin-top: 14px;">
        <h2 style="font-size: 19px; font-weight: 500; color: #111827;">Тролейбус</h2>
      </div>

      <div style="display: flex; align-items: flex-end; justify-content: center; margin-top: 12px; line-height: 1;">
        <svg viewBox="0 0 27 46" class="test-digit-one">
          <polygon points="13.3,0 18.3,0 18.3,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 12.0,39.5 12.0,11.0 3.0,16.5 0.5,14.0 0.5,11.5" />
        </svg>
        <span class="test-qty-word">квиток</span>
      </div>

      <div style="display: flex; justify-content: center; margin-top: 14px;">
        <div class="test-pill">
          <span class="test-circle"></span>
          <span class="test-validity-text">Квиток дійсний — 59:48</span>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

with open('test_adjustments.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
subprocess.run([
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--screenshot=' + os.path.abspath('test_adjustments.png'),
    '--window-size=500,320',
    os.path.abspath('test_adjustments.html')
], check=True)

print('Saved test_adjustments.png')
