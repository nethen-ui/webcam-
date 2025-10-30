import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not access webcam.")
    exit()

print("✅ Webcam accessed! Recording...")

for i in range(100):
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f"frame_{i}.jpg", frame)

cap.release()
print("🎥 Saved 100 frames as images (like an attacker would).")
