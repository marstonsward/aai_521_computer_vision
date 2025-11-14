# Webcam Setup Guide for macOS (M4/Apple Silicon)

## ✅ Your Camera is Working!

The diagnostic test confirmed your M4 Mac's camera is functional with OpenCV.

## Important Notes for M4 Mac

### 1. Camera Permissions (macOS Sequoia/Sonoma)
On macOS, apps need explicit permission to access the camera:

**To Grant Permission:**
1. Open **System Settings**
2. Go to **Privacy & Security** → **Camera**
3. Enable camera access for:
   - **Terminal.app** (if running from terminal)
   - **Python** (may appear after first attempt)
   - **iTerm2** (if using iTerm)
   - **Visual Studio Code** (if using VS Code)
   - **JupyterLab/Jupyter** (if running Jupyter)

**Important:** After granting permission, you must **close and reopen** your terminal/IDE!

### 2. Camera Initialization Timing
M4 Macs may need a brief delay after opening the camera before capturing frames:

```python
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(0.5)  # Brief delay for camera initialization
ret, frame = cap.read()
```

### 3. Running from Jupyter Notebook
When running the assignment notebook:
- Use the `pytorch` conda environment (already active)
- The notebook includes proper error handling
- If webcam fails, use the alternative static photo test

### 4. Testing Your Setup

Run the diagnostic script:
```bash
conda run -n pytorch python test_camera_simple.py
```

Expected output:
```
✅ SUCCESS: Camera 0 is fully functional!
```

## Troubleshooting

### Problem: "Camera opened but couldn't capture frame"
**Solution:** Add `time.sleep(0.5)` after `VideoCapture(0)`

### Problem: "Could not access webcam"
**Solutions:**
1. Check camera permissions (see above)
2. Close other apps using camera (Zoom, Teams, FaceTime, Photo Booth)
3. Restart terminal/IDE after granting permissions
4. Try different camera index (usually 0, but try 1 or 2)

### Problem: Permission dialog doesn't appear
**Solution:** 
```bash
# Reset camera permissions (macOS will ask again)
tccutil reset Camera
```
Then restart your terminal and run the notebook.

### Alternative: Static Photo Test
If webcam access continues to fail, you can:
1. Take a photo with Photo Booth
2. Save as `test_photo.jpg` in the module_4 directory
3. Run the "Part 2b Alternative" cell in the notebook

## Camera Specifications (Your M4 Mac)
- Resolution: 1920x1080 (Full HD)
- Color: BGR format (3 channels)
- Camera Index: 0

## For the Assignment

The notebook includes:
- ✅ Automatic camera detection and error handling
- ✅ Helpful error messages with troubleshooting steps
- ✅ Alternative static photo testing option
- ✅ Proper initialization timing for M4 Mac

You're all set to complete Part 2b of the assignment!
