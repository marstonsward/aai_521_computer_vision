# Assignment 5 - Video and Real-Time Analysis

## Overview
This assignment focuses on video processing, pose estimation, and real-time object detection using computer vision techniques. Students work with OpenCV for video I/O, TensorFlow Hub's MoveNet for pose estimation, and YOLO11 for object detection.

## Environment Setup
- **Python Environment**: Use the `pytorch` mamba environment
- **Required Libraries**: 
  - OpenCV (`cv2`)
  - MediaPipe (PyTorch-compatible pose estimation)
  - Ultralytics (YOLO)
  - NumPy, Matplotlib, PIL
  - IPython.display for HTML embedding
- **Models**: 
  - MediaPipe Pose (replaces TensorFlow Hub MoveNet)
  - YOLO11n (`yolov11n.pt`) - should be downloaded and ready to use
- **Installation**: `pip install mediapipe opencv-python pillow ultralytics`

## Part 1 - Video Read/Write

Work with the "Bangkok.mp4" video file from pixabay.com to practice video I/O and processing.

### Requirements:

**a) Video Metadata Extraction**
- Read the "Bangkok.mp4" file using OpenCV (`cv2.VideoCapture`)
- Extract and display:
  - Frame Per Second (fps) - use `cap.get(cv2.CAP_PROP_FPS)`
  - Total number of frames - use `cap.get(cv2.CAP_PROP_FRAME_COUNT)`
  - Height and Width - use `cap.get(cv2.CAP_PROP_FRAME_WIDTH)` and `cap.get(cv2.CAP_PROP_FRAME_HEIGHT)`

**b) Video Display**
- Display the video in the notebook using HTML5 video player
- Use base64 encoding to embed the video
- This provides better playback than frame-by-frame OpenCV display
- Easier to use for reviewing video in notebooks (Colab or VS Code)

**c) Apply Filters (Sketch Effect)**
- Apply adaptive thresholding to create a sketch effect:
  - Use `cv2.adaptiveThreshold()` with `ADAPTIVE_THRESH_MEAN_C` and `THRESH_BINARY_INV`
  - Recommended parameters: blockSize=11, C=2
- Display 3 sample frames showing the sketch effect
- Note: VideoWriter can save full video but takes time; sample frames are sufficient

**Analysis**: Explain how adaptive thresholding works:
- Local threshold calculation vs global thresholding
- Why it acts as an edge detector
- Benefits for varying lighting conditions

## Part 2 - Pose Estimation in Video

Apply pose estimation techniques to video data using MediaPipe Pose (PyTorch-compatible alternative).

### Requirements:

