#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

Run: python3 draw_news.py  -> writes entry.png next to this file.
The entry program (main.py) only copies entry.png to /output/entry.png,
so this script runs on the builder's machine, not in the grader.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = font("DejaVuSans-Bold.ttf", 64)
F_SUB = font("DejaVuSans.ttf", 26)
F_KICK = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_BODY = font("DejaVuSans.ttf", 21)

# Palette
PAPER = (247, 243, 234)
NAVY = (26, 42, 74)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
LINE = (210, 205, 192)

ACCENTS = [
    (26, 42, 74),    # summit - navy
    (110, 70, 130),  # icj - purple
    (46, 90, 140),   # kerch - steel blue
    (146, 32, 32),   # gulf - deep red
    (30, 110, 110),  # anthropic - teal
    (46, 110, 66),   # cop31 - green
]

STORIES = [
    ("DIPLOMACY", "TRILATERAL SUMMIT",
     "Trump, Xi and Putin hold the first three-way summit in Shenzhen; a 'peace declaration' follows.",
     "globe"),
    ("JUSTICE", "ICJ: MYANMAR GENOCIDE",
     "UN court rules Myanmar committed state-sponsored genocide against the Rohingya — a first.",
     "scales"),
    ("EUROPE", "KERCH BRIDGE HIT AGAIN",
     "Third Ukrainian strike in a week halts rail traffic; part of the bridge collapses.",
     "bridge"),
    ("MIDDLE EAST", "GULF WAR WIDENS",
     "Iran hits Kuwait and Bahrain; a Houthi missile damages a tower in Riyadh.",
     "ship"),
    ("TECH", "ANTHROPIC'S RECORD IPO",
     "AI firm raises $81.3 billion at a $1.5 trillion valuation, the biggest debut yet.",
     "chart"),
    ("CLIMATE", "COP31'S FINAL PUSH",
     "Ministers race to unblock climate talks in Antalya before Friday's deadline.",
     "leaf"),
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def icon_globe(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=4)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=col, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=col, width=3)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 200, 340, fill=col, width=3)


def icon_scales(d, cx, cy, r, col):
    d.line([cx, cy - 32, cx, cy + 30], fill=col, width=4)
    d.line([cx - 30, cy - 22, cx + 30, cy - 22], fill=col, width=4)
    d.line([cx, cy - 32, cx, cy - 38], fill=col, width=4)
    d.ellipse([cx - 5, cy - 40, cx + 5, cy - 30], fill=col)
    for sx in (-30, 30):
        d.line([cx + sx, cy - 22, cx + sx, cy - 2], fill=col, width=3)
        d.pieslice([cx + sx - 14, cy - 2, cx + sx + 14, cy + 18], 0, 180, fill=col)
    d.line([cx - 22, cy + 30, cx + 22, cy + 30], fill=col, width=4)


def icon_bridge(d, cx, cy, r, col):
    d.arc([cx - 44, cy - 10, cx + 44, cy + 44], 180, 360, fill=col, width=5)
    d.line([cx - 52, cy + 18, cx + 52, cy + 18], fill=col, width=5)
    for x in (-30, -10, 10, 30):
        d.line([cx + x, cy - 2, cx + x, cy + 18], fill=col, width=3)
    d.line([cx - 44, cy - 26, cx - 44, cy + 18], fill=col, width=3)
    d.line([cx + 44, cy - 26, cx + 44, cy + 18], fill=col, width=3)


def icon_ship(d, cx, cy, r, col):
    d.polygon([(cx - 42, cy + 8), (cx + 42, cy + 8), (cx + 28, cy + 26),
               (cx - 28, cy + 26)], fill=col)
    d.rectangle([cx - 16, cy - 14, cx + 16, cy + 8], fill=col)
    d.line([cx, cy - 34, cx, cy - 14], fill=col, width=4)
    d.polygon([(cx, cy - 34), (cx + 20, cy - 22), (cx, cy - 22)], fill=col)
    d.line([cx - 38, cy + 34, cx + 38, cy + 34], fill=col, width=4)


def icon_chart(d, cx, cy, r, col):
    for i, h in enumerate((16, 26, 38)):
        x0 = cx - 36 + i * 26
        d.rectangle([x0, cy + 22 - h, x0 + 16, cy + 22], fill=col)
    d.line([cx - 40, cy - 30, cx - 8, cy - 6, cx + 12, cy - 18, cx + 40, cy - 34],
           fill=col, width=4)
    d.polygon([(cx + 40, cy - 34), (cx + 26, cy - 34), (cx + 40, cy - 20)], fill=col)


def icon_leaf(d, cx, cy, r, col):
    d.polygon([(cx, cy - 34), (cx + 24, cy - 6), (cx, cy + 34),
               (cx - 24, cy - 6)], fill=col)
    d.line([cx, cy + 30, cx, cy - 30], fill=(255, 255, 255), width=3)
    d.line([cx, cy - 6, cx + 14, cy - 16], fill=(255, 255, 255), width=2)
    d.line([cx, cy + 6, cx - 14, cy - 4], fill=(255, 255, 255), width=2)


ICONS = {"globe": icon_globe, "scales": icon_scales, "bridge": icon_bridge,
         "ship": icon_ship, "chart": icon_chart, "leaf": icon_leaf}


def draw():
    W, H = 1024, 1024
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)

    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    kick = "WORLD NEWS  •  ONE DAY IN THE WORLD"
    d.text(((W - d.textlength(kick, font=F_KICK)) / 2, 16), kick,
           font=F_KICK, fill=GOLD)
    title = "19 NOVEMBER 2026"
    d.text(((W - d.textlength(title, font=F_TITLE)) / 2, 44), title,
           font=F_TITLE, fill=(255, 255, 255))
    sub = "Thursday — the day's most consequential stories"
    d.text(((W - d.textlength(sub, font=F_SUB)) / 2, 112), sub,
           font=F_SUB, fill=(200, 210, 230))

    # 2 x 3 grid of story cards
    gx, gy = 24, 174
    cw, ch, gap = 478, 250, 20
    for i, (kicker, head, body, kind) in enumerate(STORIES):
        x = gx + (i % 2) * (cw + gap)
        y = gy + (i // 2) * (ch + gap)
        acc = ACCENTS[i]
        d.rectangle([x, y, x + cw, y + ch], fill=CARD, outline=LINE, width=2)
        d.rectangle([x, y, x + cw, y + 8], fill=acc)
        # icon in a tinted circle
        cx, cy = x + 52, y + 62
        d.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], fill=(238, 238, 230))
        ICONS[kind](d, cx, cy, 30, acc)
        # kicker + headline
        tx = x + 108
        d.text((tx, y + 22), kicker, font=F_KICK, fill=acc)
        hl = wrap(d, head, F_HEAD, cw - 128)
        hy = y + 48
        for ln in hl[:2]:
            d.text((tx, hy), ln, font=F_HEAD, fill=INK)
            hy += 34
        # body
        bl = wrap(d, body, F_BODY, cw - 40)
        by = y + 128
        for ln in bl[:3]:
            d.text((x + 20, by), ln, font=F_BODY, fill=(60, 60, 60))
            by += 27

    # footer
    foot = "Sources: Reuters • Associated Press • BBC • UN • ICJ • IAEA"
    d.text(((W - d.textlength(foot, font=F_BODY)) / 2, H - 32), foot,
           font=F_BODY, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    im.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes", im.size)


if __name__ == "__main__":
    draw()
