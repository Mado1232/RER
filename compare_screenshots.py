from PIL import Image
import numpy as np

img1 = Image.open('C:/Users/Admin/.gemini/antigravity/brain/18c7e0a4-71bc-4cb2-954e-ac526294117a/.user_uploaded/media_1791664777128.png').convert('RGB')
img2 = Image.open('C:/Users/Admin/.gemini/antigravity/brain/18c7e0a4-71bc-4cb2-954e-ac526294117a/.user_uploaded/media_1791665140175.png').convert('RGB')

arr1 = np.array(img1)
arr2 = np.array(img2)

# Find white card bounds (near row 400)
slice1 = arr1[400, :, :]
card1_mask = (slice1[:, 0] > 250) & (slice1[:, 1] > 250) & (slice1[:, 2] > 250)
x1_min, x1_max = np.where(card1_mask)[0].min(), np.where(card1_mask)[0].max()
card1_w = x1_max - x1_min + 1

slice2 = arr2[400, :, :]
card2_mask = (slice2[:, 0] > 250) & (slice2[:, 1] > 250) & (slice2[:, 2] > 250)
x2_min, x2_max = np.where(card2_mask)[0].min(), np.where(card2_mask)[0].max()
card2_w = x2_max - x2_min + 1

print(f"Card 1 (Our App):  x={x1_min}..{x1_max}, width={card1_w}")
print(f"Card 2 (Original): x={x2_min}..{x2_max}, width={card2_w}")

# Measure QR code bounds
# In both images, the QR code has black pixels (RGB < 50) around rows 550..850
qr1_mask = (arr1[550:850, :, 0] < 50) & (arr1[550:850, :, 1] < 50) & (arr1[550:850, :, 2] < 50)
y1_idx, x1_idx = np.where(qr1_mask)
qr1_x_min, qr1_x_max = x1_idx.min(), x1_idx.max()
qr1_y_min, qr1_y_max = y1_idx.min() + 550, y1_idx.max() + 550
qr1_w = qr1_x_max - qr1_x_min + 1
qr1_h = qr1_y_max - qr1_y_min + 1

qr2_mask = (arr2[550:850, :, 0] < 50) & (arr2[550:850, :, 1] < 50) & (arr2[550:850, :, 2] < 50)
y2_idx, x2_idx = np.where(qr2_mask)
qr2_x_min, qr2_x_max = x2_idx.min(), x2_idx.max()
qr2_y_min, qr2_y_max = y2_idx.min() + 550, y2_idx.max() + 550
qr2_w = qr2_x_max - qr2_x_min + 1
qr2_h = qr2_y_max - qr2_y_min + 1

print(f"QR 1 (Our App):  x={qr1_x_min}..{qr1_x_max} (w={qr1_w}), y={qr1_y_min}..{qr1_y_max} (h={qr1_h})")
print(f"QR 2 (Original): x={qr2_x_min}..{qr2_x_max} (w={qr2_w}), y={qr2_y_min}..{qr2_y_max} (h={qr2_h})")
print(f"QR ratio to card: App={qr1_w/card1_w:.3f}, Original={qr2_w/card2_w:.3f}")

# Measure the QR card wrapper (the rounded light grey / white box around the QR code)
# In App, ticket-qr-card has background or border
# In Original, there is a rounded container with subtle shadow / border
# Let's crop the QR regions and save them side by side
crop1 = img1.crop((x1_min, 530, x1_max, 950))
crop2 = img2.crop((x2_min, 530, x2_max, 950))
crop1.save('crop_app_lower.png')
crop2.save('crop_orig_lower.png')
print("Saved crop_app_lower.png and crop_orig_lower.png")

# Measure "Номер: ..." text
# Rows 880..930
num1_mask = (arr1[880:940, :, 0] < 100) & (arr1[880:940, :, 1] < 100) & (arr1[880:940, :, 2] < 100)
if num1_mask.any():
    y1_n, x1_n = np.where(num1_mask)
    print(f"Номер 1 (Our App):  w={x1_n.max() - x1_n.min() + 1}, h={y1_n.max() - y1_n.min() + 1}, y={y1_n.min()+880}..{y1_n.max()+880}")

num2_mask = (arr2[880:940, :, 0] < 100) & (arr2[880:940, :, 1] < 100) & (arr2[880:940, :, 2] < 100)
if num2_mask.any():
    y2_n, x2_n = np.where(num2_mask)
    print(f"Номер 2 (Original): w={x2_n.max() - x2_n.min() + 1}, h={y2_n.max() - y2_n.min() + 1}, y={y2_n.min()+880}..{y2_n.max()+880}")
