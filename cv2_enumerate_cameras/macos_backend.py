import re

import AVFoundation

from cv2_enumerate_cameras.camera_info import CameraInfo

try:
    import cv2

    CAP_AVFOUNDATION = cv2.CAP_AVFOUNDATION
except ModuleNotFoundError:
    CAP_AVFOUNDATION = 1200

supported_backends = (CAP_AVFOUNDATION,)


def cameras_generator(apiPreference):
    _VID_RE = re.compile(r"VendorID_(\d+)")
    _PID_RE = re.compile(r"ProductID_(\d+)")

    devs = AVFoundation.AVCaptureDevice.devicesWithMediaType_(
        AVFoundation.AVMediaTypeVideo
    )

    devs = devs.arrayByAddingObjectsFromArray_(
        AVFoundation.AVCaptureDevice.devicesWithMediaType_(
            AVFoundation.AVMediaTypeMuxed
        )
    )

    devs = list(devs)

    devs.sort(key=lambda d: d.uniqueID())

    for i, d in enumerate(devs):
        model = str(d.modelID())
        vid_m = _VID_RE.search(model)
        pid_m = _PID_RE.search(model)

        yield CameraInfo(
            index=i,
            name=d.localizedName(),
            path=d.uniqueID(),  # macOS does not provide a path, but uniqueID persists with a device over time
            vid=int(vid_m.group(1)) if vid_m else None,
            pid=int(pid_m.group(1)) if pid_m else None,
            backend=apiPreference,
        )


__all__ = ["supported_backends", "cameras_generator"]
