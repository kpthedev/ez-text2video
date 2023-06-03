# -*- coding: utf-8 -*-
#
#  generate.py
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

import gc

import streamlit as st
import torch
from diffusers import TextToVideoSDPipeline


@st.cache_resource
def make_pipeline_generator(
    device: str, cpu_offload: bool, attention_slice: bool
) -> TextToVideoSDPipeline:
    """Create text2video pipeline"""
    pipeline = TextToVideoSDPipeline.from_pretrained(
        "damo-vilab/text-to-video-ms-1.7b",
        cache_dir="./cache",
        variant="fp16",
        torch_dtype=torch.float32 if device == "cpu" else torch.float16,
    )

    if cpu_offload:
        pipeline.enable_sequential_cpu_offload()
    else:
        pipeline = pipeline.to(torch.device(device))

    if attention_slice:
        pipeline.enable_attention_slicing()

    return pipeline


def generate(
    prompt: str,
    num_frames: int,
    num_steps: int,
    seed: int,
    height: int,
    width: int,
    device: str,
    cpu_offload: bool,
    attention_slice: bool,
) -> list:
    """Generate video with text2video pipeline"""
    pipeline = make_pipeline_generator(
        device=device, cpu_offload=cpu_offload, attention_slice=attention_slice
    )
    generator = torch.Generator().manual_seed(seed)
    video = pipeline(
        prompt=prompt,
        num_frames=num_frames,
        num_inference_steps=num_steps,
        height=height,
        width=width,
        generator=generator,
    ).frames
    torch.cuda.empty_cache()
    gc.collect()
    return video
