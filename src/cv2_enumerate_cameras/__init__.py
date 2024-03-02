import platform


system = platform.system()


class CameraInfo:
    def __init__(self, index, name, path=None, vid=None, pid=None):
        self.__index = index
        self.__name = name
        self.__path = path
        self.__vid = vid
        self.__pid = pid

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


if system == 'Windows':
    from ._cv2_enumerate_cameras import MSMF_enumerate_cameras, DSHOW_enumerate_cameras
    import re

    try:
        import cv2
        CAP_MSMF = cv2.CAP_MSMF
        CAP_DSHOW = cv2.CAP_DSHOW
    except ModuleNotFoundError:
        CAP_MSMF = 1400
        CAP_DSHOW = 700

    supported_backends = (CAP_MSMF, CAP_MSMF)

    def cameras_generator(apiPreference):

        def parse_vid_pid(path):
            if path:
                m = re.search(r'vid_([0-9a-f]{4})&pid_([0-9a-f]{4})', path, re.IGNORECASE)
                if m:
                    return int(m.group(1), 16), int(m.group(2), 16)
            return None, None

        if apiPreference == CAP_MSMF:
            camera_list = MSMF_enumerate_cameras()
        elif apiPreference == CAP_DSHOW:
            camera_list = DSHOW_enumerate_cameras()
        else:
            raise NotImplementedError(f"Unsupported backend: {apiPreference}!")
        for index, (name, path) in enumerate(camera_list):
            vid, pid = parse_vid_pid(path)
            yield CameraInfo(index, name, path, vid, pid)


if system == 'Linux':
    import os
    import glob

    try:
        import cv2
        CAP_GSTREAMER = cv2.CAP_GSTREAMER
        CAP_V4L2 = cv2.CAP_V4L2
    except ModuleNotFoundError:
        CAP_GSTREAMER = 1800
        CAP_V4L2 = 200

    supported_backends = (CAP_GSTREAMER, CAP_V4L2)

    def cameras_generator(apiPreference):

        def read_line(*args):
            try:
                with open(os.path.join(*args)) as f:
                    line = f.readline().strip()
                return line
            except IOError:
                return None

        for path in glob.glob('/dev/video*'):
            device_name = os.path.basename(path)
            index = int(device_name[5:])
            video_device_path = f'/sys/class/video4linux/{device_name}'
            usb_device_path = os.path.join(video_device_path, 'device')
            if os.path.exists(usb_device_path):
                usb_device_path = os.path.realpath(usb_device_path)
                if ':' in os.path.basename(usb_device_path):
                    name = read_line(usb_device_path, 'interface')
                    usb_device_path = os.path.dirname(usb_device_path)
                else:
                    name = read_line(usb_device_path, 'product')
                vid = int(read_line(usb_device_path, 'idVendor'), 16)
                pid = int(read_line(usb_device_path, 'idProduct'), 16)
            else:
                name = read_line(video_device_path, 'name')
                if not name:
                    name = device_name
                vid = None
                pid = None
            yield CameraInfo(index, name, path, vid, pid)


def enumerate_cameras(apiPreference):
    return list(cameras_generator(apiPreference))


__all__ = ['CameraInfo', 'supported_backends', 'enumerate_cameras']
