with open('qr_base64_v4.txt', 'r', encoding='utf-8') as f:
    qr_b64 = f.read().strip()

with open('cat_sticker_base64.txt', 'r', encoding='utf-8') as f:
    cat_b64 = f.read().strip()

with open('src/assets/qrAsset.ts', 'w', encoding='utf-8') as f:
    f.write(f'export const AUTHENTIC_QR_BASE64 = "{qr_b64}";\n')

with open('src/assets/catAsset.ts', 'w', encoding='utf-8') as f:
    f.write(f'export const AUTHENTIC_CAT_STICKER_BASE64 = "{cat_b64}";\n')

print('Updated src/assets/qrAsset.ts and catAsset.ts')
