import subprocess, os, json

script = """
const elements = [
  'body',
  '.app-container',
  '.clean-ticket-view-wrapper',
  '.ticket-export-wrapper',
  '.ticket-card-wrapper',
  '.ticket-card-body'
];

const report = {};
for (const sel of elements) {
  const el = document.querySelector(sel);
  if (el) {
    const r = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    report[sel] = {
      left: r.left,
      right: r.right,
      width: r.width,
      marginLeft: style.marginLeft,
      marginRight: style.marginRight,
      paddingLeft: style.paddingLeft,
      paddingRight: style.paddingRight,
      boxSizing: style.boxSizing
    };
  }
}

const div = document.createElement('div');
div.id = 'layout-report';
div.textContent = JSON.stringify(report);
document.body.appendChild(div);
"""

# Inject this script into a test HTML wrapper
with open('dom_dump.html', 'r', encoding='utf-8') as f:
    dom = f.read()

injected = dom.replace('</body>', f'<script>{script}</script></body>')
with open('test_inspect.html', 'w', encoding='utf-8') as f:
    f.write(injected)

# Run Edge headless and dump DOM with report
subprocess.run([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless',
    '--disable-gpu',
    '--window-size=390,844',
    '--dump-dom',
    os.path.abspath('test_inspect.html')
], stdout=open('report_out.html', 'w', encoding='utf-8'))

with open('report_out.html', 'r', encoding='utf-8') as f:
    out = f.read()

import re
m = re.search(r'<div id="layout-report">([^<]+)</div>', out)
if m:
    data = json.loads(m.group(1))
    for k, v in data.items():
        print(f"{k}: left={v['left']}, right={v['right']}, width={v['width']}, padL={v['paddingLeft']}, padR={v['paddingRight']}, marL={v['marginLeft']}, marR={v['marginRight']}")
else:
    print("Report not found in output")
