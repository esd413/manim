
Manim是一个用于精确编程的动画引擎，专为创建解释性数学视频而设计。  
此为esd413克隆manim1.6.1后进行个性化修改的版本。将不会保留（docs和部分README.md的内容）:)

## Installation
> **WARNING:** These instructions are for ManimGL _only_. Trying to use these instructions to install [ManimCommunity/manim](https://github.com/ManimCommunity/manim) or instructions there to install this version will cause problems. You should first decide which version you wish to install, then only follow the instructions for your desired version.
> 
> **Note**: To install manim directly through pip, please pay attention to the name of the installed package. This repository is ManimGL of 3b1b. The package name is `manimgl` instead of `manim` or `manimlib`. Please use `pip install manimgl` to install the version in this repository.


System requirements are [FFmpeg](https://ffmpeg.org/), [OpenGL](https://www.opengl.org/) and [LaTeX](https://www.latex-project.org) (optional, if you want to use LaTeX).
For Linux, [Pango](https://pango.gnome.org) along with its development headers are required. See instruction [here](https://github.com/ManimCommunity/ManimPango#building).请确保你的Python版本小于3.11,原因是因为requirements.txt第25行明确规定Python版本一定要小于3.11（这应该是暂时的）
根据[issues](https://github.com/3b1b/manim/issues/2053),修改requirements.txt中numpy版本为1.24.0

### Directly

```sh
# Install manimgl
pip install manimgl

# Try it out
manimgl
```

For more options, take a look at the [Using manim](#using-manim) sections further below.



```sh
# Install manimgl
pip install -e .


# Try it out
manimgl example_scenes.py OpeningManimExample
# or
manim-render example_scenes.py OpeningManimExample
```

### Directly (Windows) 

1. [Install FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows).
2. Install a LaTeX distribution. Texlive is recommended.
3. Install the remaining Python packages.
    ```sh
    git clone https://github.com/3b1b/manim.git
    cd manim
    pip install -e .
    manimgl example_scenes.py OpeningManimExample
    ```

### Mac OSX

1. Install FFmpeg, LaTeX in terminal using homebrew.
    ```sh
    brew install ffmpeg mactex
    ```
   
2. Install latest version of manim using these command.
    ```sh
    git clone https://github.com/3b1b/manim.git
    cd manim
    pip install -e .
    manimgl example_scenes.py OpeningManimExample
    ```

## Anaconda Install

1. Install LaTeX as above.
2. Create a conda environment using `conda create -n manim python=3.8`.
3. Activate the environment using `conda activate manim`.
4. Install manimgl using `pip install -e .`.


## Using manim
Try running the following:
```sh
manimgl example_scenes.py OpeningManimExample
```
This should pop up a window playing a simple scene.

Some useful flags include:
* `-w` 将场景写入文件
* `-o` 将场景写入文件并打开
* `-s` 跳到最后，并显示最后一帧（没有渲染过程）
    * `-so` 将最后一帧保存为图像并显示
* `-n <number>` to skip ahead to the `n`'th animation of a scene.
* `-f` to make the playback window fullscreen

Take a look at custom_config.yml for further configuration.  To add your customization, you can either edit this file, or add another file by the same name "custom_config.yml" to whatever directory you are running manim from.  For example [this is the one](https://github.com/3b1b/videos/blob/master/custom_config.yml) for 3blue1brown videos.  There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.

Look through the [example scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html) to get a sense of how it is used, and feel free to look through the code behind [3blue1brown videos](https://github.com/3b1b/videos) for a much larger set of example. Note, however, that developments are often made to the library without considering backwards compatibility with those old videos. To run an old project with a guarantee that it will work, you will have to go back to the commit which completed that project.

### Documentation
官方文档在[3b1b.github.io/manim](https://3b1b.github.io/manim/)但并不完整. 有一个中文版本是由[**@manim-kindergarten**](https://manim.org.cn)翻译的: [docs.manim.org.cn](https://docs.manim.org.cn/) (in Chinese).
## License
本项目遵循MIT协议