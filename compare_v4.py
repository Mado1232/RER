from PIL import Image

ref = Image.open('original_ref_full.png')
v4 = Image.open('prototype_v4.png')

# Create a side-by-side comparison image
# ref is 512x949, v4 is 430x940
rw, rh = ref.size
vw, vh = v4.size

# Scale both to height 940
ref_scaled = ref.resize((int(rw * 940 / rh), 940), Image.Resampling.LANCZOS)

cmp_img = Image.new('RGB', (ref_scaled.width + vw + 20, 940), (230, 233, 238))
cmp_img.paste(v4, (0, 0))
cmp_img.paste(ref_scaled, (vw + 20, 0))

cmp_img.save('side_by_side_v4_cmp.png')
print('Saved side_by_side_v4_cmp.png')
