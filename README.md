# ez-text2vid

![screenshot](https://user-images.githubusercontent.com/115115916/229177973-6a5b1a28-38a8-42a1-bf80-1315cc4d806c.png)

A Streamlit app to easily run the [ModelScope text-to-video](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis) diffusion model with customized video length, fps, and dimensions. It can run on 4GB video cards, as well as CPU and Apple M chips.

**Built with:**
* [Huggingface Diffusers](https://github.com/huggingface/diffusers)🧨
* [Pytorch](https://github.com/pytorch/pytorch)
* [Streamlit](https://github.com/streamlit/streamlit)

## Install
> Before installing, make sure you have a working [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) installation.

Open up your terminal and enter the following commands line-by-line:

1. Clone this repo.

```bash
git clone https://github.com/kpthedev/ez-text2video.git
```

2. Open the directory.

```bash
cd ez-text2video
```

3. Create the conda environment.

```bash
conda env create -f environment.yaml
```

## Running
To run the app, make sure you are in the `ez-text2video` directory in your terminal. Then run these two commands to activate the conda environment and start the Streamlit app:

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
