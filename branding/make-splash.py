#!/usr/bin/env python3
"""Generate Verity OS boot art: plain dark backgrounds, yellow accent only.

  splash.png           640x480   ISO boot menu (BIOS syslinux)
  grub-background.png  1920x1080 GRUB menu on the installed system
  logo.png             880x300   typographic "verity OS" wordmark

No smiley, no tagline, no artwork: just a near-black background. The yellow
accent lives in the menu colors (GRUB_COLOR_HIGHLIGHT, syslinux MENU COLOR),
not in the image. Needs Pillow + numpy.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
WHITE, YELLOW, INK = (240, 243, 250), (255, 210, 26), (9, 12, 20)
SS = 3                                              # supersampling for text


def font(size, weight="Bold"):
    for p in (
        f"/usr/share/fonts/truetype/google-fonts/Poppins-{weight}.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/seguibl.ttf" if weight == "Bold" else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if weight == "Bold" else "C:/Windows/Fonts/arial.ttf",
    ):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def dark(size, top=(10, 12, 17), bottom=(15, 18, 26), vignette=0.10):
    """Near-black vertical gradient with a barely visible vignette - no artwork."""
    w, h = size
    col = np.linspace(0, 1, h)[:, None, None]
    arr = (np.array(top) * (1 - col) + np.array(bottom) * col).astype(np.float32)
    arr = np.repeat(arr, w, axis=1)
    if vignette > 0:
        yy, xx = np.mgrid[0:h, 0:w]
        d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
        fall = 1.0 - vignette * np.clip(d - 0.6, 0, None)
        arr *= fall[..., None]
    return Image.fromarray(arr.astype(np.uint8), "RGB")


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


def splash(path):
    """Plain dark plate for the ISO boot menu - the menu text sits on top of it."""
    img = dark((640, 480))
    img.save(path, optimize=True)
    print("wrote", path, img.size)


def grub_background(path):
    """Plain dark plate for the installed system's GRUB menu."""
    img = dark((1920, 1080), top=(9, 11, 16), bottom=(14, 16, 23))
    img.save(path, optimize=True)
    print("wrote", path, img.size)


def logo_png(path):
    """Typographic wordmark only - no smiley, no tagline."""
    img = dark((880, 300))
    size = 100
    tmp = ImageDraw.Draw(Image.new("RGB", (4, 4)))
    tw = tmp.textlength("verity", font=font(size * SS, "Bold")) / SS
    total = tw + size * 0.30 + size * 0.98
    wm, _ = wordmark((880 - total) / 2, (300 - size * 0.9) / 2, size, YELLOW)
    layer = text_layer(img.size, [wm])
    img.paste(layer, (0, 0), layer)
    img.save(path, optimize=True)
    print("wrote", path, img.size)


if __name__ == "__main__":
    splash(os.path.join(HERE, "splash.png"))
    grub_background(os.path.join(HERE, "grub-background.png"))
    logo_png(os.path.join(HERE, "logo.png"))
