#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont
import random

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

def create_placeholder(filename, text, color_scheme):
    """Create a placeholder image with text"""
    width, height = 400, 400

    # Create image with background
    img = Image.new('RGB', (width, height), color=color_scheme['bg'])
    draw = ImageDraw.Draw(img)

    # Draw some abstract shapes
    for _ in range(8):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=color_scheme['line'], width=2)

    # Draw circles for scientific look
    for _ in range(5):
        x = random.randint(50, width-50)
        y = random.randint(50, height-50)
        r = random.randint(20, 60)
        draw.ellipse([x-r, y-r, x+r, y+r], outline=color_scheme['accent'], width=2)

    # Try to use a basic font, fallback to default if not available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    except:
        font = ImageFont.load_default()

    # Add text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw text background
    padding = 20
    draw.rectangle([text_x - padding, text_y - padding,
                   text_x + text_width + padding, text_y + text_height + padding],
                  fill=color_scheme['text_bg'])

    # Draw text
    draw.text((text_x, text_y), text, fill=color_scheme['text'], font=font)

    # Save image
    img.save(f'images/{filename}')
    print(f"Created {filename}")

# Color schemes - green theme
green_scheme = {
    'bg': (245, 250, 247),
    'line': (200, 230, 210),
    'accent': (13, 122, 62),
    'text_bg': (255, 255, 255),
    'text': (26, 26, 26)
}

# Create placeholder images
random.seed(42)  # For reproducible "random" patterns

# Headshot placeholder
create_placeholder('headshot.png', 'SHAHMIR\nAZIZ', green_scheme)

# Publication placeholder
random.seed(43)
create_placeholder('publication.png', 'LIPID\nVESICLE', green_scheme)

# Blog placeholders
random.seed(44)
create_placeholder('blog1.png', 'SWARM\nCONTROL', green_scheme)

random.seed(45)
create_placeholder('blog2.png', 'PROTEIN\nBINDING', green_scheme)

# Research project placeholders
random.seed(46)
create_placeholder('soma.png', 'SOMA\nDEVICE', green_scheme)

random.seed(47)
create_placeholder('glucose.png', 'GLUCOSE\nML', green_scheme)

random.seed(48)
create_placeholder('microbot.png', 'MICRO\nROBOT', green_scheme)

print("\nAll placeholder images created successfully!")