svg_sticker = """<svg viewBox="0 0 36 36" width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(18, 18) rotate(-4) translate(-18, -18)">
    <!-- Outer White Die-Cut Sticker Outline -->
    <!-- Cat Ear -->
    <path d="M 10 10 L 13.5 2.5 L 18 9 Z" fill="#ffffff" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" />
    <!-- Left Paw -->
    <ellipse cx="4" cy="13" rx="3.5" ry="2.8" fill="#ffffff" stroke="#ffffff" stroke-width="2" />
    <!-- Right Paw -->
    <ellipse cx="30" cy="29" rx="3.5" ry="2.8" fill="#ffffff" stroke="#ffffff" stroke-width="2" />
    <!-- Base Card Outline -->
    <rect x="5" y="7" width="24" height="24" rx="5" fill="#ffffff" stroke="#ffffff" stroke-width="2" />

    <!-- Cat Ear Inner -->
    <path d="M 11.5 9 L 13.5 4.5 L 16.5 8 Z" fill="#1e1b4b" />

    <!-- Black Scanner Card -->
    <rect x="6" y="8" width="22" height="22" rx="4" fill="#111827" />

    <!-- Finder Marker Top-Left -->
    <rect x="8.8" y="10.8" width="5.8" height="5.8" rx="1.3" fill="none" stroke="#ffffff" stroke-width="1.3" />
    <rect x="10.7" y="12.7" width="2" height="2" rx="0.4" fill="#ffffff" />

    <!-- Finder Marker Top-Right -->
    <rect x="18.4" y="10.8" width="5.8" height="5.8" rx="1.3" fill="none" stroke="#ffffff" stroke-width="1.3" />
    <rect x="20.3" y="12.7" width="2" height="2" rx="0.4" fill="#ffffff" />

    <!-- Scanner Frame Bottom-Left -->
    <path d="M 9 21 L 9 24.5 A 1.5 1.5 0 0 0 10.5 26 L 14 26" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="11.8" cy="23" r="1.1" fill="#ffffff" />

    <!-- QR Motif Bottom-Right -->
    <circle cx="19.5" cy="22" r="1.2" fill="#ffffff" />
    <circle cx="22.8" cy="24.5" r="1.2" fill="#ffffff" />
    <line x1="19.5" y1="22" x2="22.8" y2="24.5" stroke="#ffffff" stroke-width="1.1" stroke-linecap="round" />

    <!-- Cat Paws (on top of card edge) -->
    <!-- Left Paw -->
    <g transform="translate(4.5, 12.5) rotate(-18)">
      <ellipse cx="0" cy="0" rx="2.8" ry="2" fill="#ffffff" />
      <path d="M -0.8 -1.5 L 0 0.6 M 1 -1.2 L 1.5 0.7" stroke="#cbd5e1" stroke-width="0.5" stroke-linecap="round" />
    </g>

    <!-- Right Paw -->
    <g transform="translate(29.2, 28.5) rotate(-22)">
      <ellipse cx="0" cy="0" rx="2.8" ry="2" fill="#ffffff" />
      <path d="M -0.8 -1.3 L -0.4 0.6 M 0.9 -1 L 1 0.7" stroke="#cbd5e1" stroke-width="0.5" stroke-linecap="round" />
    </g>
  </g>
</svg>"""

with open('cat_sticker_inline.svg', 'w', encoding='utf-8') as f:
    f.write(svg_sticker)

html = f"""<!DOCTYPE html>
<html>
<body style="background:#f2f4f7; padding:20px;">
  <div style="width:54px; height:54px; border-radius:50%; background:linear-gradient(135deg, #7b2cbf 0%, #ff4b72 100%); border:3px solid #fff; box-shadow:0 4px 14px rgba(123,44,191,0.35); display:flex; align-items:center; justify-content:center;">
    {svg_sticker}
  </div>
</body>
</html>"""

with open('test_sticker_circle.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved test_sticker_circle.html")
