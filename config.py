"""
All settings are kept here, so you can tune the project
without touching the main code.
"""

# Which camera to use (0 = default laptop webcam)
CAMERA_INDEX = 0

# If EAR (Eye Aspect Ratio) goes below this value, the eye is treated as closed.
# Normal open eye is about 0.28 - 0.35. Closed eye is below 0.20.
EAR_THRESHOLD = 0.21

# Number of continuous frames the eyes must stay closed before the alarm rings.
# At about 30 frames per second, 20 frames is roughly 0.7 seconds.
CLOSED_FRAMES_LIMIT = 20
