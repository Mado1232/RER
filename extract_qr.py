from PIL import Image
import numpy as np

img = Image.open('qr_card_full_user1.png').convert('RGB')
arr = np.array(img)

# Find QR boundaries:
# QR modules are black (< 80)
black = (arr[:,:,0] < 80) & (arr[:,:,1] < 80) & (arr[:,:,2] < 80)
y_idx, x_idx = np.where(black)

min_y, max_y = y_idx.min(), y_idx.max()
min_x, max_x = x_idx.min(), x_idx.max()

print(f'QR code bounding box: x=[{min_x}, {max_x}] (w={max_x - min_x + 1}), y=[{min_y}, {max_y}] (h={max_y - min_y + 1})')

# In qr_card_full_user1.png:
# Add 12px white quiet zone around the QR
qr_box = img.crop((min_x - 14, min_y - 14, max_x + 15, max_y + 15))
print('QR box size:', qr_box.size)

# Resize to perfect square 480x480 using high quality Lanczos or bicubic
qr_square = qr_box.resize((480, 480), Image.Resampling.LANCZOS)
qr_square.save('qr_code_v4_authentic.png')

# Also threshold / clean up white background to pure #ffffff and blacks to pure #111827 or crisp black
q_arr = np.array(qr_square, dtype=float)
# Contrast enhancement
gray = 0.299 * q_arr[:,:,0] + 0.587 * q_arr[:,:,1] + 0.114 * q_arr[:,:,2]
# Binarize with smooth edge
clean_arr = np.zeros((480, 480, 3), dtype=np.uint8)
# Sharp threshold with gentle anti-aliasing
mask = np.clip((gray - 90) / (180 - 90) * 255, 0, 255).astype(np.uint8)
clean_arr[:,:,:] = mask[:,:,np.newaxis]
Image.fromarray(clean_arr).save('qr_code_clean_v4.png')

import base64
with open('qr_code_clean_v4.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

with open('qr_base64_v4.txt', 'w', encoding='utf-8') as f:
    f.write(f'data:image/png;base64,{b64}')

print('Saved qr_code_clean_v4.png and qr_base64_v4.txt')
