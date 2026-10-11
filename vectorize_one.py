import numpy as np
from PIL import Image, ImageDraw

# Load user cropped image
img_orig = Image.open('C:/Users/Admin/.gemini/antigravity/brain/18c7e0a4-71bc-4cb2-954e-ac526294117a/.user_uploaded/media_1791660741518.png').convert('L')
arr_orig = np.array(img_orig)
mask = arr_orig < 160
y_idx, x_idx = np.where(mask)
orig_crop = arr_orig[y_idx.min():y_idx.max()+1, x_idx.min():x_idx.max()+1]
h, w = orig_crop.shape
print(f"Original crop: width={w}, height={h}")

# We want an exact polygon that minimizes the difference with orig_crop
# Let's inspect points:
# The stem width is about 7px.
# Stem right: x ≈ 18.8
# Stem left: x ≈ 11.6
# Top: y = 0
# Bottom of foot: y = 44.5
# Top of foot: y = 39.5
# Left of foot: x = 2.4
# Right of foot: x = 26.6

# Beak:
# Let's test a parameterized polygon:
# P0: (top_beak_x, 0)
# P1: (stem_r, 0)
# P2: (stem_r, foot_t)
# P3: (foot_r, foot_t)
# P4: (foot_r, foot_b)
# P5: (foot_l, foot_b)
# P6: (foot_l, foot_t)
# P7: (stem_l, foot_t)
# P8: (stem_l, beak_inner_y)
# P9: (beak_under_x, beak_under_y)
# P10: (beak_tip_x, beak_tip_b)
# P11: (beak_tip_x, beak_tip_t)

best_diff = 1e9
best_params = None

scale = 8
# Let's fine tune using optimization or grid search
for top_beak_x in [11.8, 12.2, 12.6, 13.0]:
    for beak_tip_t in [10.5, 11.0, 11.5]:
        for beak_tip_b in [13.0, 13.5, 14.0]:
            for beak_under_x, beak_under_y in [(2.5, 15.5), (3.0, 15.8), (3.5, 16.0), (3.0, 16.5), (2.0, 15.0)]:
                for beak_inner_y in [10.5, 11.0, 11.5, 12.0]:
                    poly = [
                        (top_beak_x * scale, 0.0 * scale),
                        (18.8 * scale, 0.0 * scale),
                        (18.8 * scale, 39.5 * scale),
                        (26.6 * scale, 39.5 * scale),
                        (26.6 * scale, 44.5 * scale),
                        (2.4 * scale, 44.5 * scale),
                        (2.4 * scale, 39.5 * scale),
                        (11.6 * scale, 39.5 * scale),
                        (11.6 * scale, beak_inner_y * scale),
                        (beak_under_x * scale, beak_under_y * scale),
                        (0.5 * scale, beak_tip_b * scale),
                        (0.5 * scale, beak_tip_t * scale),
                    ]
                    # Render on high-res canvas
                    canvas = Image.new('L', (w * scale, h * scale), 255)
                    draw = ImageDraw.Draw(canvas)
                    draw.polygon(poly, fill=0)
                    rendered = canvas.resize((w, h), Image.Resampling.LANCZOS)
                    arr_ren = np.array(rendered)
                    diff = np.mean(np.abs(arr_ren.astype(float) - orig_crop.astype(float)))
                    if diff < best_diff:
                        best_diff = diff
                        best_params = (top_beak_x, beak_tip_t, beak_tip_b, beak_under_x, beak_under_y, beak_inner_y)

print("Best diff:", best_diff)
print("Best params:", best_params)
top_beak_x, beak_tip_t, beak_tip_b, beak_under_x, beak_under_y, beak_inner_y = best_params

# Save comparison image
poly = [
    (top_beak_x * scale, 0.0 * scale),
    (18.8 * scale, 0.0 * scale),
    (18.8 * scale, 39.5 * scale),
    (26.6 * scale, 39.5 * scale),
    (26.6 * scale, 44.5 * scale),
    (2.4 * scale, 44.5 * scale),
    (2.4 * scale, 39.5 * scale),
    (11.6 * scale, 39.5 * scale),
    (11.6 * scale, beak_inner_y * scale),
    (beak_under_x * scale, beak_under_y * scale),
    (0.5 * scale, beak_tip_b * scale),
    (0.5 * scale, beak_tip_t * scale),
]
canvas = Image.new('L', (w * scale, h * scale), 255)
draw = ImageDraw.Draw(canvas)
draw.polygon(poly, fill=0)
rendered = canvas.resize((w, h), Image.Resampling.LANCZOS)

# Create comparison image: [orig_crop, rendered, diff*3]
comp = Image.new('L', (w * 3 + 10, h), 255)
comp.paste(Image.fromarray(orig_crop), (0, 0))
comp.paste(rendered, (w + 5, 0))
diff_arr = np.clip(np.abs(np.array(rendered).astype(float) - orig_crop.astype(float)) * 3, 0, 255).astype(np.uint8)
comp.paste(Image.fromarray(diff_arr), (w * 2 + 10, 0))
comp.resize(((w * 3 + 10) * 4, h * 4), Image.Resampling.NEAREST).save('compare_one.png')
print("Saved compare_one.png")

# Generate SVG
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <polygon points="{top_beak_x:.1f},0 18.8,0 18.8,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 11.6,39.5 11.6,{beak_inner_y:.1f} {beak_under_x:.1f},{beak_under_y:.1f} 0.5,{beak_tip_b:.1f} 0.5,{beak_tip_t:.1f}" fill="currentColor" />
</svg>"""
with open('digit_one.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print("SVG points:", f"{top_beak_x:.1f},0 18.8,0 18.8,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 11.6,39.5 11.6,{beak_inner_y:.1f} {beak_under_x:.1f},{beak_under_y:.1f} 0.5,{beak_tip_b:.1f} 0.5,{beak_tip_t:.1f}")
