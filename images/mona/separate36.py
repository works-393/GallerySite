#! python3
# 画像を36分割する
# コマンドプロンプトから実行
from PIL import Image

# 元画像を読み込み
original = Image.open('memo0.jpg')
width, height = original.size

# 分割数
cols = 6
rows = 6
piece_width = width // cols
piece_height = height // rows

# 切り出しループ
count = 1
for row in range(rows):
    for col in range(cols):
        left = col * piece_width
        upper = row * piece_height
        right = left + piece_width
        lower = upper + piece_height

        cropped = original.crop((left, upper, right, lower))
        cropped.save(f'memo{count}.jpg')
        count += 1
