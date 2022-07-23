from PIL import Image, ImageDraw, ImageFont
import math

class ShapeDrawer:
    def __init__(self, img_name, img_size):
        self.img_name = img_name
        self.img = Image.new("RGB", img_size, color = "white")
        self.draw = ImageDraw.Draw(self.img)
        self.fontsize = 12;
        self.font = ImageFont.truetype("./fonts/times.ttf", self.fontsize)

    def draw_oval(self, text, coordinate):
        self.draw.text(coordinate, text, fill = "black", font=self.font, anchor="mm")
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        bounding_coor = list(bounding_coor)
        bounding_coor[0] -= 20
        bounding_coor[1] -= 20
        bounding_coor[2] += 20
        bounding_coor[3] += 20
        self.draw.ellipse(bounding_coor, fill = None, outline = "black", width = 1)

    def draw_rectangle(self, text, coordinate):
        self.draw.text(coordinate, text, fill = "black", font=self.font, anchor="mm")
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        bounding_coor = list(bounding_coor)
        bounding_coor[0] -= 20
        bounding_coor[1] -= 20
        bounding_coor[2] += 20
        bounding_coor[3] += 20
        bounding_coor = tuple(bounding_coor)
        self.draw.rectangle(bounding_coor, fill = None, outline = "black", width = 1)

    def draw_parallelogram(self, text, coordinate):
        self.draw.text(coordinate, text, fill = "black", font=self.font, anchor="mm")
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        text_length = self.draw.textlength(text, font=self.font)
        bounding_coor = list(bounding_coor)
        # Calculating coordinate of parallagram
        bounding_coor_parall = (
            bounding_coor[0], bounding_coor[1] - 20,
            bounding_coor[0] + text_length + 20, bounding_coor[1] - 20,
            bounding_coor[2], bounding_coor[3] + 20,
            bounding_coor[2] - text_length - 20, bounding_coor[3] + 20
        )
        self.draw.polygon(bounding_coor_parall, fill = None, outline = "black", width = 1)

    def draw_diamond(self, text, coordinate):
        self.draw.text(coordinate, text, fill = "black", font=self.font, anchor="mm")
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        #Distance between coordinate and top left bounding_coor
        radius_bounding_circle = math.sqrt(
            (bounding_coor[0] - coordinate[0]) ** 2 +
            (bounding_coor[1] - coordinate[1]) ** 2
        ) + 20
        self.draw.regular_polygon((coordinate, radius_bounding_circle), 4, 45, fill = None, outline = "black")

    # def draw_line(self, coordinate):
    #     self.draw.line(coordinate, fill = "black")

    def save(self):
        self.img.save(self.img_name)
