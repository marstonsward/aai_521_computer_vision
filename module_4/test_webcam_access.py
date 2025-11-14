#!/usr/bin/env python3
"""
Webcam Access Diagnostic Tool for macOS
Tests camera permissions and provides troubleshooting steps
"""

import cv2
import sys
import subprocess
import platform

print("="*60)
print("WEBCAM ACCESS DIAGNOSTIC TOOL")
print("="*60)
print()

# Check OS
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Python Version: {sys.version.split()[0]}")
print(f"OpenCV Version: {cv2.__version__}")
print()

# Check if running on macOS
if platform.system() != "Darwin":
    print("⚠️  This diagnostic is designed for macOS")
    print()

print("Attempting to access webcam...")
print()

# Try to open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ WEBCAM ACCESS FAILED")
    print()
    print("Common causes on macOS:")
    print()
    print("1. PERMISSION DENIED")
    print("   → Open System Settings")
    print("   → Go to Privacy & Security → Camera")
    print("   → Enable camera access for:")
    print("     • Terminal (if running from terminal)")
    print("     • Python")
    print("     • iTerm (if using iTerm)")
    print("     • VS Code (if using VS Code)")
    print("     • Jupyter (if running Jupyter)")
    print()
    print("2. CAMERA IN USE")
    print("   → Close other apps using the camera:")
    print("     • Zoom, Teams, Skype, FaceTime")
    print("     • Other browser tabs with camera access")
    print("     • Photo Booth")
    print()
    print("3. RESTART REQUIRED")
    print("   → After granting permissions, you may need to:")
    print("     • Close and reopen Terminal/IDE")
    print("     • Or restart Python kernel")
    print()
    print("TO FIX:")
    print("1. Open System Settings")
    print("2. Click Privacy & Security in sidebar")
    print("3. Click Camera")
    print("4. Toggle ON for Terminal/Python/Your IDE")
    print("5. Restart your terminal/IDE")
    print("6. Run this script again")
    print()
    
else:
    print("✅ WEBCAM ACCESS SUCCESSFUL!")
    print()
    
    # Try to read a frame
    ret, frame = cap.read()
    
    if ret:
        print(f"✓ Frame captured successfully")
        print(f"✓ Resolution: {frame.shape[1]}x{frame.shape[0]}")
        print(f"✓ Color channels: {frame.shape[2]}")
        print()
        print("Your webcam is working correctly!")
        print()
        print("To test face detection:")
        print("1. Run the Jupyter notebook")
        print("2. Execute the webcam detection cell")
        print("3. Your face should be detected with a blue rectangle")
        print()
    else:
        print("⚠️  Could open camera but failed to capture frame")
        print("This might indicate a hardware issue")
        print()
    
    cap.release()

print("="*60)
print()

# Offer to check which processes are using the camera (macOS specific)
if platform.system() == "Darwin":
    print("Checking for processes using the camera...")
    try:
        result = subprocess.run(
            ["lsof", "|", "grep", "AppleCamera"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.stdout:
            print("Processes using camera:")
            print(result.stdout)
        else:
            print("No other processes detected using camera")
    except:
        pass
    print()

sys.exit(0 if cap.isOpened() else 1)
