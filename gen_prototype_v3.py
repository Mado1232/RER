import base64

# Read authentic QR code base64 from file
with open('qr_base64.txt', 'r', encoding='utf-8') as f:
    qr_base64 = f.read().strip()

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root {{
  --bg-page: #f2f4f7;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  background: var(--bg-page);
  font-family: var(--font-sans);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 16px 10px 48px;
  overflow-x: hidden;
}}

.ticket-wrapper {{
  position: relative;
  width: calc(100% - 10px);
  max-width: 410px;
  margin: 0 auto;
}}

/* Red DEMO badge */
.demo-badge {{
  position: absolute;
  top: -12px;
  right: 6px;
  z-index: 30;
  background: #dc2626;
  color: #ffffff;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.6px;
  padding: 3px 9px;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(220, 38, 38, 0.35);
  display: flex;
  align-items: center;
  gap: 5px;
}}
.demo-dot {{
  width: 5px;
  height: 5px;
  background: #fff;
  border-radius: 50%;
}}

/* Top Mascot Badge */
.top-badge-container {{
  position: absolute;
  top: -27px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}}

.top-badge {{
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(145deg, #e02874 0%, #7b2cbf 100%);
  border: 3.5px solid #ffffff;
  box-shadow: 0 4px 14px rgba(123, 44, 191, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
}}

/* Card Body */
.card-body {{
  background: #ffffff;
  border-radius: 28px 28px 0 0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  padding: 36px 0 0 0;
  position: relative;
}}

/* Concave Notch Cutout */
.notch-cutout-container {{
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 86px;
  height: 32px;
  z-index: 3;
  pointer-events: none;
}}
.notch-svg {{
  width: 100%;
  height: 100%;
  display: block;
}}

/* Marquee Ticker Strip */
.ticker-strip {{
  background: #ebf5fb;
  color: #0284c7;
  padding: 7.5px 0;
  overflow: hidden;
  white-space: nowrap;
  margin-bottom: 14px;
  border-top: 1px solid #e0f0fa;
  border-bottom: 1px solid #e0f0fa;
}}
.ticker-track {{
  display: inline-flex;
  white-space: nowrap;
  animation: marquee 20s linear infinite;
}}
@keyframes marquee {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(-50%); }}
}}
.ticker-text {{
  font-size: 13px;
  font-weight: 500;
  padding: 0 16px;
}}

/* Header Тролейбус */
.ticket-header {{
  text-align: center;
  padding: 2px 16px 0;
}}
.ticket-title {{
  font-size: 19px;
  font-weight: 600;
  color: #111827;
  letter-spacing: -0.2px;
}}
.ticket-hairline {{
  width: 160px;
  height: 1px;
  background: #edf0f5;
  margin: 10px auto 0;
}}

/* Purchase info */
.purchase-time {{
  text-align: center;
  color: #6b7280;
  font-size: 14.5px;
  font-weight: 400;
  margin-top: 14px;
}}

/* 1 квиток */
.ticket-qty {{
  text-align: center;
  font-size: 38px;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.025em;
  margin-top: 6px;
  line-height: 1.1;
}}

/* Validity pill */
.validity-pill-wrapper {{
  display: flex;
  justify-content: center;
  margin-top: 12px;
}}
.validity-pill {{
  display: inline-flex;
  align-items: center;
  gap: 9px;
  background: linear-gradient(90deg, #d4f4e2 0%, #dceefb 100%);
  padding: 8px 24px;
  border-radius: 9999px;
}}
.validity-circle {{
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2px solid #16a34a;
}}
.validity-text {{
  font-size: 15.5px;
  font-weight: 600;
  color: #065f46;
  font-variant-numeric: tabular-nums;
}}

/* Transport line */
.transport-line {{
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 7px;
  margin-top: 16px;
  margin-bottom: 22px;
}}
.transport-label {{
  font-size: 18px;
  font-weight: 500;
  color: #6b7280;
}}
.transport-number {{
  font-size: 27px;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.01em;
}}

/* Perforation with side notches */
.perforation-container {{
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  height: 22px;
  margin-bottom: 14px;
}}
.notch {{
  width: 20px;
  height: 20px;
  background: var(--bg-page);
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 5;
}}
.notch-left {{ left: -10px; }}
.notch-right {{ right: -10px; }}
.perforation-line {{
  flex: 1;
  margin: 0 16px;
  height: 2px;
  display: flex;
  align-items: center;
}}

/* QR Code Section */
.qr-section {{
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  padding: 4px 16px 14px;
}}
.qr-watermark {{
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-18deg);
  font-size: 26px;
  font-weight: 900;
  color: rgba(156, 163, 175, 0.12);
  pointer-events: none;
  white-space: nowrap;
  letter-spacing: 2px;
  z-index: 1;
}}
.qr-card {{
  background: #ffffff;
  border-radius: 22px;
  padding: 12px;
  box-shadow: 0 3px 16px rgba(0, 0, 0, 0.04);
  border: 1px solid #f3f4f6;
  display: inline-block;
  position: relative;
  z-index: 2;
  line-height: 0;
}}
.qr-image {{
  display: block;
  width: 240px;
  height: 240px;
  object-fit: contain;
  border-radius: 14px;
}}