- **Load MediaPipe Pose Model**: 
  - Use MediaPipe: `import mediapipe as mp; mp.solutions.pose.Pose()`
  - Model detects 33 keypoints (more detailed than MoveNet's 17): nose, eyes, ears, mouth, shoulders, elbows, wrists, hands, hips, knees, ankles, feet

- **Process GIF Frames**:
  - Load a GIF file (dance.gif) and extract frames
  - For each frame:
    - Convert to RGB (MediaPipe requires RGB)
    - Run pose estimation using `pose.process(image_rgb)`
    - Extract landmarks from results
    - Draw keypoints and skeleton on original frame using `mp.solutions.drawing_utils`
  
- **Output**:
  - Create video with pose overlay
  - Display sample frames with detected poses
  - Each landmark has format [x, y, z, visibility]

- **Visualization**:
  - Use MediaPipe's built-in drawing utilities: `mp.solutions.drawing_utils.draw_landmarks()`
  - Predefined connections for pose skeleton automatically applied
  - Visibility threshold filters unreliable keypoints

**Reference**: <https://google.github.io/mediapipe/solutions/pose>

## Part 3 - Real-Time Object Detection with YOLO11

Implement object detection using YOLO11 model with webcam input.

### Requirements:

- **Model Setup**:
  - Use YOLO 11 nano model (`yolov11n.pt`)
  - Model should be pre-downloaded and ready to use
  - Load with Ultralytics library: `YOLO('yolov11n.pt')`

- **Webcam Capture**:
  - Option 1: OpenCV's `cv2.VideoCapture(0)` for local webcam
  - Option 2: JavaScript-based capture for Google Colab (provided in assignment)

- **Detection**:
  - Capture photo(s) from webcam
  - Run YOLO detection with confidence threshold (e.g., 0.5)
  - Display results with bounding boxes, class labels, and confidence scores

### Important Implementation Notes:

**VSCode/M4 Mac Limitation**: 
- Webcam access may not work properly in VSCode on M4 Mac due to system limitations
- **Solution**: Include an on/off flag (`ENABLE_WEBCAM = False` by default)
- Code should handle both enabled/disabled scenarios gracefully
- Print informative messages about webcam status

**Alternative Testing**:
- Test detection on video frames instead of webcam
- Use existing video files (e.g., Bangkok.mp4) to demonstrate functionality
- This ensures code can be evaluated even without webcam access

**Code Structure**:
```python
ENABLE_WEBCAM = False  # Set to True to enable
if ENABLE_WEBCAM:
    # Webcam capture and detection code
else:
    # Informative message about why it's disabled
```

## Extra Credit - Real-Time Pose Estimator

Design and implement a real-time pose estimation system combining webcam capture with pose detection.

### Requirements:

- **Core Functionality**:
  - Combine webcam video capture with MediaPipe Pose estimation
  - Process frames continuously in a loop
  - Display pose skeleton overlay in real-time
  - Show frame count or FPS on display

- **Implementation Details**:
  - Use `cv2.VideoCapture(0)` for webcam
  - Process each frame through MediaPipe Pose
  - Use MediaPipe's drawing utilities for automatic skeleton rendering
  - Display using `cv2.imshow()`
  - Include exit mechanism (e.g., press 'q' to quit)

- **Error Handling**:
  - Check if webcam opens successfully
  - Handle frame read failures gracefully
  - Release resources properly on exit

- **Configuration Flag**:
  - Include `ENABLE_REALTIME_POSE = False` flag
  - Same considerations as Part 3 for VSCode/M4 Mac

- **Alternative Demonstration**:
  - If webcam unavailable, demonstrate concept using video file
  - Process first N frames of Bangkok.mp4 with pose estimation
  - This simulates real-time processing without requiring webcam

### Expected Behavior:
- When enabled and webcam available: Live pose detection window
- When disabled or webcam unavailable: Demo using video file with informative messages
- All scenarios should run without errors

## Code Organization

Follow this structure for clean, maintainable code:

1. **Imports Section**: All imports in one cell at the top
2. **Constants and Configuration**: File paths, model URLs, configuration flags
3. **Helper Functions**: Reusable functions for video embedding, pose drawing, etc.
4. **Part 1**: Video metadata, display, and filtering
5. **Part 2**: Pose estimation on GIF
6. **Part 3**: YOLO object detection
7. **Extra Credit**: Real-time pose estimation

### Key Principles:
- **Update in place**: Modify existing cells rather than appending
- **No broken cells**: Test each cell before moving to the next
- **Clear separation**: Each part clearly marked with markdown headers
- **Reusable code**: Functions defined once and used throughout

## Technical Implementation Notes

### Video I/O Best Practices:
- Use `Path` objects for file paths and `.resolve()` for absolute paths
- Always check if `VideoCapture` opened successfully
- Release video capture objects when done: `cap.release()`
- For writing videos, use appropriate fourcc codec (e.g., 'mp4v' for .mp4)

### Pose Estimation Details:
- MediaPipe input: RGB image (any size, automatically handled)
- Output: 33 landmarks with [x, y, z, visibility] for each point
- Coordinates are normalized (0-1), multiply by image dimensions for pixel positions
- Use visibility threshold (0.5) to filter unreliable keypoints
- Z-coordinate represents depth relative to hips

### YOLO Usage:
- Direct prediction: `results = model(image, conf=threshold)`
- Access detections: `results[0].boxes`
- Each box has: `cls` (class ID), `conf` (confidence), coordinates
- Get class names: `model.names[class_id]`
- Built-in plotting: `results[0].plot()`

## Guidance from Lab 5 (Lab5_video_processing.ipynb)

The provided lab notebook demonstrates:

1. **Video I/O**:
   - Reading: `cv2.VideoCapture('filename.avi')`
   - Writing: `cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))`
   - Metadata: `cap.get(cv2.CAP_PROP_*)`

2. **Background Subtraction**:
   - `cv2.createBackgroundSubtractorKNN()` for foreground/background separation

3. **Object Tracking**:
   - **Kalman Filter**: Predict and correct object positions
   - **MeanShift**: Track objects based on color distribution

4. **Displaying Video in Notebooks**:
   - Embed video using `IPython.display.HTML` with base64 encoding
   - Useful for Colab or VS Code

These techniques are especially relevant for Part 1 video handling and can be referenced for tracking concepts.

## Testing and Validation

### Part 1 Checklist:
- [ ] Video opens successfully and metadata displays correctly
- [ ] HTML5 video player shows embedded video
- [ ] Three sketch frames display with clear edge effects

### Part 2 Checklist:
- [ ] MediaPipe Pose model loads without errors
- [ ] GIF frames extract correctly
- [ ] Pose keypoints and skeleton draw on frames
- [ ] Output video created and displays

### Part 3 Checklist:
- [ ] YOLO11 model loads successfully
- [ ] Detection works on test images/frames
- [ ] Bounding boxes and labels display correctly
- [ ] Webcam flag controls behavior appropriately

### Extra Credit Checklist:
- [ ] Real-time pose processing implemented (or simulated)
- [ ] Frame display shows pose overlay
- [ ] Exit mechanism works properly
- [ ] Alternative demo provided if webcam unavailable

## Common Issues and Solutions

**Issue**: OpenCV can't open video file
- **Solution**: Use absolute paths with `Path.resolve()`, check file exists

**Issue**: Webcam doesn't work in VSCode
- **Solution**: Expected on M4 Mac, use flag to disable and test with video files

**Issue**: MediaPipe model not working
- **Solution**: Ensure `pip install mediapipe opencv-python` completed successfully

**Issue**: YOLO model not found
- **Solution**: Ensure `yolov11n.pt` is in correct directory or provide full path

**Issue**: Pose keypoints not visible
- **Solution**: Lower confidence threshold, check coordinate scaling

**Issue**: Video embed doesn't display
- **Solution**: Ensure base64 encoding is correct, check video file size

## Submission Requirements

Submit a complete Jupyter notebook with:
1. All code cells executed successfully
2. Output visible for all parts
3. Clear markdown explanations for each section
4. Analysis and observations included
5. Configuration flags set appropriately for evaluation environment
6. No broken or duplicate cells

The notebook should run from top to bottom without errors when executed in the pytorch environment.
