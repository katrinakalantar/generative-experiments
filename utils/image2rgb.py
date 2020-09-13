#!/bin/python3

from colorthief import ColorThief
import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

image = sys.argv[1]
n_colors = int(sys.argv[2])

def palette_to_rgb(palette):
    rgb = []
    for i in palette:
        rgb.append(tuple([j / 255 for j in i]))
    return rgb
    
color_thief = ColorThief(image)
dominant_color = palette_to_rgb([color_thief.get_color(quality=2)])  # get the dominant color
palette = color_thief.get_palette(color_count=n_colors)              # build a color palette
rgb_palette = palette_to_rgb(palette)                                # convert to RGB scale

print("\ncolor palette:")
print(palette)

output_string = '[\'rgb'
print(output_string)

for i in palette:
	output_string += (str(i))
	output_string += '\',\'rgb'

print(output_string)
output_string = output_string[0:len(output_string)-5]
output_string += ']'
print(output_string)

plt.bar([i for i in range(n_colors)], [10 for i in range(n_colors)],color=sns.color_palette(rgb_palette))
plt.savefig('palette_colors.png')