/* Ticket ID */
.ticket-id-line {{
  display: flex;
  align-items: center;
  gap: 7px;
  margin-top: 15px;
  font-size: 16px;
}}
.ticket-id-label {{
  color: #6b7280;
  font-weight: 400;
}}
.ticket-id-value {{
  color: #111827;
  font-weight: 700;
}}

/* Scalloped edge */
.scallop-bottom {{
  line-height: 0;
  width: 100%;
  margin-top: 8px;
}}
.scallop-svg {{
  width: 100%;
  height: 10px;
  display: block;
}}

/* External footer */
.external-footer {{
  text-align: center;
  font-size: 13px;
  color: #9ca3af;
  margin-top: 18px;
  line-height: 1.4;
}}
</style>
</head>
<body>
  <div class="ticket-wrapper">
    <div class="demo-badge">
      <span class="demo-dot"></span>
      ЗРАЗОК / DEMO
    </div>

    <!-- Top Mascot Badge -->
    <div class="top-badge-container">
      <div class="top-badge" title="monobank mascot">
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
    </div>

    <!-- White Ticket Body -->
    <div class="card-body">
      <!-- Concave Notch in card -->
      <div class="notch-cutout-container">
        <svg viewBox="0 0 86 32" class="notch-svg" preserveAspectRatio="none">
          <path d="M 0 0 C 4 0 7 2 9 6 C 16 19 28 29 43 29 C 58 29 70 19 77 6 C 79 2 82 0 86 0 Z" fill="#f2f4f7" />
        </svg>
      </div>

      <!-- Ticker Strip -->
      <div class="ticker-strip">
        <div class="ticker-track">
          <span class="ticker-text">Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі &nbsp; ◆ &nbsp;</span>
          <span class="ticker-text">Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі &nbsp; ◆ &nbsp;</span>
        </div>
      </div>

      <!-- Title -->
      <div class="ticket-header">
        <h2 class="ticket-title">Тролейбус</h2>
        <div class="ticket-hairline"></div>
      </div>

      <!-- Purchase Date & Time -->
      <div class="purchase-time">
        Придбано 29 вересня о 13:32
      </div>

      <!-- 1 квиток -->
      <div class="ticket-qty">
        1 квиток
      </div>

      <!-- Validity Pill -->
      <div class="validity-pill-wrapper">
        <div class="validity-pill">
          <span class="validity-circle"></span>
          <span class="validity-text">Квиток дійсний — 59:55</span>
        </div>
      </div>

      <!-- Transport Line -->
      <div class="transport-line">
        <span class="transport-label">Тролейбус</span>
        <span class="transport-number">№ 375</span>
      </div>

      <!-- Perforation Line with Side Notches -->
      <div class="perforation-container">
        <div class="notch notch-left"></div>
        <div class="perforation-line">
          <svg width="100%" height="2" style="display: block;">
            <line x1="0" y1="1" x2="100%" y2="1" stroke="#D1D5DB" stroke-width="1.8" stroke-dasharray="8 7" />
          </svg>
        </div>
        <div class="notch notch-right"></div>
      </div>

      <!-- Lower QR Section -->
      <div class="qr-section">
        <div class="qr-watermark">ЗРАЗОК • DEMO</div>
        <div class="qr-card">
          <img src="{qr_base64}" class="qr-image" alt="QR Code" width="240" height="240" />
        </div>
        <div class="ticket-id-line">
          <span class="ticket-id-label">Номер:</span>
          <span class="ticket-id-value">612 121</span>
        </div>
      </div>

      <!-- Scalloped bottom -->
      <div class="scallop-bottom">
        <svg viewBox="0 0 360 10" width="100%" height="10" preserveAspectRatio="none" class="scallop-svg">
          <path d="M 0 0 C 4.0 8 16.0 8 20.0 0 C 24.0 8 36.0 8 40.0 0 C 44.0 8 56.0 8 60.0 0 C 64.0 8 76.0 8 80.0 0 C 84.0 8 96.0 8 100.0 0 C 104.0 8 116.0 8 120.0 0 C 124.0 8 136.0 8 140.0 0 C 144.0 8 156.0 8 160.0 0 C 164.0 8 176.0 8 180.0 0 C 184.0 8 196.0 8 200.0 0 C 204.0 8 216.0 8 220.0 0 C 224.0 8 236.0 8 240.0 0 C 244.0 8 256.0 8 260.0 0 C 264.0 8 276.0 8 280.0 0 C 284.0 8 296.0 8 300.0 0 C 304.0 8 316.0 8 320.0 0 C 324.0 8 336.0 8 340.0 0 C 344.0 8 356.0 8 360.0 0 L 360 0 L 0 0 Z" fill="#ffffff" />
        </svg>
      </div>
    </div>

    <!-- External footer -->
    <div class="external-footer">
      Ви зможете повторно відкрити цю сторінку пізніше
    </div>
  </div>
</body>
</html>"""

with open('test_full_ticket_v3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved test_full_ticket_v3.html")
