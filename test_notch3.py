html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body { background: #f2f4f7; padding: 40px; display: flex; justify-content: center; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.card-wrapper {
  position: relative;
  width: 390px;
  filter: drop-shadow(0 4px 20px rgba(0,0,0,0.06));
}
.badge {
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(145deg, #e02874 0%, #7b2cbf 100%);
  border: 3.5px solid #ffffff;
  box-shadow: 0 4px 14px rgba(123, 44, 191, 0.35);
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
}
.card {
  background: #ffffff;
  border-radius: 28px 28px 0 0;
  padding: 38px 0 20px;
  position: relative;
  overflow: hidden;
}
.notch-svg-container {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 84px;
  height: 32px;
  z-index: 3;
  pointer-events: none;
}
.notch-svg {
  width: 100%;
  height: 100%;
  display: block;
}
.ticker {
  background: #ebf5fb;
  color: #0284c7;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  text-align: center;
}
</style>
</head>
<body>
  <div class="card-wrapper">
    <div class="badge">
      <svg viewBox="0 0 36 36" width="34" height="34" fill="none">
        <g transform="translate(18, 18) rotate(-4) translate(-18, -18)">
          <path d="M 10 10 L 13.5 2.5 L 18 9 Z" fill="#ffffff" stroke="#ffffff" stroke-width="2.5" stroke-linejoin="round" />
          <ellipse cx="4" cy="13" rx="3.5" ry="2.8" fill="#ffffff" stroke="#ffffff" stroke-width="2" />
          <ellipse cx="30" cy="29" rx="3.5" ry="2.8" fill="#ffffff" stroke="#ffffff" stroke-width="2" />
          <rect x="5" y="7" width="24" height="24" rx="5" fill="#ffffff" stroke="#ffffff" stroke-width="2" />
          <path d="M 11.5 9 L 13.5 4.5 L 16.5 8 Z" fill="#1e1b4b" />
          <rect x="6" y="8" width="22" height="22" rx="4" fill="#111827" />
          <rect x="8.8" y="10.8" width="5.8" height="5.8" rx="1.3" fill="none" stroke="#ffffff" stroke-width="1.3" />
          <rect x="10.7" y="12.7" width="2" height="2" rx="0.4" fill="#ffffff" />
          <rect x="18.4" y="10.8" width="5.8" height="5.8" rx="1.3" fill="none" stroke="#ffffff" stroke-width="1.3" />
          <rect x="20.3" y="12.7" width="2" height="2" rx="0.4" fill="#ffffff" />
          <path d="M 9 21 L 9 24.5 A 1.5 1.5 0 0 0 10.5 26 L 14 26" fill="none" stroke="#ffffff" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
          <circle cx="11.8" cy="23" r="1.1" fill="#ffffff" />
          <circle cx="19.5" cy="22" r="1.2" fill="#ffffff" />
          <circle cx="22.8" cy="24.5" r="1.2" fill="#ffffff" />
          <line x1="19.5" y1="22" x2="22.8" y2="24.5" stroke="#ffffff" stroke-width="1.1" stroke-linecap="round" />
          <g transform="translate(4.5, 12.5) rotate(-18)">
            <ellipse cx="0" cy="0" rx="2.8" ry="2" fill="#ffffff" />
            <path d="M -0.8 -1.5 L 0 0.6 M 1 -1.2 L 1.5 0.7" stroke="#cbd5e1" stroke-width="0.5" stroke-linecap="round" />
          </g>
          <g transform="translate(29.2, 28.5) rotate(-22)">
            <ellipse cx="0" cy="0" rx="2.8" ry="2" fill="#ffffff" />
            <path d="M -0.8 -1.3 L -0.4 0.6 M 0.9 -1 L 1 0.7" stroke="#cbd5e1" stroke-width="0.5" stroke-linecap="round" />
          </g>
        </g>
      </svg>
    </div>
    <div class="card">
      <div class="notch-svg-container">
        <svg viewBox="0 0 84 32" class="notch-svg" preserveAspectRatio="none">
          <path d="M 0 0 C 4 0 7 2 9 6 C 16 19 28 29 42 29 C 56 29 68 19 75 6 C 77 2 80 0 84 0 Z" fill="#f2f4f7" />
        </svg>
      </div>
      <div class="ticker">Життя — цікаве, і мотивація то є сильн ◆ залишайтеся</div>
    </div>
  </div>
</body>
</html>"""

with open('test_notch3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved test_notch3.html")
