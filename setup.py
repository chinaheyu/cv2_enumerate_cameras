from setuptools import Extension, setup, find_packages
import platform

major, minor, _ = platform.python_version_tuple()
version = (int(major), int(minor))
system = platform.system()

if system == 'Windows':
    if version < (3, 7):
        setup(
            name='cv2_enumerate_cameras',
            description='Enumerate / List / Find / Detect / Search index for opencv VideoCapture.',
            version='1.1.4',
            package_dir={"": "src"},
            packages=find_packages('src'),
            ext_modules=[
                Extension(
                    name="cv2_enumerate_cameras._cv2_enumerate_cameras",
                    sources=["src/cv2_enumerate_cameras/cv2_enumerate_cameras.cpp"]
                )
            ]
        )
    else:
        setup(
            ext_modules=[
                Extension(
                    name="cv2_enumerate_cameras._cv2_enumerate_cameras",
                    sources=["src/cv2_enumerate_cameras/cv2_enumerate_cameras.cpp"]
                )
            ]
        )

if system == 'Linux':
    setup()
