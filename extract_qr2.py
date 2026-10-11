from PIL import Image
import numpy as np

img = Image.open('qr_card_full_user1.png').convert('RGB')
arr = np.array(img)

# QR code finder patterns:
# Top-left finder pattern is around x=70..115, y=40..85
# Bottom-left finder pattern is around x=70..115, y=210..260
# Let's find black pixels in the region y < 275
black = (arr[:,:,0] < 80) & (arr[:,:,1] < 80) & (arr[:,:,2] < 80)
# zero out below y=280
black[280:, :] = False

y_idx, x_idx = np.where(black)
min_y, max_y = y_idx.min(), y_idx.max()
min_x, max_x = x_idx.min(), x_idx.max()

print(f'Actual QR bounding box: x=[{min_x}, {max_x}] (w={max_x - min_x + 1}), y=[{min_y}, {max_y}] (h={max_y - min_y + 1})')

# The QR is w=227, h=227! It's a PERFECT SQUARE!
# Add 10px white margin all around
pad = 10
qr_box = img.crop((min_x - pad, min_y - pad, max_x + pad, max_y + pad))
print('QR box with padding:', qr_box.size)

# Resize to crisp 480x480 square
qr_square = qr_box.resize((480, 480), Image.Resampling.LANCZOS)

# Clean up contrast
q_arr = np.array(qr_square, dtype=float)
gray = 0.299 * q_arr[:,:,0] + 0.587 * q_arr[:,:,1] + 0.114 * q_arr[:,:,2]
# High contrast threshold
mask = np.clip((gray - 85) / (175 - 85) * 255, 0, 255).astype(np.uint8)
clean_arr = np.dstack([mask, mask, mask])
clean_img = Image.fromarray(clean_arr)
clean_img.save('qr_code_clean_v4.png')

import base64
with open('qr_code_clean_v4.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

with open('qr_base64_v4.txt', 'w', encoding='utf-8') as f:
    f.write(f'data:image/png;base64,{b64}')

print('Successfully saved clean square QR qr_code_clean_v4.png and qr_base64_v4.txt')
