🎨 VisionDraw: Motion-to-Canvas Tracker
VisionDraw is a Python application that uses real-time object tracking to create a digital drawing board. It identifies a user-defined target and translates its spatial movement into a persistent trail on a separate drawing window.

✨ Features
Custom ROI Selection: Manually select any object to track (your face, a marker, or a specific colored item).

Legacy MOSSE Tracking: Uses the MOSSE (Minimum Output Sum of Squared Error) tracker, optimized for high speed and responsiveness.

Dual-Window Interface: * Tracker Window: Shows the live camera feed with the active tracking bounding box.

Draw Screen: A dedicated black canvas where your movements are recorded as white brushstrokes.

Real-time Interaction: Features instant clearing and re-calibration.

🛠️ Installation
1. Prerequisites

You will need Python 3.x installed.

2. Required Libraries

This project requires opencv-contrib-python (which includes the legacy tracking modules) and numpy.

Bash
pip install opencv-contrib-python numpy
🚀 How to Use
Launch the App: Run the script from your terminal:

Bash
python your_script_name.py
Initialize Tracking: * Press the 'r' key.

A static frame will appear. Click and drag your mouse to draw a box around the object you want to track.

Press Enter or Space to confirm the selection.

Draw: Move the object around the camera's field of view. A white line will appear on the "Draw Screen" following the center of your object.

Controls:

r: Re-select a new object/reset tracking.

c: Clear the drawing canvas.

q: Quit the application.

📂 Code Logic Breakdown
Tracking Algorithm

The script utilizes cv2.legacy.TrackerMOSSE_create(). While newer trackers exist, MOSSE is used here because it is incredibly fast, allowing for a smooth, lag-free drawing experience even on older hardware.

Canvas Mapping

A separate NumPy array (canvas) acts as a persistent memory of your movements.

Line Continuity: The script calculates the "center" of the tracking box and draws a line between the current center and the prev_center (the position in the last frame). This ensures the trail is a solid line rather than a series of disconnected dots.

💡 Tips for Better Performance
High Contrast: Use an object that stands out from your background (e.g., a red ball against a white wall).

Lighting: Ensure your room is well-lit to reduce "noise" in the camera feed, which can cause the tracker to lose the object.

Steady Movement: While MOSSE is fast, extremely rapid movements might cause the tracker to lose its target.
