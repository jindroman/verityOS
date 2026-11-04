#!/usr/bin/env python3
"""Generate Verity OS boot art from branding/logo-source.png (the smiley):

  splash.png           640x480   ISO boot menu (BIOS syslinux)
  grub-background.png  1920x1080 GRUB menu on the installed system
  logo.png             880x300   general purpose logo

Needs Pillow + numpy. Uses the Poppins font if present (falls back to DejaVu).
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "logo-source.png")
SS = 3                                              # supersampling for text
INK, WHITE, GREY = (9, 12, 20), (240, 243, 250), (150, 158, 178)


def font(size, weight="Bold"):
    for p in (f"/usr/share/fonts/truetype/google-fonts/Poppins-{weight}.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def load_logo():
    """The smiley, cropped to its circle, plus its main yellow."""
    im = Image.open(SRC).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    a = np.array(im)
    solid = a[(a[..., 3] == 255) & (a[..., 0] > 240) & (a[..., 2] < 90)]
    yellow = tuple(int(v) for v in np.median(solid[:, :3], axis=0)) if len(solid) else (255, 214, 0)
    return im, yellow


def logo_at(size):
    im, _ = load_logo()
    out = im.resize((size, size), Image.LANCZOS)
    return out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2)) if size > im.width else out


def vgradient(size, top, bottom):
    w, h = size
    col = np.linspace(0, 1, h)[:, None, None]
    arr = (np.array(top) * (1 - col) + np.array(bottom) * col).astype(np.uint8)
    return Image.fromarray(np.repeat(arr, w, axis=1), "RGB")


def glow(canvas, cx, cy, radius, color, strength=0.35):
    layer = Image.new("L", canvas.size, 0)
    ImageDraw.Draw(layer).ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=255)
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55)).point(lambda v: int(v * strength))
    canvas.paste(Image.new("RGB", canvas.size, color), (0, 0), layer)


def text_layer(canvas_size, items):
    """Render text at SS x for crisp edges and return it downscaled as RGBA."""
    big = Image.new("RGBA", (canvas_size[0] * SS, canvas_size[1] * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    for it in items:
        it(d)
    return big.resize(canvas_size, Image.LANCZOS)


def wordmark(x, y, size, yellow):
    """Draws 'verity' + yellow 'OS' pill, top-left at (x, y); returns (drawer, width)."""
    f = font(int(size * SS), "Bold")
    pf = font(int(size * 0.44 * SS), "Bold")
    tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw = tmp.textlength("verity", font=f) / SS
    pw, ph = size * 0.98, size * 0.68
    gap = size * 0.30

    def draw(d):
        d.text((x * SS, y * SS), "verity", font=f, fill=WHITE)
        px, py = (x + tw + gap) * SS, (y + size * 0.27) * SS
        d.rounded_rectangle([px, py, px + pw * SS, py + ph * SS], radius=ph * SS / 2, fill=yellow)
        ow = tmp.textlength("OS", font=pf)
        d.text((px + (pw * SS - ow) / 2, py + ph * SS * 0.06), "OS", font=pf, fill=INK)
    return draw, tw + gap + pw


def paste_text(img, items):
    layer = text_layer(img.size, items)
    img.paste(layer, (0, 0), layer)


def splash(path):
    _, Y = load_logo()
    img = vgradient((640, 480), (10, 13, 22), (20, 26, 42))
    glow(img, 76, 82, 62, Y, 0.28)
    mark = logo_at(104)
    img.paste(mark, (24, 30), mark)
    wm, _ = wordmark(150, 36, 54, Y)
    tag = lambda d: d.text((154 * SS, 108 * SS), "Simple. Honest. AI built in.", font=font(15 * SS, "Regular"), fill=GREY)
    foot = lambda d: d.text((40 * SS, 452 * SS), "Verity OS", font=font(11 * SS, "Regular"), fill=(88, 96, 116))
    paste_text(img, [wm, tag, foot])
    ImageDraw.Draw(img).line([(40, 165), (600, 165)], fill=(40, 48, 68), width=1)
    img.save(path, optimize=True)
    print("wrote", path, img.size)


def grub_background(path):
    """Logo in the lower-middle: GRUB draws its menu in the upper part of the screen."""
    _, Y = load_logo()
    W, H = 1920, 1080
    img = vgradient((W, H), (8, 10, 18), (22, 28, 46))
    cx, cy = W // 2, 690
    glow(img, cx, cy, 230, Y, 0.30)
    mark = logo_at(300)
    img.paste(mark, (cx - 150, cy - 150), mark)
    size = 96
    tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw = tmp.textlength("verity", font=font(size * SS, "Bold")) / SS
    total = tw + size * 0.30 + size * 0.98
    wm, _ = wordmark(cx - total / 2, cy + 190, size, Y)
    tag = lambda d: d.text((cx * SS - tmp.textlength("Simple. Honest. AI built in.", font=font(26 * SS, "Regular")) / 2,
                            (cy + 320) * SS), "Simple. Honest. AI built in.", font=font(26 * SS, "Regular"), fill=GREY)
    paste_text(img, [wm, tag])
    img.save(path, optimize=True)
    print("wrote", path, img.size)


def logo_png(path):
    _, Y = load_logo()
    img = vgradient((880, 300), (10, 13, 22), (20, 26, 42))
    glow(img, 150, 150, 120, Y, 0.28)
    mark = logo_at(200)
    img.paste(mark, (50, 50), mark)
    wm, _ = wordmark(285, 85, 100, Y)
    paste_text(img, [wm])
    img.save(path, optimize=True)
    print("wrote", path, img.size)


if __name__ == "__main__":
    splash(os.path.join(HERE, "splash.png"))
    grub_background(os.path.join(HERE, "grub-background.png"))
    logo_png(os.path.join(HERE, "logo.png"))
