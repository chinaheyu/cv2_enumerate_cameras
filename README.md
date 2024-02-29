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

### Enumerate Cameras

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

### Camera Info

The `cv2_enumerate_cameras.enumerate_cameras()` function will return a list of `CameraInfo` objects.

- `CameraInfo.index`: Camera index for creating `cv2.VideoCapture`
- `CameraInfo.name`: Camera name
- `CameraInfo.path`:  Camera device path
- `CameraInfo.vid`:  Vendor identifier
- `CameraInfo.pid`:  Product identifier

### Find Camera by Vendor and Product Identifier

```python
import cv2
from cv2_enumerate_cameras import enumerate_cameras

def find_camera(vid, pid, apiPreference=cv2.CAP_MSMF):
    for i in enumerate_cameras(apiPreference):
        if i.vid == vid and i.pid == pid:
            return cv2.VideoCapture(i.index, apiPreference)
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
- [ ] Linux Support
- [ ] MacOS Support
