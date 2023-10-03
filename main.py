import cv2
import numpy as np


def apply_wave_effect(img, phase, wave_amplitude):
    rows, cols, _ = img.shape

    # Create a grid of x, y coordinates
    x = np.arange(cols)
    y = np.arange(rows)
    X, Y = np.meshgrid(x, y, indexing='xy')
    print(X,Y)

    # Calculate the wave pattern
    wave = wave_amplitude * np.sin(2 * np.pi * X / 180 + phase)

    # Update Y values based on masks and cast to int32
    mask_70_80 = (Y >= int(rows * 0.70)) & (Y < int(rows * 0.80))
    mask_80_above = Y >= int(rows * 0.80)

    Y[mask_70_80] += wave[mask_70_80].astype(np.int32)
    Y[mask_80_above] += (2.5 * wave[mask_80_above]).astype(np.int32)

    # Clip to ensure Y indices remain within the image dimensions
    Y = np.clip(Y, 0, rows - 1)

    # Using fancy indexing to get the final image
    wave_img = img[Y, X]

    return wave_img


image_path = "pexels-quang-nguyen-vinh-2166695 (4).jpg"
output_video_path = "output_video_main_wave10.mp4"

img = cv2.imread(image_path)
h, w, _ = img.shape
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (w, h))
wave_height = 10.0
phase = 0.0

for _ in range(5 * fps):
    frame = apply_wave_effect(img, phase, wave_height)
    out.write(frame)
    phase -= 0.04

out.release()

