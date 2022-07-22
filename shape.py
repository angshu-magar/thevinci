from PIL import Image, ImageDraw, ImageFont

class ShapeDrawer:
    def __init__(self, img_name):
        self.img_name = img_name
        self.img = Image.new("RGB", (595, 842), color = "white")
        self.draw = ImageDraw.Draw(self.img)
        self.fontsize = 12;
        self.font = ImageFont.truetype("./fonts/times.ttf", self.fontsize)

    def draw_oval(self):
        self.draw.ellipse((50,50,500,500), fill = None, outline = "black", width = 1)
        self.img.save(self.img_name)
        return 0

