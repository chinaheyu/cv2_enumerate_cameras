from _cv2_enumerate_cameras import MSMF_enumerate_cameras, DSHOW_enumerate_cameras
import cv2
import re


class CameraInfo:
    def __init__(self, index, name, path):
        self.__index = index
        self.__name = name
        self.__path = path

    def __str__(self):
        vid_pid = self.__parse_vid_pid()
        if vid_pid:
            return f'{self.__index}: {self.__name} ({vid_pid[0]:04X}:{vid_pid[1]:04X})'
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
        if self.__path:
            return self.__path
        return None

    @property
    def vid(self):
        vid_pid = self.__parse_vid_pid()
        if vid_pid:
            return vid_pid[0]

    @property
    def pid(self):
        vid_pid = self.__parse_vid_pid()
        if vid_pid:
            return vid_pid[1]

    def __parse_vid_pid(self):
        if self.__path:
            m = re.search(r'vid_([0-9a-f]{4})&pid_([0-9a-f]{4})', self.__path, re.IGNORECASE)
            if m:
                return int(m.group(1), 16), int(m.group(2), 16)


def enumerate_cameras(apiPreference):
    if apiPreference == cv2.CAP_MSMF:
        camera_list = MSMF_enumerate_cameras()
    elif apiPreference == cv2.CAP_DSHOW:
        camera_list = DSHOW_enumerate_cameras()
    else:
        raise NotImplementedError(f"Unsupported backend {cv2.videoio_registry.getBackendName(apiPreference)}!")
    return [CameraInfo(i, *c) for i, c in enumerate(camera_list)]


__all__ = ['enumerate_cameras']
