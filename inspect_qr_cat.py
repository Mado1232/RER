from PIL import Image

# 1. Compare the center cat head in reference QR vs our current QR
ref = Image.open('ref_qr_section.png')
# Cat head in ref is roughly in the center
w, h = ref.size
ref_cat = ref.crop((int(w * 0.38), int(h * 0.65), int(w * 0.62), int(h * 0.88)))
ref_cat.save('ref_qr_cat_crop.png')
print('Cropped ref_qr_cat_crop.png')

# Current QR
cur = Image.open('qr_code.png')
cw, ch = cur.size
cur_cat = cur.crop((int(cw * 0.38), int(ch * 0.38), int(cw * 0.62), int(ch * 0.62)))
cur_cat.save('cur_qr_cat_crop.png')
print('Cropped cur_qr_cat_crop.png')
