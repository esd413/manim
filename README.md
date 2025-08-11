<p align="center">
    <a href="https://github.com/3b1b/manim">
        <img src="https://raw.githubusercontent.com/3b1b/manim/master/logo/cropped.png">
    </a>
</p>

[![pypi version](https://img.shields.io/pypi/v/manimgl?logo=pypi)](https://pypi.org/project/manimgl/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![Manim Subreddit](https://img.shields.io/reddit/subreddit-subscribers/manim.svg?color=ff4301&label=reddit&logo=reddit)](https://www.reddit.com/r/manim/)
[![Manim Discord](https://img.shields.io/discord/581738731934056449.svg?label=discord&logo=discord)](https://discord.com/invite/bYCyhM9Kz2)
[![docs](https://github.com/3b1b/manim/workflows/docs/badge.svg)](https://3b1b.github.io/manim/)

Manim是一个用于精确编程动画的引擎，专为创建解释性数学视频而设计。



此Manim版本为esd413个人修改后的版本，可能与原版略有不同，但我会标注出来。原版存在的问题非常多，一部分的代码会无法运行。

对于Windows用户来说，该版本的Manim以及原版只能安装在高于Windows7的版本中（笔者使用的是Windows10,windows8没使用过，windows7好像是因为安装不了Python3.8及以上的版本）。

Note, there are two versions of manim.  This repository began as a personal project by the author of [3Blue1Brown](https://www.3blue1brown.com/) for the purpose of animating those videos, with video-specific code available [here](https://github.com/3b1b/videos).  In 2020 a group of developers forked it into what is now the [community edition](https://github.com/ManimCommunity/manim/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. See [this page](https://docs.manim.community/en/stable/faq/installation.html#different-versions) for more details.

## 安装
> [!Warning]
> **警告:** These instructions are for ManimGL _only_. Trying to use these instructions to install [Manim Community/manim](https://github.com/ManimCommunity/manim) or instructions there to install this version will cause problems. You should first decide which version you wish to install, then only follow the instructions for your desired version.

> [!Note]
> **Note**: To install manim directly through pip, please pay attention to the name of the installed package. This repository is ManimGL of 3b1b. The package name is `manimgl` instead of `manim` or `manimlib`. Please use `pip install manimgl` to install the version in this repository.

该Manim运行在Python3.8以及更高的版本。**Python一定要安装64位**，因为32位的Python很多标准库都要手动编译，而且只能在32位的系统上编译，不然就不能被32位的Python使用。 **Intel的用户安装的Python版本也是AMD64**想知道原因的请看[python下载包的时候，如何选择是win32，还是amd64的，其中的cp又是什么意思？](https://blog.csdn.net/qq_35889860/article/details/103269569)


Manim所需的环境 [FFmpeg](https://ffmpeg.org/), [OpenGL](https://www.opengl.org/) and [LaTeX](https://www.latex-project.org) (可选的，如果你想使用Latex，没有Latex将无法编辑数学公式和文字，除非你只是用来画图形).
对于Linux用户, [Pango](https://pango.gnome.org) along with its development headers are required. See instruction [here](https://github.com/ManimCommunity/ManimPango#building).


### 直接安装

```sh
# Install manimgl
pip install manimgl

# Try it out
manimgl
```

For more options, take a look at the [Using manim](#using-manim) sections further below.


如果你想修改manimlib本身，克隆此存储库并在该目录中执行：

```sh
# Install manimgl
pip install -e .

# Try it out
manimgl example_scenes.py OpeningManimExample
# or
manim-render example_scenes.py OpeningManimExample
```

### 直接安装 (Windows) 

1. [Install FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows).
2. 安装LaTeX发行版。 [Texlive](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/) 是被推荐的。
3. Install the remaining Python packages.
    ```sh
    git clone https://github.com/esd413/manim.git
    cd manim
    pip install -e .
    manimgl example_scenes.py OpeningManimExample
    ```

### Mac OSX

1. 在终端中使用Homebrew安装ffmpeg和latex.
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

Look through the [example scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html) to see examples of the library's syntax, animation types and object types. In the [3b1b/videos](https://github.com/3b1b/videos) repo, you can see all the code for 3blue1brown videos, though code from older videos may not be compatible with the most recent version of manim. The readme of that repo also outlines some details for how to set up a more interactive workflow, as shown in [this manim demo video](https://www.youtube.com/watch?v=rbu7Zu5X1zI) for example.

When running in the CLI, some useful flags include:
* `-w` to write the scene to a file
* `-o` to write the scene to a file and open the result
* `-s` to skip to the end and just show the final frame.
    * `-so` will save the final frame to an image and show it
* `-n <number>` to skip ahead to the `n`'th animation of a scene.
* `-f` to make the playback window fullscreen

Take a look at custom_config.yml for further configuration.  To add your customization, you can either edit this file, or add another file by the same name "custom_config.yml" to whatever directory you are running manim from.  For example [this is the one](https://github.com/3b1b/videos/blob/master/custom_config.yml) for 3blue1brown videos.  There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.

### 文档
Documentation is in progress at [3b1b.github.io/manim](https://3b1b.github.io/manim/). And there is also a Chinese version maintained by [**@manim-kindergarten**](https://manim.org.cn): [docs.manim.org.cn](https://docs.manim.org.cn/) (in Chinese).

[manim-kindergarten](https://github.com/manim-kindergarten/) wrote and collected some useful extra classes and some codes of videos in [manim_sandbox repo](https://github.com/manim-kindergarten/manim_sandbox).


## Contributing
Is always welcome.  As mentioned above, the [community edition](https://github.com/ManimCommunity/manim) has the most active ecosystem for contributions, with testing and continuous integration, but pull requests are welcome here too.  Please explain the motivation for a given change and examples of its effect.


## License
This project falls under the MIT license.
