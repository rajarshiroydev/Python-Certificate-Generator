# Certificate Generator

### Things you need
<ul>
  <li>A certificate template.
  <li>A font file in .ttf format.
  <li>Lastly, a list of names in .txt format.
</ul>

### Explaining the code

Using [Pillow Module](https://pypi.org/project/Pillow/) to write the text on the certificate.
  

    from PIL import Image, ImageFont, ImageDraw

    save_path = ""
    font_file1 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
    font_file2 = ImageFont.truetype(r'Font/GreatVibes-Regular.ttf', 140)
    font_colour = "#000000"

    template = Image.open(r'template.png')
    WIDTH, HEIGHT = template.size
