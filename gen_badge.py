svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54 54" width="54" height="54">
  <defs>
    <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF4B72" />
      <stop offset="100%" stop-color="#7B2CBF" />
    </linearGradient>
  </defs>

  <!-- Circular background badge with white border -->
  <circle cx="27" cy="27" r="25.5" fill="url(#badgeGrad)" stroke="#ffffff" stroke-width="3" />

  <!-- The monobank Cat Sticker (white die-cut border) -->
  <g transform="translate(27, 27) rotate(-4) translate(-27, -27)">
    <!-- Outer White Die-Cut Silhouette (sticker outline) -->
    <!-- Ear silhouette -->
    <path d="M 19 14.5 L 22.5 7 L 27 13 Z" fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" />
    <!-- Left paw silhouette -->
    <ellipse cx="13" cy="18" rx="4" ry="3" fill="#ffffff" stroke="#ffffff" stroke-width="2.5" />
    <!-- Right paw silhouette -->
    <ellipse cx="39" cy="34.5" rx="4" ry="3" fill="#ffffff" stroke="#ffffff" stroke-width="2.5" />
    <!-- Card outer white base -->
    <rect x="13.5" y="12.5" width="25" height="25" rx="5.5" fill="#ffffff" stroke="#ffffff" stroke-width="2.5" />

    <!-- Cat inner ear -->
    <path d="M 20.5 13.5 L 22.5 8.5 L 25.5 12.5 Z" fill="#1e1b4b" />

    <!-- Black Scanner Card -->
    <rect x="15" y="14" width="22" height="22" rx="4.2" fill="#111827" />

    <!-- Scanner card graphics (white markings) -->
    <!-- Top-left finder marker -->
    <rect x="17.8" y="16.8" width="6.2" height="6.2" rx="1.5" fill="none" stroke="#ffffff" stroke-width="1.4" />
    <rect x="19.7" y="18.7" width="2.4" height="2.4" rx="0.5" fill="#ffffff" />

    <!-- Top-right finder marker -->
    <rect x="28" y="16.8" width="6.2" height="6.2" rx="1.5" fill="none" stroke="#ffffff" stroke-width="1.4" />
    <rect x="29.9" y="18.7" width="2.4" height="2.4" rx="0.5" fill="#ffffff" />

    <!-- Bottom-left scanner frame -->
    <path d="M 18 27.5 L 18 31.5 A 1.5 1.5 0 0 0 19.5 33 L 23.5 33" fill="none" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="21" cy="29" r="1.2" fill="#ffffff" />

    <!-- Bottom-right QR symbol motif -->
    <circle cx="29" cy="28.5" r="1.4" fill="#ffffff" />
    <circle cx="32.5" cy="31" r="1.4" fill="#ffffff" />
    <line x1="29" y1="28.5" x2="32.5" y2="31" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" />

    <!-- Cat paws clutching the card (on top of card) -->
    <!-- Left paw (top-left edge) -->
    <g transform="translate(13.5, 17.5) rotate(-18)">
      <ellipse cx="0" cy="0" rx="3.2" ry="2.2" fill="#ffffff" />
      <path d="M -1 -1.8 L 0 0.8 M 1.2 -1.5 L 1.8 1" stroke="#cbd5e1" stroke-width="0.6" stroke-linecap="round" />
    </g>

    <!-- Right paw (bottom-right edge) -->
    <g transform="translate(38, 34) rotate(-22)">
      <ellipse cx="0" cy="0" rx="3.2" ry="2.2" fill="#ffffff" />
      <path d="M -1 -1.5 L -0.5 0.8 M 1 -1.2 L 1.2 0.9" stroke="#cbd5e1" stroke-width="0.6" stroke-linecap="round" />
    </g>
  </g>
</svg>"""

with open('cat_badge_v2.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

html = f"""<!DOCTYPE html>
<html>
<body style="background:#f2f4f7; display:flex; gap:30px; align-items:center; padding:30px;">
  <div>
    <div style="font-family:sans-serif; font-size:12px; margin-bottom:6px; color:#555;">New SVG:</div>
    <div style="width:54px; height:54px; display:inline-block;">{svg_content}</div>
  </div>
  <div>
    <div style="font-family:sans-serif; font-size:12px; margin-bottom:6px; color:#555;">Original crop:</div>
    <img src="exact_badge_crop2.png" style="width:54px; height:47px; object-fit:contain; border-radius:50%;" />
  </div>
</body>
</html>"""

with open('test_badge.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Badge SVG generated successfully")
