"""
    We want to call it with two arguments: the Pokedex folder and the name of the new folder
    which will be PokedexPNG.
"""

from sys import argv
import os
from PIL import Image

# Grab first and second argument
source_folder = argv[1]
dest_folder = argv[2]

# check of the dest_folder exists, if not we create it.
dest_path = f"./{dest_folder}"
if not os.path.exists(dest_path):
    os.mkdir(dest_path)

source_path = f"./{source_folder}"

with os.scandir(source_path) as pokedex_dir:
    # Loop through Pokedex
    for image in pokedex_dir:
        if image.name.endswith(".jpg") and image.is_file():
            # Convert images to png
            # Save to the new folder
            pokemon_img = Image.open(f"./{source_folder}/{image.name}")
            image_name = image.name.replace(".jpg", ".png")
            pokemon_img.save(f"./{dest_folder}/{image_name}", "png")
