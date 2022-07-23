from PIL import Image, ImageDraw, ImageFont
import math

class ShapeDrawer:
    def __init__(self, img_name, img_size):
        self.img_name = img_name
        self.img = Image.new("RGB", img_size, color = "white")
        self.draw = ImageDraw.Draw(self.img)
        self.fontsize = 15;
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

    def draw_line(self, coordinate, text=""):
        self.draw.line(coordinate, fill = "black")
        coor_len = len(coordinate)
        arrow_length = 8
        if ((coordinate[coor_len - 1] == coordinate[coor_len - 3]) and (coordinate[coor_len - 2] > coordinate[coor_len - 4])):
            self.draw.line(coordinate, fill = "black")
            self.draw.line(
                [
                    ((coordinate[coor_len - 2] - arrow_length), (coordinate[coor_len - 1] - arrow_length)),
                    ((coordinate[coor_len - 2]), (coordinate[coor_len - 1])),
                    ((coordinate[coor_len - 2] - arrow_length), (coordinate[coor_len - 1] + arrow_length))
                ], fill = "black"
            )
        elif ((coordinate[coor_len - 1] == coordinate[coor_len - 3]) and (coordinate[coor_len - 2] < coordinate[coor_len - 4])):
            self.draw.line(coordinate, fill = "black")
            self.draw.line(
                [
                    ((coordinate[coor_len - 2] + arrow_length), (coordinate[coor_len - 1] - arrow_length)),
                    ((coordinate[coor_len - 2]), (coordinate[coor_len - 1])),
                    ((coordinate[coor_len - 2] + arrow_length), (coordinate[coor_len - 1] + arrow_length))
                ], fill = "black"
            )
        elif ((coordinate[coor_len - 2] == coordinate[coor_len - 4]) and (coordinate[coor_len - 1] > coordinate[coor_len - 3])):
            self.draw.line(coordinate, fill = "black")
            self.draw.line(
                [
                    ((coordinate[coor_len - 2] - arrow_length), (coordinate[coor_len - 1] - arrow_length)),
                    ((coordinate[coor_len - 2]), (coordinate[coor_len - 1])),
                    ((coordinate[coor_len - 2] + arrow_length), (coordinate[coor_len - 1] - arrow_length))
                ], fill = "black"
            )
        else:
            self.draw.line(coordinate, fill = "black")
            self.draw.line(
                [
                    ((coordinate[coor_len - 2] - arrow_length), (coordinate[coor_len - 1] + arrow_length)),
                    ((coordinate[coor_len - 2]), (coordinate[coor_len - 1])),
                    ((coordinate[coor_len - 2] + arrow_length), (coordinate[coor_len - 1] + arrow_length))
                ], fill = "black"
            )

        if (coordinate[1] == coordinate[3]):
            mid_point = (((coordinate[0]+coordinate[2]) / 2), ((coordinate[1]+coordinate[3]) / 2))
            anchor_point = list(mid_point)
            anchor_point[1] -= 10
            anchor_point = tuple(anchor_point)
            self.draw.text(anchor_point, text, fill = "black", font=self.font, anchor="ms")

        elif (coordinate[0] == coordinate[2]):
            mid_point = (((coordinate[0]+coordinate[2]) / 2), ((coordinate[1]+coordinate[3]) / 2))
            anchor_point = list(mid_point)
            anchor_point[0] += 10
            anchor_point = tuple(anchor_point)
            self.draw.text(anchor_point, text, fill = "black", font=self.font, anchor="lm")

    def return_bounding_coor(self, text, coordinate):
        bounding_coor = self.draw.textbbox(coordinate, text, font=self.font, anchor="mm")
        return bounding_coor

    def save(self):
        self.img.save(self.img_name)
