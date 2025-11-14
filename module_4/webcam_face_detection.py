#!/usr/bin/env python3
"""
Standalone webcam face detection script for M4 Mac
Run this from terminal if Jupyter webcam fails
"""

import cv2
import time

print("="*60)
print("WEBCAM FACE DETECTION - STANDALONE SCRIPT")
print("="*60)
print("\nThis script runs outside Jupyter to avoid camera access issues")
print("Press 'q' in the video window to quit\n")

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

if face_cascade.empty() or eye_cascade.empty():
    print("ERROR: Haar cascade XML files not found")
    print("Make sure you're running from the module_4 directory")
    exit(1)

print("✓ Haar cascades loaded")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open webcam")
    exit(1)

print("✓ Webcam opened")

# Initialize camera with retry
print("⏳ Initializing camera...")
camera_ready = False
for attempt in range(20):  # Try for up to 6 seconds
    time.sleep(0.3)
    ret, frame = cap.read()
    if ret and frame is not None:
        camera_ready = True
        print(f"✓ Camera ready! Resolution: {frame.shape[1]}x{frame.shape[0]}\n")
        break

if not camera_ready:
    print("ERROR: Camera timeout - could not capture frames")
    cap.release()
    exit(1)

# Main detection loop
print("Starting face detection... Press 'q' to quit\n")
frame_count = 0
face_count = 0

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        
        # Detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) > 0:
            face_count += 1
        
        # Draw detections
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Detect eyes
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # Display info
        cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'q' to quit", (10, 70), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Face Detection - Press q to quit', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nInterrupted by user")

finally:
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n{'='*60}")
    print(f"SESSION COMPLETED")
    print(f"{'='*60}")
    print(f"Total frames: {frame_count}")
    print(f"Frames with faces: {face_count}")
    if frame_count > 0:
        print(f"Detection rate: {face_count/frame_count*100:.1f}%")
    print(f"{'='*60}\n")
