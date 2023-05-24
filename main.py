import cv2
from stitching import Stitcher
import os



# parser = argparse.ArgumentParser(
#     description="Create panoramas from a set of images. \
#                  All the images must be in the same directory."
# )
# parser.add_argument(dest="data_dir", help="directory containing the images")

if __name__ == '__main__':
    # args = vars(parser.parse_args())
    # images = get_image_paths('data')
    cv2.ocl.setUseOpenCL(False)
    dir = 'C:\\Users\\hieu.nguyen20_onemou\\Desktop\\OMRE Tech\\stitching-tutorial\\data\\2104.F1'
    images = [os.path.join(dir, x) for x in os.listdir(dir)]
    settings = {"rotation": "data/matrices/rotation_matrices.json", "matches_graph_dot_file": "graph.txt", "crop": False}
    stitcher = Stitcher(**settings)

    # imgs = []
    # for i in range(len(images)):
    #     imgs.append(cv2.imread(images[i]))
    #     imgs[i] = cv2.resize(imgs[i], (0, 0), fx=0.4, fy=0.4)
    # stitchy = cv2.Stitcher.create()
    # (dummy, panorama) = stitchy.stitch(imgs)
    panorama = stitcher.stitch(images)


    # h, _, _ = panorama.shape
    # color = [255, 255, 255]
    # cv2.imwrite("result/out_1.jpg", cv2.copyMakeBorder(panorama, int(h * 0.35), int(h * 0.35), 0, 0, cv2.BORDER_CONSTANT, value = color))
    cv2.imwrite("result/out.jpg", panorama)