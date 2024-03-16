try:
    import cv2
    CAP_ANY = cv2.CAP_ANY
except ModuleNotFoundError:
    CAP_ANY = 0


class CameraInfo:
    def __init__(self, index, name, path, vid, pid, backend):
        self.__index = index
        self.__name = name
        self.__path = path
        self.__vid = vid
        self.__pid = pid
        self.__backend = backend

    def __str__(self):
        if self.__vid is not None and self.__pid is not None:
            return f'{self.__index}: {self.__name} ({self.__vid:04X}:{self.__pid:04X})'
        return f'{self.__index}: {self.__name}'

    def __repr__(self):
        return str(self)

    @property
    def index(self):
        return self.__index

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path

    @property
    def vid(self):
        return self.__vid

    @property
    def pid(self):
        return self.__pid

    @property
    def backend(self):
        return self.__backend

    def to_any(self):
        return CameraInfo(self.__index + self.__backend, self.__name, self.__path, self.__vid, self.__pid, CAP_ANY)


__all__ = ['CameraInfo']
