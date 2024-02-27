from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="_cv2_enumerate_cameras",
            packages=['cv2_enumerate_cameras'],
            sources=["cv2_enumerate_cameras.cpp"]
        ),
    ]
)
