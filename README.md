# Low Feature Images Stitching
 
This project is based on [stitching](https://github.com/OpenStitching/stitching), a Python package for fast and robust image stitching. 
When performing image stitching on a set of images that contain multiple low-feature images, such as a blank wall, our stitching algorithm base on feature matching encounters a challenge as there are no features for matching. 

In order to overcome this obstacle, I suggest employing camera rotation to populate the Rotation Matrix of the no-feature image. 
The Intrinsic Matrix is computed based on the matched images. 

It is important to note that this work is currently in the form of a preliminary draft for this idea.

## Installation

To use this project, you will need to install the following dependencies:

- `numpy`
- `opencv-python`
- `stitching`

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
My workflow is presented as below:
1. Run feature detection and feature matching on images set.
2. Extract matching images set, detect central images.
3. Build rotation matrices for non-matched images, using rotation matrix get from devices.
4. Adding images back to set with according matrix.
5. Run transform images to plane, then blend and crop.

## Resources and Result

Images set and camera rotation matrices are captured by One Mount Real Estate.

Output is not optimized due to the fact this is the draft based on ideas about camera rotation matrices. Please fell free to create pull request if you want to improve it. 

Thanks for reading!
