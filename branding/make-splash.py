#!/usr/bin/env python3
"""Generate the Verity OS boot splash (640x480) for the ISO boot menu."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 640, 480
BG_TOP, BG_BOT = (11, 13, 18), (22, 26, 38)
YELLOW = (255, 210, 26)
WHITE = (235, 238, 245)
GREY = (140, 148, 165)

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
for y in range(H):                      # vertical gradient background
    t = y / (H - 1)
    d.line([(0, y), (W, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOT)))

def hexagon(cx, cy, r, rot=30):
    return [(cx + r * math.cos(math.radians(rot + 60 * i)),
             cy + r * math.sin(math.radians(rot + 60 * i))) for i in range(6)]

# logo mark: yellow hexagon with a dark V cut into it
cx, cy, r = 110, 85, 52
d.polygon(hexagon(cx, cy, r), fill=YELLOW)
d.polygon(hexagon(cx, cy, r - 9), fill=BG_TOP)
d.polygon([(cx - 26, cy - 24), (cx - 11, cy - 24), (cx, cy + 6), (cx + 11, cy - 24),
           (cx + 26, cy - 24), (cx + 4, cy + 28), (cx - 4, cy + 28)], fill=YELLOW)

def font(size, bold=True):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

d.text((185, 48), "Verity", font=font(46), fill=WHITE)
d.text((185 + d.textlength("Verity ", font=font(46)), 48), "OS", font=font(46), fill=YELLOW)
d.text((187, 108), "Install  \u00b7  Live  \u00b7  AI-assisted", font=font(15, False), fill=GREY)
d.line([(40, 165), (W - 40, 165)], fill=(45, 52, 70), width=1)
d.text((40, H - 28), "Verity OS", font=font(11, False), fill=(90, 98, 115))

img.save("splash.png", optimize=True)
print("wrote splash.png", img.size)
