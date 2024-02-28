from . import enumerate_cameras, CAP_MSMF, CAP_DSHOW


if __name__ == '__main__':
    print(f'Enumerate using MSMF backend:')
    for i in enumerate_cameras(CAP_MSMF):
        print(i)
    print()
    print(f'Enumerate using DSHOW backend:')
    for i in enumerate_cameras(CAP_DSHOW):
        print(i)
