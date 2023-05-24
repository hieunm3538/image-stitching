import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img1 = cv.imread('data/2303.1511/09.JPG')
    img2 = cv.imread('data/2303.1511/10.JPG')

    cameraMatrix = np.array([[489.09710825, 0., 335.5],
                             [0., 489.09710825, 447.],
                             [0., 0., 1.]])

    R = np.array([[0.9429074, 0.0551263, -0.04662883],
                  [-0.02326928, 0.8150798, -0.56174123],
                  [0.02462351, 0.2714183, 0.8126464]])

    R2 = np.array([[1., 0., 0.],
                    [0., 1., 0.],
                    [0., 0., 1.]])

    H = cameraMatrix.dot(R).dot(np.linalg.inv(cameraMatrix))
    H = H / H[2][2]

    img_stitch = cv.warpPerspective(img2, H, (img2.shape[1], img2.shape[0]))
    img_stitch[img_stitch.shape[0] - img1.shape[0] : img_stitch.shape[0], img_stitch.shape[1] - img1.shape[1] : img_stitch.shape[1]] = img1

    cv.imwrite("result/rotation.jpg", img_stitch)
