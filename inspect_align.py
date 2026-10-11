import subprocess, os, tempfile, json

test_html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="vendor/react.production.min.js"></script>
  <script src="vendor/react-dom.production.min.js"></script>
  <script src="vendor/html-to-image.js"></script>
  <script src="vendor/html2canvas.min.js"></script>
  <script src="app.js"></script>
  <script>
    // Wait for react to mount
    setTimeout(() => {
      const dump = {};
      const els = ['.app-container', '.clean-ticket-view-wrapper', '.ticket-export-wrapper', '.ticket-card-wrapper', '.ticket-card-body'];
      els.forEach(s => {
        const el = document.querySelector(s);
        if (el) {
          const r = el.getBoundingClientRect();
          const cs = window.getComputedStyle(el);
          dump[s] = {
            rect: { left: r.left, right: r.right, width: r.width },
            display: cs.display,
            flexDirection: cs.flexDirection,
            justifyContent: cs.justifyContent,
            alignItems: cs.alignItems,
            margin: cs.margin,
            padding: cs.padding,
            width: cs.width,
            maxWidth: cs.maxWidth
          };
        }
      });
      const p = document.createElement('pre');
      p.id = 'debug-output';
      p.textContent = JSON.stringify(dump, null, 2);
      document.body.appendChild(p);
    }, 600);
  </script>
</body>
</html>
"""

with open('inspect_align.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
with tempfile.TemporaryDirectory() as tmp_dir:
    out_file = os.path.abspath('inspect_align_out.html')
    subprocess.run([
        edge_path,
        '--headless',
        '--disable-gpu',
        '--virtual-time-budget=3000',
        f'--user-data-dir={tmp_dir}',
        '--dump-dom',
        '--window-size=390,844',
        'http://localhost:3000/inspect_align.html?view=clean'
    ], stdout=open(out_file, 'w', encoding='utf-8'))

with open('inspect_align_out.html', 'r', encoding='utf-8') as f:
    out = f.read()

import re
m = re.search(r'<pre id="debug-output">([^<]+)</pre>', out)
if m:
    print(m.group(1))
else:
    print("Not found")
