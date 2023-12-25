from PIL import Image, ImageDraw, ImageFont
up_text = ""
down_text = ""
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
if text_type == 1:
    up_text = ""
    down_text = input("Введите нижний текст: ")
elif text_type == 2:
    up_text = input("Введите верхний текст: ")
    down_text = input("Введите нижний текст: ")
else:
    print("Перезапустите программу")
    quit()
print(up_text, down_text)
mems = ["cat.png", "cat1.png"]
print("Выберете картинку для мема: ")
for i in range(len(mems)):
    print(f"{i}: {mems[i]}")
choose = int(input("Выберете картинку: "))
image = Image.open(mems[choose])
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('times.ttf', size=70)
text = draw.textbbox((0, 0), up_text, font)
draw.text(((width - text[2]) / 2, 10), up_text, font=font, fill="black")
text = draw.textbbox((0, 0), down_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), down_text, font=font, fill="black")
image.save("new_mem.jpg")