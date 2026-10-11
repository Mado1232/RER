import shutil

shutil.copy('qr_code_v5_rounded.png', 'qr_authentic_2x.png')
shutil.copy('qr_code_v5_rounded.png', 'qr_code.png')

with open('qr_base64_v5.txt', 'r', encoding='utf-8') as f:
    b64 = f.read().strip()

with open('qr_base64.txt', 'w', encoding='utf-8') as f:
    f.write(b64)

with open('src/assets/qrAsset.ts', 'w', encoding='utf-8') as f:
    f.write(f'export const AUTHENTIC_QR_BASE64 = "{b64}";\n')

print('Successfully updated QR files and src/assets/qrAsset.ts')
