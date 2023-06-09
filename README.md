# Image Stitching Project

This project is based on [stitching](https://github.com/OpenStitching/stitching), a Python package for fast and robust image stitching. Our goal is to add features that can help stitch images based on camera rotation.

## Installation

To use this project, you will need to install the following dependencies:

- `numpy`
- `opencv-python`

You can install these dependencies using the following command:

```bash
pip install requirements.txt
```

## Usage

To use this project, you can import the `stitching` module and call `sitcher.stitch` function. For example:

```python
    dir = "Your path to images directory"
    images = [os.path.join(dir, x) for x in os.listdir(dir)]
    settings = {"rotation": "data/matrices/rotation_matrices.json", "matches_graph_dot_file": "graph.txt", "crop": False}
    stitcher = Stitcher(**settings)
    panorama = stitcher.stitch(images)

    cv2.imwrite("result/out.jpg", panorama)
```

## Tutorial

Image stitching for low feature images require information about extrinsic and intrisic matrix of the camera.