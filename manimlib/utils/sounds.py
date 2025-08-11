from __future__ import annotations
# 声音及音乐的导入
from manimlib.utils.directories import get_sound_dir
from manimlib.utils.file_ops import find_file


def get_full_sound_file_path(sound_file_name: str) -> str:
    return find_file(
        sound_file_name,
        directories=[get_sound_dir()],
        extensions=[".wav", ".mp3", ""]
    )
