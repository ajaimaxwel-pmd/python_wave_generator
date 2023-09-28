import cv2
import numpy as np


def apply_wave_effect(img, phase, wave_amplitude):
    rows, cols, _ = img.shape
    wave_img = np.copy(img)
    for y in range(int(rows * 0.70), rows):
        for x in range(cols):
            # gradient
            if y >= int(rows * 0.80):
                wave_amplitude = 2.5
            offset_y = int(wave_amplitude * np.sin(2 * np.pi * x / 180 + phase))
            if 0 <= y + offset_y < rows:
                wave_img[y + offset_y, x] = img[y, x]
    return wave_img


image_path = "pexels-quang-nguyen-vinh-2166695.jpg"
output_video_path = "output_video.mp4"

img = cv2.imread(image_path)
h, w, _ = img.shape
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (w, h))
wave_height = 5.0
phase = 0.0

for _ in range(5 * fps):
    frame = apply_wave_effect(img, phase, wave_height)
    out.write(frame)
    phase -= 0.04

out.release()
