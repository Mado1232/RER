import subprocess, os, json

script = """
const all = document.querySelectorAll('*');
const widest = [];
for (const el of all) {
  const r = el.getBoundingClientRect();
  if (r.width > 390 || el.scrollWidth > 390) {
    widest.push({
      tag: el.tagName,
      cls: el.className,
      rectW: r.width,
      scrollW: el.scrollWidth,
      left: r.left,
      right: r.right
    });
  }
}
const div = document.createElement('div');
div.id = 'widest-report';
div.textContent = JSON.stringify(widest);
document.body.appendChild(div);
"""

with open('dom_dump.html', 'r', encoding='utf-8') as f:
    dom = f.read()

injected = dom.replace('</body>', f'<script>{script}</script></body>')
with open('test_widest.html', 'w', encoding='utf-8') as f:
    f.write(injected)

subprocess.run([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless',
    '--disable-gpu',
    '--window-size=390,844',
    '--dump-dom',
    os.path.abspath('test_widest.html')
], stdout=open('report_widest.html', 'w', encoding='utf-8'))

with open('report_widest.html', 'r', encoding='utf-8') as f:
    out = f.read()

import re
m = re.search(r'<div id="widest-report">([^<]+)</div>', out)
if m:
    data = json.loads(m.group(1))
    for item in data:
        print(f"{item['tag']}.{item['cls']}: rectW={item['rectW']}, scrollW={item['scrollW']}, left={item['left']}, right={item['right']}")
