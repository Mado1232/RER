import base64, os, subprocess

with open('cat_sticker_base64.txt', 'r', encoding='utf-8') as f:
    cat_sticker_b64 = f.read().strip()

with open('qr_base64_v4.txt', 'r', encoding='utf-8') as f:
    qr_b64 = f.read().strip()

html = f'''<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>V4 Pixel-Perfect Ticket Test</title>
<style>
:root {{
  --bg-page: #f2f4f7;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Helvetica, Arial, sans-serif;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

body {{
  background: var(--bg-page);
  font-family: var(--font-sans);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 12px 10px 48px;
  overflow-x: hidden;
}}

/* Ticket Container */
.ticket-card-wrapper {{
  position: relative;
  width: calc(100% - 10px);
  max-width: 410px;
  margin: 0 auto;
  padding-top: 44px;
}}

/* DEMO Badge on upper-left to never block Info button */
.demo-corner-badge {{
  position: absolute;
  top: 14px;
  left: 10px;
  z-index: 30;
  background: #dc2626;
  color: #ffffff;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.6px;
  padding: 3px 8px;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(220, 38, 38, 0.35);
  display: flex;
  align-items: center;
  gap: 5px;
}}
.demo-badge-dot {{
  width: 5px;
  height: 5px;
  background: #fff;
  border-radius: 50%;
}}

/* Top Info Button ⓘ in upper-right */
.ticket-top-info-btn {{
  position: absolute;
  top: 12px;
  right: 12px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 1.5px solid #9ca3af;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
  font-family: serif;
  font-size: 13px;
  font-weight: 600;
  font-style: italic;
  background: transparent;
  cursor: pointer;
  z-index: 20;
}}

/* Mascot Badge Anchor & Badge */
.ticket-top-emblem-container {{
  position: absolute;
  top: 3px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}}

.ticket-top-emblem {{
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(135deg, #9a55d1 0%, #e02874 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 14px rgba(123, 44, 191, 0.28);
  border: 3.5px solid #ffffff;
}}

.ticket-sticker-img {{
  width: 42px;
  height: 46px;
  object-fit: contain;
}}

/* White Ticket Body */
.ticket-card-body {{
  background: #ffffff;
  border-radius: 26px 26px 0 0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  padding: 24px 0 0 0;
  position: relative;
}}

/* Notch Cutout */
.ticket-notch-cutout-container {{
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 106px;
  height: 28px;
  z-index: 3;
  pointer-events: none;
}}

.ticket-notch-svg {{
  width: 100%;
  height: 100%;
  display: block;
}}

/* Blue Marquee Ticker */
.ticket-ticker-strip {{
  background: #ebf5fb;
  color: #0284c7;
  padding: 7px 0;
  overflow: hidden;
  white-space: nowrap;
  margin-top: 10px;
  margin-bottom: 14px;
  position: relative;
  border-top: 1px solid #e0f0fa;
  border-bottom: 1px solid #e0f0fa;
}}

.ticker-track {{
  display: inline-flex;
  white-space: nowrap;
  animation: marquee-smooth 24s linear infinite;
}}

@keyframes marquee-smooth {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(-50%); }}
}}

.ticker-item {{
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.1px;
  padding: 0 16px;
}}

/* Header «Тролейбус» */
.ticket-header {{
  text-align: center;
  padding: 0 16px;
}}

.ticket-title {{
  font-size: 19px;
  font-weight: 600;
  color: #111827;
  letter-spacing: -0.2px;
}}

/* Horizontal Hairline separator under «Тролейбус» */
.ticket-hairline {{
  width: 130px;
  height: 1px;
  background: #e5e7eb;
  margin: 8px auto 0;
}}

/* Purchase string */
.ticket-purchase-time {{
  text-align: center;
  color: #6b7280;
  font-size: 14.5px;
  font-weight: 400;
  margin-top: 14px;
}}

/* «1 квиток» */
.ticket-quantity {{
  text-align: center;
  font-size: 38px;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.025em;
  margin-top: 6px;
  line-height: 1.1;
}}

/* Validity pill */
.ticket-validity-pill-wrapper {{
  display: flex;
  justify-content: center;
  margin-top: 12px;
}}

.ticket-validity-pill {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(90deg, #d7f5e4 0%, #d8edfb 100%);
  padding: 7px 22px;
  border-radius: 9999px;
}}

.validity-indicator-circle {{
  width: 13px;
  height: 13px;
  border-radius: 50%;
  border: 1.5px solid #34d399;
  background: transparent;
  display: inline-block;
  flex-shrink: 0;
}}

.validity-text {{
  font-size: 15.5px;
  font-weight: 600;
  color: #1f2937;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.1px;
}}

/* «Тролейбус № 375» */
.ticket-transport-line {{
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 7px;
  margin-top: 22px;
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
  letter-spacing: 0.02em;
  font-variant-numeric: tabular-nums;
}}

.number-sign-glyph {{
  font-weight: 700;
  margin-right: 2px;
}}

/* Perforation */
.ticket-perforation-container {{
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  height: 22px;
  margin-bottom: 14px;
}}

.ticket-notch {{
  width: 21px;
  height: 21px;
  background: #f2f4f7;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 5;
}}

.notch-left {{
  left: -10.5px;
}}

.notch-right {{
  right: -10.5px;
}}

.ticket-perforation-dashed {{
  flex: 1;
  margin: 0 16px;
  height: 2px;
  display: flex;
  align-items: center;
}}

/* QR Code Section */
.ticket-lower-section {{
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  padding: 4px 16px 14px;
}}

.ticket-qr-card {{
  background: #ffffff;
  border-radius: 26px;
  padding: 12px;
  box-shadow: 0 3px 16px rgba(0, 0, 0, 0.04);
  border: 1px solid #f3f4f6;
  display: inline-block;
  position: relative;
  z-index: 2;
  line-height: 0;
}}

.qr-image-asset {{
  display: block;
  width: 240px;
  height: 240px;
  object-fit: contain;
  border-radius: 12px;
}}

/* Ticket ID line */
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
  font-weight: 700;
  color: #111827;
  letter-spacing: 0.5px;
}}

/* Bottom scalloped edge */
.ticket-scallop-edge {{
  height: 14px;
  background: radial-gradient(circle at 10px -3px, transparent 10px, #ffffff 10.5px);
  background-size: 20px 14px;
  background-repeat: repeat-x;
  width: 100%;
}}

.ticket-reopen-note {{
  text-align: center;
  color: #9ca3af;
  font-size: 13px;
  margin-top: 14px;
  padding: 0 16px;
}}
</style>
</head>
<body>

<div class="ticket-card-wrapper">
  <!-- DEMO Badge -->
  <div class="demo-corner-badge">
    <span class="demo-badge-dot"></span>
    ЗРАЗОК / DEMO
  </div>

  <!-- Info Button ⓘ -->
  <button class="ticket-top-info-btn" title="Інформація про квиток">i</button>

  <!-- Mascot Badge -->
  <div class="ticket-top-emblem-container">
    <div class="ticket-top-emblem" title="monobank mascot">
      <img src="{cat_sticker_b64}" class="ticket-sticker-img" alt="monobank cat">
    </div>
  </div>

  <!-- Ticket Body -->
  <div class="ticket-card-body">
    <!-- Notch cutout -->
    <div class="ticket-notch-cutout-container">
      <svg viewBox="0 0 106 28" className="ticket-notch-svg" preserveAspectRatio="none">
        <path d="M 0 0 L 12 0 C 20 0 26 3 31 8 C 37 16 44 24 53 24 C 62 24 69 16 75 8 C 80 3 86 0 94 0 L 106 0 Z" fill="#f2f4f7" />
      </svg>
    </div>

    <!-- Blue Marquee Strip -->
    <div class="ticket-ticker-strip">
      <div class="ticker-track">
        <span class="ticker-item">Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі &nbsp; ◆ &nbsp;</span>
        <span class="ticker-item">Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі &nbsp; ◆ &nbsp;</span>
      </div>
    </div>

    <!-- Header «Тролейбус» -->
    <div class="ticket-header">
      <h2 class="ticket-title">Тролейбус</h2>
      <div class="ticket-hairline"></div>
    </div>

    <!-- Purchase String -->
    <div class="ticket-purchase-time">
      Придбано 29 вересня о 13:32
    </div>

    <!-- «1 квиток» -->
    <div class="ticket-quantity">
      1 квиток
    </div>

    <!-- Validity pill -->
    <div class="ticket-validity-pill-wrapper">
      <div class="ticket-validity-pill">
        <span class="validity-indicator-circle"></span>
        <span class="validity-text">
          Квиток дійсний — 59:55
        </span>
      </div>
    </div>

    <!-- «Тролейбус № 375» -->
    <div class="ticket-transport-line">
      <span class="transport-label">Тролейбус</span>
      <span class="transport-number"><span class="number-sign-glyph">№</span> 375</span>
    </div>

    <!-- Perforation line -->
    <div class="ticket-perforation-container">
      <div class="ticket-notch notch-left"></div>
      <div class="ticket-perforation-dashed">
        <svg width="100%" height="2" style="display: block;">
          <line x1="0" y1="1" x2="100%" y2="1" stroke="#D1D5DB" stroke-width="1.5" stroke-dasharray="8.5 8" stroke-linecap="butt" />
        </svg>
      </div>
      <div class="ticket-notch notch-right"></div>
    </div>

    <!-- Lower Section: QR Code -->
    <div class="ticket-lower-section">
      <div class="ticket-qr-card">
        <img src="{qr_b64}" class="qr-image-asset" alt="QR Code">
      </div>

      <div class="ticket-id-line">
        <span class="ticket-id-label">Номер:</span>
        <span class="ticket-id-value">612 121</span>
      </div>
    </div>

    <!-- Bottom Scallop Edge -->
    <div class="ticket-scallop-edge"></div>
  </div>

  <div class="ticket-reopen-note">
    Ви зможете повторно відкрити цю сторінку пізніше
  </div>
</div>

</body>
</html>
'''

with open('test_full_v4.html', 'w', encoding='utf-8') as f:
    f.write(html)

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out_path = r'C:\Users\Admin\.gemini\antigravity\scratch\trolleybus-ticket-editor\prototype_v4.png'
in_path = os.path.abspath('test_full_v4.html')

subprocess.run([
    edge_path,
    '--headless',
    '--disable-gpu',
    f'--screenshot={out_path}',
    '--window-size=430,940',
    in_path
])

# Also recreate comparison
ref = Image.open('original_ref_full.png')
v4 = Image.open('prototype_v4.png')
rw, rh = ref.size
vw, vh = v4.size
ref_scaled = ref.resize((int(rw * 940 / rh), 940), Image.Resampling.LANCZOS)
cmp_img = Image.new('RGB', (ref_scaled.width + vw + 20, 940), (230, 233, 238))
cmp_img.paste(v4, (0, 0))
cmp_img.paste(ref_scaled, (vw + 20, 0))
cmp_img.save('side_by_side_v4_cmp.png')
print('Updated side_by_side_v4_cmp.png')
