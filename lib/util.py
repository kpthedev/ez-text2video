# -*- coding: utf-8 -*-
#
#  util.py
#
#  Copyright 2023 KP
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from pathlib import Path

import cv2
import torch


# Adapted from: https://github.com/huggingface/diffusers/blob/main/src/diffusers/utils/testing_utils.py
def convert_to_video(video_frames: list, fps: int, filename: str) -> str:
    """Convert from numpy array of frame to webm"""
    Path("./outputs").mkdir(parents=True, exist_ok=True)
    output_video_path = f"./outputs/{filename}.webm"
    fourcc = cv2.VideoWriter_fourcc(*"VP90")
    h, w, c = video_frames[0].shape
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=(w, h))
    for i in range(len(video_frames)):
        img = cv2.cvtColor(video_frames[i], cv2.COLOR_RGB2BGR)
        video_writer.write(img)
    return output_video_path


def get_device() -> str:
    """Get string of torch accelerator"""
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"
