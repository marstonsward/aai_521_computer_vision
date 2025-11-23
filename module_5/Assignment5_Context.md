# Assignment 5 - Video and Real-time Analysis - Context & Guidelines

## Overview

This assignment focuses on video processing, pose estimation, and real-time object detection using computer vision techniques.

## Part 1 - Video Read/Write

### Objective

Read and process video files using Python and OpenCV, applying basic video manipulation and filtering techniques.

### Tasks

**a) Video Metadata Extraction**

- Read the file "Bangkok.mp4" using OpenCV
- Extract and print metadata:
  - Frame Per Second (fps)
  - Total number of frames
  - Height and Width of the video

**b) Video Playback**

- Multiple playback methods available in different environments
- For Google Colab: Use HTML embedding with base64 encoding
- For local execution: Use direct display methods

**c) Video Filtering**

- Apply adaptive threshold mean and threshold binary inverse filters
- Create a "sketch" version of the video
- Instead of processing entire video, display 3 sample frames
- Optional: Use VideoWriter to save full processed video (time-consuming)

## Part 2 - Pose Estimation in Video

### Objective

Apply pose estimation techniques to video files, detecting human body keypoints across frames.

### Approach

- **Framework**: PyTorch-based pose estimation models
- **Input Format**: GIF or video file
- **Model Options**:
  - MediaPipe Pose (lightweight, real-time capable)
  - YOLOv8-pose (YOLO with pose detection)
  - OpenPose-compatible models

### Tasks

- Load a pre-trained pose estimation model
- Process video frames sequentially
- Detect 17+ body keypoints per frame
- Draw skeleton connections
- Visualize and save results

### Implementation Notes

- Use PyTorch instead of TensorFlow for better M1/M2/M4 Silicon support
- Ensure compatibility with both Colab and local Mac environments
- Handle different video formats (GIF, MP4, AVI)

## Part 3 - Real-time Webcam Object Detection

### Objective

Implement real-time object detection using webcam input with YOLO11.

### Requirements

- **Model**: YOLOv11 (yolo11n.pt - nano version for speed)
- **Framework**: Ultralytics library with PyTorch backend
- **Input**: Live webcam feed

### Platform-Specific Implementation

#### For Local Execution (M4 Silicon Mac)

- Use `cv2.VideoCapture(0)` for direct webcam access
- Leverage Metal Performance Shaders (MPS) backend
- Test webcam availability in VS Code/Jupyter

#### For Google Colab

- Use JavaScript Camera Capture snippet
- Base64 encode captured frames
- Process images server-side

### Tasks

1. Load YOLOv11 model
2. Access webcam (method depends on environment)
3. Capture frame/photo
4. Run object detection
5. Display annotated results

### Control Interface

- **Start/Stop Button**: Add interactive controls for live feed
- **For Jupyter/Colab**: Use ipywidgets buttons
- **For VS Code**: Use interactive cell outputs

## Extra Credit - Real-Time Pose Estimator

### Objective

Build a live pose estimation system that processes webcam feed in real-time.

### Requirements

- Combine webcam capture with pose estimation
- Process frames at interactive frame rates (>15 FPS)
- Add start/stop controls
- Display skeleton overlay in real-time

### Implementation Considerations

- Use lightweight models (MediaPipe or YOLOv8-pose nano)
- Optimize for M4 Silicon using MPS backend
- Implement frame skipping if needed for performance
- Add FPS counter for monitoring

## Technical Requirements

### Environment Setup

**Required Packages:**

```bash
# Core dependencies
pip install torch torchvision torchaudio
pip install opencv-python
pip install ultralytics
pip install mediapipe
pip install numpy
pip install matplotlib
pip install ipywidgets

# For video processing
pip install imageio
pip install imageio-ffmpeg

# For Jupyter/Colab
pip install ipython
```

### PyTorch Configuration

**For M4 Silicon (MPS Backend):**

```python
import torch
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
```

**For Google Colab (CUDA):**

```python
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

### Webcam Access Patterns

**Local (VS Code/Jupyter):**

```python
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()
```

**Google Colab:**

```python
from google.colab.patches import cv2_imshow
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
    js = Javascript('''
        async function takePhoto(quality) {
            // JavaScript camera capture code
        }
    ''')
    display(js)
    data = eval_js('takePhoto({})'.format(quality))
    binary = b64decode(data.split(',')[1])
    with open(filename, 'wb') as f:
        f.write(binary)
    return filename
```

## Portability Strategy

### Cross-Platform Code Structure

```python
import sys
import torch

# Detect environment
IS_COLAB = 'google.colab' in sys.modules
IS_MAC_SILICON = torch.backends.mps.is_available()

# Configure device
if IS_COLAB and torch.cuda.is_available():
    device = torch.device("cuda")
elif IS_MAC_SILICON:
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"Running on: {device}")
```

### Webcam Handler

```python
class WebcamHandler:
    def __init__(self):
        self.is_colab = 'google.colab' in sys.modules
        
    def capture_frame(self):
        if self.is_colab:
            return self._capture_colab()
        else:
            return self._capture_local()
    
    def _capture_local(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None
    
    def _capture_colab(self):
        # JavaScript-based capture
        pass
```

## Interactive Controls

### Start/Stop Button Implementation

```python
import ipywidgets as widgets
from IPython.display import display

# Create buttons
start_button = widgets.Button(description="Start Detection")
stop_button = widgets.Button(description="Stop Detection")

# State management
is_running = False

def on_start_click(b):
    global is_running
    is_running = True
    # Start detection loop

def on_stop_click(b):
    global is_running
    is_running = False
    # Stop detection loop

start_button.on_click(on_start_click)
stop_button.on_click(on_stop_click)

display(widgets.HBox([start_button, stop_button]))
```

## Performance Optimization

### For M4 Silicon

- Enable MPS backend for GPU acceleration
- Use smaller model variants (nano/small)
- Consider frame resolution reduction
- Implement frame skipping if needed

### For Google Colab

- Utilize free GPU runtime (T4)
- Batch process frames when possible
- Cache model weights to avoid reloading

## Deliverables

1. **Notebook with all three parts implemented**
2. **PyTorch-based implementations** (not TensorFlow)
3. **Cross-platform compatibility** (Colab and M4 Mac)
4. **Interactive controls** for live detection
5. **Documentation and analysis** of techniques used
6. **Sample outputs** (processed videos, detected poses, screenshots)

## Tips for Success

- Test webcam access early in both environments
- Use try-except blocks for environment-specific code
- Print device information for debugging
- Save intermediate results frequently
- Use small test videos/images first
- Monitor resource usage (RAM, GPU)
- Add progress indicators for long operations
