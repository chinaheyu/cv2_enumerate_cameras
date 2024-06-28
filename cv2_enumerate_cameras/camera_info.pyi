CAP_ANY: int


class CameraInfo:

    def __init__(self, index: int, name: str, path: str | None, vid: int | None, pid: int | None, backend: int) -> None:
        self.index: int = index
        self.name: str = name
        self.path: str | None = path
        self.vid: int | None = vid
        self.pid: int | None = pid
        self.backend: int = backend

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
