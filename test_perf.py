html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body { background: #f2f4f7; padding: 40px; display: flex; flex-direction: column; gap: 30px; align-items: center; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.card {
  width: 390px;
  background: #ffffff;
  padding: 20px 0;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}
.ticket-perforation-container {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  height: 22px;
}
.ticket-notch {
  width: 20px;
  height: 20px;
  background: #f2f4f7;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 5;
}
.notch-left {
  left: -10px;
}
.notch-right {
  right: -10px;
}
.ticket-perforation-line {
  flex: 1;
  margin: 0 18px;
  height: 2px;
  display: flex;
  align-items: center;
}
</style>
</head>
<body>
  <div>
    <h3>Perforation implementation:</h3>
    <div class="card">
      <div class="ticket-perforation-container">
        <div class="ticket-notch notch-left"></div>
        <div class="ticket-perforation-line">
          <svg width="100%" height="2" style="display: block;">
            <line x1="0" y1="1" x2="100%" y2="1" stroke="#D1D5DB" stroke-width="1.8" stroke-dasharray="8 7" />
          </svg>
        </div>
        <div class="ticket-notch notch-right"></div>
      </div>
    </div>
  </div>
  <div>
    <h3>Reference crop:</h3>
    <img src="original_perf_ref.png" style="width: 390px; height: auto;" />
  </div>
</body>
</html>"""

with open('test_perf.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved test_perf.html")
