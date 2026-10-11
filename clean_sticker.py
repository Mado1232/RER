from PIL import Image, ImageFilter
import numpy as np

img = Image.open('user_badge_notch_ref.png').convert('RGBA')

# Badge center is at (104.5, 64)
# Crop around sticker
crop = img.crop((80, 34, 131, 91))
arr = np.array(crop, dtype=float)

# Background has high color divergence between channels (pink/purple) and low green
max_c = np.max(arr[:,:,:3], axis=2)
min_c = np.min(arr[:,:,:3], axis=2)
delta = max_c - min_c

# Background condition:
# Red is high (>120), Blue is high (>120), Green is low (<160), delta > 40
is_bg = (delta > 38) & (arr[:,:,1] < 165)

# Mask image
mask_arr = np.where(is_bg, 0, 255).astype(np.uint8)
mask_img = Image.fromarray(mask_arr, 'L')
# Smooth mask
mask_blurred = mask_img.filter(ImageFilter.GaussianBlur(radius=0.7))

# Whitewash edge pixels so no purple fringe remains
out_arr = arr[:,:,:3].copy()
mask_np = np.array(mask_blurred)
edge_mask = (mask_np > 5) & (mask_np < 245)
out_arr[edge_mask] = [255, 255, 255]

res = np.dstack([out_arr.astype(np.uint8), mask_np])
res_img = Image.fromarray(res, 'RGBA')
res_img.save('clean_extracted_sticker.png')
print('Saved clean_extracted_sticker.png with PIL GaussianBlur')
