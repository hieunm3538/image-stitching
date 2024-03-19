import cv2
from stitching import Stitcher
import os


if __name__ == '__main__':
    # args = vars(parser.parse_args())
    # images = get_image_paths('data')
    cv2.ocl.setUseOpenCL(False)
    images_path = 'data/22032023'
    images = [os.path.join(images_path, x) for x in os.listdir(images_path)]
    settings = {"rotation": "data/matrices/rotation_matrices.json", "matches_graph_dot_file": "graph.txt", "crop": False}
    stitcher = Stitcher(**settings)
    panorama = stitcher.stitch(images)
    cv2.imwrite("result/out.jpg", panorama)