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
            # camera_params = json.loads(json_input)
            # intrisic_matrix = [np.array(R) for R in dict["K"]]
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
        angle[1] += (image_index - central_index) // 2 * 20
        # angle[2] *= -0.7
        # angle[0] *= -0.1
        rotation = R.from_euler('zyx', angle, degrees=True)
        print("Image index: " + str(image_index))
        print(rotation.as_matrix())
        print("Angles:")
        print(angle)
        print((image_index - central_index) // 2 * 30)
 #        return np.array([[ 0.28652248,  0.15573756,  0.83455145],
 # [-0.114048,    0.6318925,  -0.14520025],
 # [-0.4678647,  -0.02612399,  0.11794481]])
        return rotation.as_matrix()

    def euler_angles(self, cameras):
        angles = []
        for i in cameras:
            angle = R.from_matrix(i)
            angles.append(angle.as_euler('zyx',degrees=True))

        print(angles)

