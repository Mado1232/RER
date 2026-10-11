import subprocess, os, json, re

script = """
const el = document.querySelector('.ticket-card-wrapper');
let cur = el;
const chain = [];
while (cur && cur !== document.documentElement) {
  const r = cur.getBoundingClientRect();
  const cs = window.getComputedStyle(cur);
  chain.push({
    tag: cur.tagName,
    cls: cur.className,
    r_left: r.left,
    r_right: r.right,
    r_width: r.width,
    pad: cs.padding,
    mar: cs.margin,
    display: cs.display,
    justify: cs.justifyContent,
    alignItems: cs.alignItems
  });
  cur = cur.parentElement;
}
document.title = JSON.stringify(chain);
"""

with open('debug_chain.html', 'w', encoding='utf-8') as f:
    f.write(f"""<!DOCTYPE html><html><head><link rel="stylesheet" href="styles.css"></head><body><div id="root"></div><script src="vendor/react.production.min.js"></script><script src="vendor/react-dom.production.min.js"></script><script src="vendor/html-to-image.js"></script><script src="vendor/html2canvas.min.js"></script><script src="app.js"></script><script>
setTimeout(() => {{
  {script}
}}, 300);
</script></body></html>""")

subprocess.run([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless',
    '--disable-gpu',
    '--window-size=412,915',
    '--dump-dom',
    'http://localhost:3000/?view=clean'
], stdout=open('debug_chain_out.html', 'w', encoding='utf-8'))

with open('debug_chain_out.html', 'r', encoding='utf-8') as f:
    out = f.read()

# Let's inspect the injected script by running on local debug_chain.html
subprocess.run([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless',
    '--disable-gpu',
    '--window-size=412,915',
    '--dump-dom',
    os.path.abspath('debug_chain.html')
], stdout=open('debug_chain_out2.html', 'w', encoding='utf-8'))

with open('debug_chain_out2.html', 'r', encoding='utf-8') as f:
    out2 = f.read()

m = re.search(r'<title>(\[.+?\])</title>', out2)
if m:
    data = json.loads(m.group(1))
    for item in data:
        print(f"{item['tag']}.{item['cls']}: left={item['r_left']}, right={item['r_right']}, w={item['r_width']} | display={item['display']}, justify={item['justify']}, mar={item['mar']}, pad={item['pad']}")
else:
    print("Could not find chain in title")
