# Certificate Generator

## Things you need
<ul>
  <li>A certificate template.
  <li>A font file in .ttf format.
  <li>Lastly, a list of names in .txt format.
</ul>
<br>
<br>

## Explaining the code

Using [Pillow Module](https://pypi.org/project/Pillow/) to write the text on the certificate.
  
```python
from PIL import Image, ImageFont, ImageDraw

save_path = ""
font_file1 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
font_file2 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
font_colour = "#000000"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

event_name = ""
event_name_len = len(event_name)
```
<ul>
  <li>Paste the link of the folder in save_path where you would want to save the certificates.
  <li>Here I have written 2 lines of font files because a lot of the times, we need to change the event for different set of participants. If there are more fields to be written, just add more such lines. Also this gives us the freedom to change the font file and size for each text. (In my case, there were 2 fields and so the code is written that way)
  <li>The certificate file name should be written in place of template.png.
  <li>event_name is optional and can be used if a second field is required. Refer second point.
</ul>
<br>
<br>

Code module for reading names from each line.
```python
name_list = []

f = open('names.txt', 'r')
names = f.readlines()
for item in names:
    name_list.append(item[:-1].title().strip())
```
<ul>
  <li>name_list[] is for storing the names in a list from a text file.
  <li>The .txt file name should me written in place of names.txt.
  <li>item[:-1] else it will throw an error because of '\n' in each line. <br>title() as data may not be clean and this will make the names in Title Case. <br>strip() as the data may have extra spaces on both sides.
</ul>
<br>
<br>

The actual stuff
```python
for i in name_list:
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width = draw.textlength(i, font = font_file1)
    name_height = draw.textlength(i, font = font_file1)
    draw.text(((WIDTH - name_width) / 1.75, (HEIGHT - 1410)), i, fill = font_colour, font = font_file1)
    draw.text(((WIDTH - event_name_len) / 3.8, (HEIGHT - 1235)), event_name, fill = font_colour, font = font_file2)
    image_source.save(f"{save_path}/ {i}.png")
    print('Saving Certificate of:', i)
```
<ul>
  <li>The certificate file name should be written in place of template.png.
  <li>The numerical values will have to be adjusted according to the dimensions of the certificate and placement of the text.
  <li>Use number of draw.text lines as per need.
</ul
  

Working:
| Template      | Generated |
| ----------- | ----------- |
| ![Template](https://github.com/roy-rajarshi/Certificate-Generator/blob/main/template.png)      |        |
  
  
  
  
  
  
  
  
