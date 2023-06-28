## Setup

```
# python environment
conda env create -f=rvc.yaml

# install ffmpeg and ffprobe
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar xvf ffmpeg-release-amd64-static.tar.xz
cd ffmpeg-release-amd64-static
sudo cp ffmpeg /usr/local/bin
sudo cp ffprobe /usr/local/bin

```
