from PIL import Image, ImageDraw
import random
import math

def create_linear_gradient(size, colors):

    width, height = size
    base = Image.new('RGB', size, colors[0])
    top = Image.new('RGB', size, colors[1])
    mask = Image.new('L', (1, height))

    for y in range(height):
        mask.putpixel((0, y), int(255 * (y / height)))

    mask = mask.resize(size)
    base.paste(top, (0, 0), mask)
    return base


def add_soft_blobs(image, palette, blob_count=20):

    draw = ImageDraw.Draw(image, 'RGBA')
    width, height = image.size

    for _ in range(blob_count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(50, 200)
        color = random.choice(palette)
        rgba = hex_to_rgba(color, alpha=random.randint(30, 80))  # low opacity
        draw.ellipse((x - r, y - r, x + r, y + r), fill=rgba)

    return image


def hex_to_rgba(hex_color, alpha=128):

    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b, alpha)


def generate_background(size=(800, 800), palette=None):
    if not palette or len(palette) < 2:
        palette = ['#ffcc00', '#ffee88']  # fallback yellow gradient

    # Step 1: Smooth gradient base
    background = create_linear_gradient(size, colors=random.sample(palette, 2))

    # Step 2: Add soft blobs for atmosphere
    background = add_soft_blobs(background, palette, blob_count=15)

    return background

