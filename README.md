# ez-text2vid

![screenshot](https://user-images.githubusercontent.com/115115916/229177973-6a5b1a28-38a8-42a1-bf80-1315cc4d806c.png)

A Streamlit app to easily run the [ModelScope text-to-video](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis) diffusion model with customizable number of frames, fps, and dimensions.

**Built with:**
* [Huggingface Diffusers](https://github.com/huggingface/diffusers)🧨
* [Pytorch](https://github.com/pytorch/pytorch)
* [Streamlit](https://github.com/streamlit/streamlit)

## Install
To install, just clone the repo and install the requirements with `pip`. Using a virtual environment is highly recommended, below is an example using `venv`:

### Linux/MacOS
```bash
git clone https://github.com/kpthedev/ez-text2video.git
cd ez-text2video
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Windows
```bash
git clone https://github.com/kpthedev/ez-text2video.git
cd ez-text2video
python -m venv .env
.env\Scripts\activate
pip install -r requirements.txt
```

## Running
To run the app, make sure you are in the `ez-text2video` folder and have activated the environment, then run:

```bash
streamlit run app.py
```
This should open the webUI in your browser automatically.

> The very first time you run the app, it will automatically download the models from Huggingface. This may a couple of minutes (~5 mins).


## License
All the original code that I have written is licensed under a GPL license. For the model weight license and conditions please refer to the [model card](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis).


## Changelog
* Mar 31, 2023 - Inital release
