# type: ignore
from cv2_enumerate_cameras import enumerate_cameras, supported_backends
from cv2_enumerate_cameras.camera_info import CAP_ANY


try:
    from cv2.videoio_registry import getBackendName
except ModuleNotFoundError:
    def getBackendName(api):
        return str(api)


def main():
    for backend in [CAP_ANY, *supported_backends]:
        backend_name = getBackendName(backend)
        print(f'Enumerate using {backend_name} backend:')
        camera_info_list = enumerate_cameras(backend)
        if not camera_info_list:
            print(f"No camera on {backend_name} backend.")
            continue

        name_column_length = max(max((len(i.name) for i in camera_info_list)), 4)
        path_column_length = max(max((len(i.path) for i in camera_info_list)), 4)

        separate_line = "+-------+-" + "-" * name_column_length + "-+------+------+-" + "-" * path_column_length + "-+"
        output_rows = [
            separate_line,
            "| index | " + "name".center(name_column_length) + " | vid  | pid  | " + "path".center(path_column_length) + " |",
            separate_line
        ]
        for i in camera_info_list:
            row = f"| {i.index:5} | " + i.name.rjust(name_column_length) + " | "
            if i.vid is None:
                row += f" --  | "
            else:
                row += f"{i.vid:04X} | "
            if i.pid is None:
                row += f" --  | "
            else:
                row += f"{i.pid:04X} | "
            if i.path:
                row += i.path.rjust(path_column_length) + " |"
            else:
                row += "--".center(path_column_length) + " |"
            output_rows.append(row)
        output_rows.append(separate_line)
        print('\n'.join(output_rows))


if __name__ == '__main__':
    main()
