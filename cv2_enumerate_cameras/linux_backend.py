from cv2_enumerate_cameras.camera_info import CameraInfo
import os


try:
    import cv2
    CAP_GSTREAMER = cv2.CAP_GSTREAMER
    CAP_V4L2 = cv2.CAP_V4L2
except ModuleNotFoundError:
    CAP_GSTREAMER = 1800
    CAP_V4L2 = 200

supported_backends = (CAP_GSTREAMER, CAP_V4L2)


def read_line(*args):
    try:
        with open(os.path.join(*args)) as f:
            line = f.readline().strip()
        return line
    except IOError:
        return None


try:
    from linuxpy.video.device import iter_video_capture_devices

    def capture_files():
        for device in iter_video_capture_devices():
            yield device.PREFIX + str(device.index)
except ImportError:
    import glob

    def capture_files():
        yield from glob.glob('/dev/video*')


def cameras_generator(apiPreference):
    for path in capture_files():
        # find device name and index
        device_name = os.path.basename(path)
        if not device_name[5:].isdigit():
            continue
        index = int(device_name[5:])

        # read camera name
        video_device_path = f'/sys/class/video4linux/{device_name}'
        video_device_name_path = os.path.join(video_device_path, 'name')
        if os.path.exists(video_device_name_path):
            name = read_line(video_device_name_path)
        else:
            name = device_name

        # find vendor id and product id
        vid = None
        pid = None
        usb_device_path = os.path.join(video_device_path, 'device')
        if os.path.exists(usb_device_path):
            usb_device_path = os.path.realpath(usb_device_path)

            if ':' in os.path.basename(usb_device_path):
                usb_device_path = os.path.dirname(usb_device_path)

            vid = read_line(usb_device_path, 'idVendor')
            pid = read_line(usb_device_path, 'idProduct')
            if vid is not None:
                vid = int(vid, 16)
            if pid is not None:
                pid = int(pid, 16)

        yield CameraInfo(index, name, path, vid, pid, apiPreference)


__all__ = ['supported_backends', 'cameras_generator']
