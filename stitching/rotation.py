import json
import numpy as np
from scipy.spatial.transform import Rotation as R


class Rotation:

    DEFAULT_ROTATION = None

    def __init__(self, json_input):
        self.estimated_cameras = None
        self.rotation_mode = True if json_input else False
        if json_input:
            with open(json_input, 'r') as j:
                camera_params = json.loads(j.read())
            self.collected_cameras = [np.array(rotation) for rotation in camera_params["rotations"]]
            self.angles = [np.array(angle) for angle in camera_params["angles"]]

    def detect_central_image(self, estimated_cameras, img_names):
        self.estimated_cameras = estimated_cameras
        central_rotation_matrix = np.array([[1.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0],
                                            [0.0, 0.0, 1.0]]).astype(np.float32)
        for i in range(len(self.estimated_cameras)):
            if (self.estimated_cameras[i].R == central_rotation_matrix).all():
                return img_names[i]
        return 0

    def calculate_rotation_matrix_to_central_image(self, central_index, image_index):
        if central_index == image_index:
            return self.collected_cameras[image_index]
        angle = [i * 180 / np.pi for i in self.angles[image_index] - self.angles[central_index]]
        rotation = R.from_euler('zyx', angle, degrees=True)
        return rotation.as_matrix()

    @staticmethod
    def convert_to_euler_angles(cameras):
        angles = []
        for i in cameras:
            angle = R.from_matrix(i)
            angles.append(angle.as_euler('zyx',degrees=True))

        return angles
