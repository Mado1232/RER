import subprocess, os

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700;900&display=swap" rel="stylesheet">
<style>
  body {
    margin: 0;
    padding: 20px;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    gap: 25px;
  }
  .row {
    display: flex;
    align-items: flex-end;
    color: #111827;
    line-height: 1;
  }
  .d1 {
    display: inline-flex;
    align-items: flex-end;
    margin-right: 7px;
  }
</style>
</head>
<body>
  <!-- Variant 1: Roboto 700, 37px -->
  <div class="row">
    <span class="d1">
      <svg viewBox="0 0 27 46" width="20.5" height="35" fill="#111827">
        <polygon points="13.0,0 18.8,0 18.8,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 11.6,39.5 11.6,11.0 3.0,16.5 0.5,14.0 0.5,11.5" />
      </svg>
    </span>
    <span style="font-family: 'Roboto', sans-serif; font-size: 37px; font-weight: 700; letter-spacing: -0.6px; transform: translateY(2px);">квиток</span>
  </div>

  <!-- Variant 2: Roboto 900, 35px -->
  <div class="row">
    <span class="d1">
      <svg viewBox="0 0 27 46" width="20.5" height="35" fill="#111827">
        <polygon points="13.0,0 18.8,0 18.8,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 11.6,39.5 11.6,11.0 3.0,16.5 0.5,14.0 0.5,11.5" />
      </svg>
    </span>
    <span style="font-family: 'Roboto', sans-serif; font-size: 35px; font-weight: 900; letter-spacing: -0.6px; transform: translateY(2px);">квиток</span>
  </div>

  <!-- Variant 3: System sans-serif 700, 36px -->
  <div class="row">
    <span class="d1">
      <svg viewBox="0 0 27 46" width="20.5" height="35" fill="#111827">
        <polygon points="13.0,0 18.8,0 18.8,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 11.6,39.5 11.6,11.0 3.0,16.5 0.5,14.0 0.5,11.5" />
      </svg>
    </span>
    <span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; font-size: 36px; font-weight: 700; letter-spacing: -0.6px; transform: translateY(2px);">квиток</span>
  </div>
</body>
</html>
"""

with open('test_title_variants.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = os.path.abspath('test_title_variants.png')
in_path = os.path.abspath('test_title_variants.html')
subprocess.run([edge_path, '--headless', '--disable-gpu', f'--screenshot={out_path}', '--window-size=400,250', in_path], check=True)
print('Rendered test_title_variants.png')
