from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Load our clean square QR
base_img = Image.open('qr_code_clean_v4.png').convert('RGB')
w, h = base_img.size

# We will create an enhanced version
qr = base_img.copy()
draw = ImageDraw.Draw(qr)

# Module size is roughly 17.3 pixels
# 1. Redraw 3 Finder Patterns with rounded corners (squircle style)
finders = [
    (19, 19, 139, 139),     # Top-Left
    (341, 19, 461, 139),   # Top-Right
    (19, 341, 139, 461)    # Bottom-Left
]

for x0, y0, x1, y1 in finders:
    # Clear region with white (plus quiet 1px margin)
    draw.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], fill='#ffffff')
    
    # Outer black rounded rectangle (radius 22px)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill='#000000')
    
    # Inner white rounded rectangle (1 module border = ~17.3px)
    mod = 17.3
    draw.rounded_rectangle([x0 + mod, y0 + mod, x1 - mod, y1 - mod], radius=16, fill='#ffffff')
    
    # Center black rounded square (3 modules = ~52px)
    draw.rounded_rectangle([x0 + mod * 2, y0 + mod * 2, x1 - mod * 2, y1 - mod * 2], radius=10, fill='#000000')

# 2. Redraw Center Cat Head with Sharp Triangular Ears
# Clear center circle
cx, cy = 240, 240
# Cat cutout circle radius 48px
draw.ellipse([cx - 48, cy - 48, cx + 48, cy + 48], fill='#ffffff')

# Draw the black cat head silhouette with distinct, sharp triangular ears
# Points defining the cat silhouette:
# Left ear tip: (213, 195)
# Right ear tip: (267, 195)
# Forehead: curve between (227, 216) and (253, 216)
# Left cheek: around (198, 245)
# Right cheek: around (282, 245)
# Chin: around (240, 276)
cat_poly = [
    (240, 218),  # forehead center
    (229, 216),  # forehead left
    (222, 210),  # inner left ear base
    (212, 194),  # left ear TIP (sharp triangle)
    (203, 220),  # outer left ear base
    (198, 235),  # upper left cheek
    (196, 248),  # left cheek widest
    (202, 262),  # lower left jaw
    (216, 273),  # left chin
    (240, 278),  # bottom chin center
    (264, 273),  # right chin
    (278, 262),  # lower right jaw
    (284, 248),  # right cheek widest
    (282, 235),  # upper right cheek
    (277, 220),  # outer right ear base
    (268, 194),  # right ear TIP (sharp triangle)
    (258, 210),  # inner right ear base
    (251, 216),  # forehead right
]

draw.polygon(cat_poly, fill='#000000')

# Save updated clean QR
qr.save('qr_code_v5_rounded.png')

import base64
with open('qr_code_v5_rounded.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

with open('qr_base64_v5.txt', 'w', encoding='utf-8') as f:
    f.write(f'data:image/png;base64,{b64}')

print('Successfully generated qr_code_v5_rounded.png and qr_base64_v5.txt')
