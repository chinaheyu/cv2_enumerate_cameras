__version__ = '1.1.9'

from .camera_info import CameraInfo
import platform

system = platform.system()

try:
    import cv2
    CAP_ANY = cv2.CAP_ANY
except ModuleNotFoundError:
    CAP_ANY = 0

if system == 'Windows':
    from .windows_backend import supported_backends, cameras_generator
elif system == 'Linux':
    from .linux_backend import supported_backends, cameras_generator
else:
    from .opencv_backend import supported_backends, cameras_generator


def enumerate_cameras(apiPreference=CAP_ANY):
    if apiPreference != CAP_ANY and apiPreference not in supported_backends:
        raise NotImplementedError(f"Unsupported backend: {apiPreference}!")

    if apiPreference == CAP_ANY:
        return [i.to_any() for j in supported_backends for i in enumerate_cameras(j)]
    else:
        return list(cameras_generator(apiPreference))


__all__ = ['CameraInfo', 'supported_backends', 'enumerate_cameras']
