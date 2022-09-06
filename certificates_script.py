from PIL import Image, ImageFont, ImageDraw

save_path = ""
font_file1 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
font_file2 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
font_colour = "#000000"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

event_name = ""
event_name_len = len(event_name)

name_list = []

f = open('names.txt', 'r')
names = f.readlines()
for item in names:
    name_list.append(item[:-1].title().strip())

print(name_list)

for i in name_list:
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width = draw.textlength(i, font = font_file1)
    name_height = draw.textlength(i, font = font_file1)
    draw.text(((WIDTH - name_width) / 1.75, (HEIGHT - 1410)), i, fill = font_colour, font = font_file1)
    draw.text(((WIDTH - event_name_len) / 3.8, (HEIGHT - 1235)), event_name, fill = font_colour, font = font_file2)
    image_source.save(f"{save_path}/ {i}.png")
    print('Saving Certificate of:', i)