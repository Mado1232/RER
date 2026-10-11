# Refined vector sticker matching ref_sticker_detail.png
# Total SVG size 60x60, sticker centered and filling 42x46

svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%" fill="none">
  <!-- Tilted sticker group -->
  <g transform="translate(32, 33) rotate(-3) translate(-32, -33)">
    
    <!-- 1. White die-cut outline (Silhouette layer) -->
    <!-- Left ear silhouette -->
    <path d="M 21 17 L 27 5 C 27.8 3.5 29.5 3.5 30.2 5 L 35 15 Z" fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" />
    <!-- Right ear silhouette -->
    <path d="M 34 14 L 40 8.5 C 41 7.5 42.5 8 43 9.5 L 45 16 Z" fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" />
    
    <!-- Left paw silhouette (clutching top-left) -->
    <path d="M 16 23 C 13.5 24.5 13 28 15 31 C 16.5 33 19 33.5 22 33 L 22 22 Z" fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" />
    
    <!-- Bottom-right paw silhouette (clutching bottom-right) -->
    <path d="M 43 43 L 44 49 C 45 52 48 53 50.5 50.5 C 52 49 52 46 50 44 L 45 42 Z" fill="#ffffff" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" />
    
    <!-- Card silhouette (white outline) -->
    <rect x="17" y="15" width="31" height="31" rx="7" fill="#ffffff" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round" />

    <!-- 2. Cat ears inner lines and head -->
    <!-- Left ear inside -->
    <path d="M 27 7.5 L 29.5 15 L 33 13.5 Z" fill="#111827" />
    <path d="M 26.5 7 L 29 14.5" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" />

    <!-- 3. Black card body -->
    <rect x="18" y="16" width="29" height="29" rx="5.5" fill="#111827" />

    <!-- 4. White paws overlaying card with finger notches -->
    <!-- Left paw (3 rounded pads) -->
    <path d="M 15 25 C 14 26 14.5 28 16 28.5 C 17.5 29 18.5 27.5 18 26 Z" fill="#ffffff" />
    <path d="M 16 28.5 C 15.5 29.8 16.5 31 18 31 C 19.5 31 20 29.5 19.5 28.5 Z" fill="#ffffff" />
    <path d="M 17 23.5 C 16 24 16 25.5 17.5 26 C 19 26.5 20 25 19.5 24 Z" fill="#ffffff" />
    <!-- Paw base -->
    <circle cx="17" cy="27" r="3.2" fill="#ffffff" />
    <path d="M 15.5 25.5 L 18 26.5 M 16.5 28.5 L 19 29" stroke="#cbd5e1" stroke-width="0.7" stroke-linecap="round" />

    <!-- Bottom-right paw (3 rounded pads) -->
    <circle cx="47" cy="46" r="3.2" fill="#ffffff" />
    <path d="M 45 44 C 44.5 43 46 42 47 43 C 48 44 47.5 45.5 46.5 45 Z" fill="#ffffff" />
    <path d="M 47.5 43.5 C 48.5 43 49.8 44 49.5 45.5 C 49.2 46.8 48 47 47 46 Z" fill="#ffffff" />
    <path d="M 46.5 47 C 47.5 47.5 48.5 49 47 49.8 C 45.8 50.2 45 48.8 45.5 47.8 Z" fill="#ffffff" />
    <path d="M 46 44 L 47 45.5 M 47 47 L 46 48.5" stroke="#cbd5e1" stroke-width="0.7" stroke-linecap="round" />

    <!-- 5. Scanner UI elements on the card -->
    <!-- Viewfinder corners [ ] -->
    <path d="M 23 20.5 L 21.5 20.5 C 20.7 20.5 20.2 21 20.2 21.8 L 20.2 23" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M 42 20.5 L 43.5 20.5 C 44.3 20.5 44.8 21 44.8 21.8 L 44.8 23" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M 20.2 38 L 20.2 39.2 C 20.2 40 20.7 40.5 21.5 40.5 L 23 40.5" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M 44.8 38 L 44.8 39.2 C 44.8 40 44.3 40.5 43.5 40.5 L 42 40.5" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />

    <!-- 4 QR pattern blocks -->
    <!-- Top-left square -->
    <rect x="22.5" y="22.5" width="6.8" height="6.8" rx="1.5" fill="none" stroke="#ffffff" stroke-width="1.5" />
    <!-- Top-right square -->
    <rect x="33.5" y="22.5" width="6.8" height="6.8" rx="1.5" fill="none" stroke="#ffffff" stroke-width="1.5" />
    <!-- Bottom-left square -->
    <rect x="22.5" y="31.8" width="6.8" height="6.8" rx="1.5" fill="none" stroke="#ffffff" stroke-width="1.5" />
    <!-- Bottom-right: percent mark -->
    <g transform="translate(34, 32)">
      <circle cx="2" cy="2" r="1.3" fill="none" stroke="#ffffff" stroke-width="1.2" />
      <line x1="5.2" y1="1.4" x2="1.4" y2="5.6" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" />
      <circle cx="4.8" cy="5" r="1.3" fill="none" stroke="#ffffff" stroke-width="1.2" />
    </g>
  </g>
</svg>'''

with open('cat_badge.svg', 'w', encoding='utf-8') as f:
    f.write(svg_code)

print('Updated cat_badge.svg')
