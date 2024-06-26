class CameraInfo:
    index: int
    name: str
    path: str
    vid: int
    pid: int
    backend: int

    def __init__(self, index: int, name: str, path: str, vid: int, pid: int, backend: int) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def to_any(self) -> CameraInfo:
        ...
