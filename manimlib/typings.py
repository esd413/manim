from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union, Tuple, Annotated, Literal, Iterable, Dict
    from colour import Color
    import numpy as np
    import re

    try:
        from typing import Self
    except ImportError:
        from typing_extensions import Self

    # Abbreviations for a common types
    ManimColor = Union[str, Color, None]
    RangeSpecifier = Tuple[float, float, float] | Tuple[float, float]


    Span = tuple[int, int]
    SingleSelector = Union[
        str,
        re.Pattern,
        tuple[Union[int, None], Union[int, None]],
    ]
    Selector = Union[SingleSelector, Iterable[SingleSelector]]

    UniformDict = Dict[str, float | bool | np.ndarray | tuple]

    # These are various alternate names for np.ndarray meant to specify
    # certain shapes.
    #
    # In theory, these annotations could be used to check arrays sizes
    # at runtime, but at the moment nothing actually uses them, and
    # the names are here primarily to enhance readibility and allow
    # for some stronger type checking if numpy has stronger typing
    # in the future
    FloatArray = np.ndarray[int, np.dtype[np.float64]] # 一个任意维度的、数据类型为 float64 的 NumPy 数组
    Vect2 = Annotated[FloatArray, Literal[2]] # 二维向量
    Vect3 = Annotated[FloatArray, Literal[3]] # 三维向量
    Vect4 = Annotated[FloatArray, Literal[4]] # 四维向量
    VectN = Annotated[FloatArray, Literal["N"]] # N维向量
    Matrix3x3 = Annotated[FloatArray, Literal[3, 3]] # 3x3矩阵
    VectArray = Annotated[FloatArray, Literal["N", 1]] # 1维数组
    Vect2Array = Annotated[FloatArray, Literal["N", 2]] # 2维数组
    Vect3Array = Annotated[FloatArray, Literal["N", 3]] # 3维数组
    Vect4Array = Annotated[FloatArray, Literal["N", 4]] # 4维数组
    VectNArray = Annotated[FloatArray, Literal["N", "M"]] # N维数组
