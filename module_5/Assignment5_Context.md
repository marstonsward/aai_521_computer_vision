# Assignment 5 - Video and real-time analysis

## Part 1 - Video read/write

We start with reading a video in python and apply some basic tools on it. The video chosen for this part is from pixabay.com. A resource of free video/image and sound clips.

a) Read the file “Bangkok.mp4” file using OpenCV. Find the relevant commands to find the video’s metadata and print out following information about the video:

- Frame Per second (fps)
- Total number of frames
- Height and Width of the video

b) There are many ways to play this file inside google colab. If you just use OpenCV, it will be shown frame by frame. Another approach is to use embedded version using HTML library. For the rest of the steps, it would be easier to use html version for playing the video.

c) Let’s apply some filters on the video file. Use adaptive_theshold_mean and threshold_binary_inv, to create a sketch version of the video. You can use Videowriter command to save the output but it takes quite some time. Instead, only print 3 frames of the video.

## Part 2 - Pose estimation in video

Return to the functions that were provided in previous assignments to estimate the pose in images. This time, we want to experience it in a video file. For that, we will use **MediaPipe Pose** (PyTorch-compatible alternative to TensorFlow Hub's MoveNet) and estimate the pose of the girl in video. The format of the video this time is gif.

**Installation**: `pip install mediapipe opencv-python`
**Reference**: <https://google.github.io/mediapipe/solutions/pose>

## Part 3 - Using webcam video

Now, we want to use webcam and make object detection on real-time. As you have seen in previous modules, the first step is to have a pre-trained model and use it for future classifications. My recommendation is to use the YOLO 11 model for this part (yolov11n.pt).

Another piece that we need is a script to connect our webcam to python to make a live object detection application. We will be using the code snippet for Camera Capture which runs JavaScript code to utilize your computer's webcam. Please refer to previous assignment to copy the code here.

Use a code to detect the camera and take a photo and finally detect the objects in the photo.

## Extra credit

Design a Real-Time pose estimator.

## Guidance from Lab 5 (Lab5_video_processing.ipynb)

The provided lab notebook `Lab5_video_processing.ipynb` demonstrates several key concepts relevant to this assignment:

1.  **Video I/O**:
    -   Reading video: `cv2.VideoCapture('filename.avi')`
    -   Writing video: `cv2.VideoWriter('output.mp4', ...)`
    -   Getting metadata: `cap.get(cv2.CAP_PROP_FPS)`, `cap.get(cv2.CAP_PROP_FRAME_COUNT)`, etc.

2.  **Background Subtraction**:
    -   Using `cv2.createBackgroundSubtractorKNN()` to separate foreground objects from the background.

3.  **Object Tracking**:
    -   **Kalman Filter**: The `Pedestrian` class implements a Kalman Filter (`cv2.KalmanFilter`) to predict and correct the position of tracked objects.
    -   **MeanShift**: Uses `cv2.meanShift` with a histogram back-projection to track objects based on color distribution.

4.  **Displaying Video in Notebooks**:
    -   The lab shows how to embed a video player using `IPython.display.HTML` and base64 encoding, which is useful for viewing results in Colab or VS Code.

You can use these techniques, especially the video reading/writing and display methods, for Part 1. The tracking concepts might be useful references for the pose estimation or extra credit parts.

