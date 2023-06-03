# ez-text2vid

<p align="center">
  <img src="https://user-images.githubusercontent.com/115115916/229304939-077368d0-58a2-499e-a2c8-010e1bb5f4e7.png" />
</p>

A Streamlit app to easily run the [ModelScope text-to-video](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis) diffusion model with customized video length, fps, and dimensions. It can run on 4GB video cards, as well as CPU and Apple M chips.

**Built with:**
* [Huggingface Diffusers](https://github.com/huggingface/diffusers)🧨
* [Pytorch](https://github.com/pytorch/pytorch)
* [Streamlit](https://github.com/streamlit/streamlit)

## Installation 
Before installing, make sure you have working [git](https://git-scm.com/downloads) and [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) installations. If you have an Nvidia graphics card, you should also install [CUDA](https://developer.nvidia.com/cuda-downloads).

### Install Steps:
1. Open a terminal on your machine. On Windows, you should use the Anaconda Prompt terminal.

2. Clone this repo using git:

    ```terminal
    git clone https://github.com/kpthedev/ez-text2video.git
    ```

3. Open the folder:

    ```terminal
    cd ez-text2video
    ```

4. Create the conda environment:

    ```terminal
    conda env create -f environment.yaml
    ```

## Running
To run the app, make sure you are in the `ez-text2video` folder in your terminal. Then run these two commands to activate the conda environment and start the Streamlit app:

```bash
conda activate t2v
streamlit run app.py
```
This should open the webUI in your browser automatically.

> The very first time you run the app, it will automatically download the models from Huggingface. This may a couple of minutes (~5 mins).


## License
All the original code that I have written is licensed under a GPL license. For the text-to-video model license and conditions please refer to the [model card](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis).


## Changelog
* Mar 31, 2023 - Inital release
* April 1, 2023 - Switch to conda install
* June 2, 2023 - Move to stable version of diffusers
