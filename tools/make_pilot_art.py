"""Square crops of real artwork colored by children in the first TPA pilot (D:/Personal Bisnis/TPA/result).
Crops keep only the drawing: the printed QR/access code in the sheet corner is cut away.

    python tools/make_pilot_art.py   # -> assets/gen/pilot_art_1..4.png
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps

SRC = Path(r'D:/Personal Bisnis/TPA/result')
GEN = Path(__file__).resolve().parent.parent / 'assets' / 'gen'
# (file, left, top, right, bottom) as fractions of the photo
CROPS = [('July 15 Photo 8.jpg', 0.21, 0.08, 0.81, 0.88),   # blue whale
         ('July 15 Photo 6.jpg', 0.25, 0.04, 0.80, 0.77),      # clownfish
         ('July 15 Photo 3.jpg', 0.29, 0.14, 0.77, 0.79),      # seahorse
         ('July 15 Photo 9.jpg', 0.31, 0.19, 0.81, 0.85)]      # swordfish

for i, (f, l, t, r, b) in enumerate(CROPS, 1):
    im = ImageOps.exif_transpose(Image.open(SRC / f)).convert('RGB')
    W, H = im.size
    im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
    side = min(im.size)
    im = ImageOps.fit(im, (side, side)).resize((520, 520), Image.LANCZOS)
    im.save(GEN / f'pilot_art_{i}.png')
    print('saved', GEN / f'pilot_art_{i}.png')

# Pilot photos (assets/pilot-project, WhatsApp screenshots): strip the black letterbox bars -> pilot_photo_1..4.jpg
BLUR = {3: [(772, 445, 858, 522)]}   # photo index -> boxes (after bar crop)
PHOTOS = Path(__file__).resolve().parent.parent / 'assets' / 'pilot-project'
for i, f in enumerate(sorted(PHOTOS.glob('*.jpeg')), 1):
    im = ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    rows = np.where(np.asarray(im.convert('L')).mean(axis=1) > 18)[0]
    im = im.crop((0, rows[0] + 2, im.width, rows[-1] - 1))
    for box in BLUR.get(i, []):   # printed QR + access code on the sheet stays unreadable
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(9)), box[:2])
    im.save(GEN / f'pilot_photo_{i}.jpg', quality=90)
    print('saved', GEN / f'pilot_photo_{i}.jpg', im.size)
