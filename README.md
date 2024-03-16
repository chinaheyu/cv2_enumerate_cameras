# cv2_enumerate_cameras

## Installation

### Install from PyPI

```commandline
pip install cv2_enumerate_cameras
```

### Install from Source

```commandline
pip install git+https://github.com/chinaheyu/cv2_enumerate_cameras.git
```

## Example

### Run as Script

```commandline
python -m cv2_enumerate_cameras
```

### Supported Backends

```python
from cv2.videoio_registry import getBackendName
from cv2_enumerate_cameras import supported_backends

for backend in supported_backends:
    print(getBackendName(backend))
```

### Enumerate Cameras

This is an example showing how to enumerate cameras.

```python
from cv2_enumerate_cameras import enumerate_cameras

for camera_info in enumerate_cameras():
    print(f'{camera_info.index}: {camera_info.name}')
```

Output:

```
1400: HD Webcam
...
700: HD Webcam
701: OBS Virtual Camera
...
```

These indices may seem strange, since [opencv defaults to using the high digits of index to represent the backend](https://github.com/opencv/opencv/blob/4.x/modules/videoio/src/cap.cpp#L245). For example, 701 indicates the second camera on the DSHOW backend (700).

You can also select a supported backend for enumerating camera devices.

Currently supported backends on windows:

- Microsoft Media Foundation (CAP_MSMF)
- DirectShow (CAP_DSHOW)

Currently supported backends on linux:

- GStreamer (CAP_GSTREAMER)
-  V4L/V4L2 (CAP_V4L2)

Here's an example of enumerating camera devices via the CAP_MSMF backend on windows.

```python
import cv2
from cv2_enumerate_cameras import enumerate_cameras

for camera_info in enumerate_cameras(cv2.CAP_MSMF):
    print(f'{camera_info.index}: {camera_info.name}')
```

Output:

```
0: HD Webcam
...
```

Once you have found the target camera, you can create a `cv2.VideoCapture` by its index and backend properties.

```pycon
cap = cv2.VideoCapture(camera_info.index, camera_info.backend)
```

### Camera Info

The `cv2_enumerate_cameras.enumerate_cameras()` function will return a list of `CameraInfo` objects.

- `CameraInfo.index`: Camera index for creating `cv2.VideoCapture`
- `CameraInfo.name`: Camera name
- `CameraInfo.path`:  Camera device path
- `CameraInfo.vid`:  Vendor identifier
- `CameraInfo.pid`:  Product identifier
- `CameraInfo.backend`: Camera backend

### Find Camera by Vendor and Product Identifier

```python
import cv2
from cv2_enumerate_cameras import enumerate_cameras

def find_camera(vid, pid, apiPreference=cv2.CAP_ANY):
    for i in enumerate_cameras(apiPreference):
        if i.vid == vid and i.pid == pid:
            return cv2.VideoCapture(i.index, i.backend)
    return None

cap = find_camera(0x04F2, 0xB711)
while True:
    result, frame = cap.read()
    if not result:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
```

## TODO

- [x] Windows Support
- [x] Linux Support
- [ ] MacOS Support
