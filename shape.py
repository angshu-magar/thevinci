from PIL import Image, ImageDraw, ImageFont

class ShapeDrawer:
    def __init__(self, img_name):
        self.img_name = img_name
        self.img = Image.new("RGB", (595, 842), color = "white")
        self.draw = ImageDraw.Draw(self.img)
        self.fontsize = 12;
        self.font = ImageFont.truetype("./fonts/times.ttf", self.fontsize)

    def draw_oval(self, text, coordinate):
        self.draw.text(coordinate, text, font=self.font, anchor="mm")
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        bounding_coor = list(bounding_coor)
        bounding_coor[0] -= 20
        bounding_coor[1] -= 20
        bounding_coor[2] += 20
        bounding_coor[3] += 20
        self.draw.ellipse(bounding_coor, fill = None, outline = "black", width = 1)

    def save(self):
        self.img.save(self.img_name)
