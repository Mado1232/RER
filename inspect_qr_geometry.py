from PIL import Image, ImageDraw
import numpy as np

# Load our clean square QR
img = Image.open('qr_code_clean_v4.png').convert('RGBA')
w, h = img.size
print('Base QR size:', w, h)

# We want 3 finder patterns:
# In 480x480 image:
# Finder patterns are at:
# 1. Top-Left:
# outer box roughly from (20, 20) to (115, 115)
# 2. Top-Right:
# outer box roughly from (365, 20) to (460, 115)
# 3. Bottom-Left:
# outer box roughly from (20, 365) to (115, 460)

# Let's inspect exact finder pattern coordinates in img
arr = np.array(img.convert('L'))

# Find the exact bounding box of the top-left finder pattern
# It's an isolated block of black in the corner
tl_black = arr[:140, :140] < 128
tl_y, tl_x = np.where(tl_black)
tl_x0, tl_y0 = tl_x.min(), tl_y.min()
tl_x1, tl_y1 = tl_x.max(), tl_y.max()
tl_size = tl_x1 - tl_x0 + 1
print(f'Top-Left finder box: ({tl_x0}, {tl_y0}) to ({tl_x1}, {tl_y1}), size={tl_size}')

# Top-Right finder pattern
tr_black = arr[:140, 340:] < 128
tr_y, tr_x = np.where(tr_black)
tr_x0, tr_y0 = 340 + tr_x.min(), tr_y.min()
tr_x1, tr_y1 = 340 + tr_x.max(), tr_y.max()
tr_size = tr_x1 - tr_x0 + 1
print(f'Top-Right finder box: ({tr_x0}, {tr_y0}) to ({tr_x1}, {tr_y1}), size={tr_size}')

# Bottom-Left finder pattern
bl_black = arr[340:, :140] < 128
bl_y, bl_x = np.where(bl_black)
bl_x0, bl_y0 = bl_x.min(), 340 + bl_y.min()
bl_x1, bl_y1 = bl_x.max(), 340 + bl_y.max()
bl_size = bl_x1 - bl_x0 + 1
print(f'Bottom-Left finder box: ({bl_x0}, {bl_y0}) to ({bl_x1}, {bl_y1}), size={bl_size}')

# Center cat head area
center_black = arr[180:300, 180:300] < 128
cy, cx = np.where(center_black)
cx0, cy0 = 180 + cx.min(), 180 + cy.min()
cx1, cy1 = 180 + cx.max(), 180 + cy.max()
print(f'Center cat head box: ({cx0}, {cy0}) to ({cx1}, {cy1})')
