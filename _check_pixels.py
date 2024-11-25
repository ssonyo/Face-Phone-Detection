import cv2

# 이미지 열기
image_path = "/root/emotion/face3.jpg"
img = cv2.imread(image_path)

# 이미지 크기 확인
height, width, channels = img.shape
print(f"이미지 크기: {width}x{height} (픽셀)")


# 정사각형 크기 결정 (짧은 변 기준)
crop_size = min(width, height)

# 중심 좌표 계산
start_x = (width - crop_size) // 2
start_y = (height - crop_size) // 2

# 크롭 수행
cropped_img = img[start_y:start_y + crop_size, start_x:start_x + crop_size]
print(f"크롭된 이미지 크기: {cropped_img.shape[:2]}")

# 결과 저장 또는 보기
cv2.imwrite("face3.jpg", cropped_img)

