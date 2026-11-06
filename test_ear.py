"""
A small test to check that the EAR calculation works.
Run with:  python test_ear.py
"""

from eye_utils import calculate_ear

# Open eye: upper and lower eyelids are far apart
open_eye = [(0, 5), (3, 3.5), (7, 3.5), (10, 5), (7, 6.5), (3, 6.5)]

# Closed eye: eyelids are almost touching
closed_eye = [(0, 5), (3, 4.8), (7, 4.8), (10, 5), (7, 5.2), (3, 5.2)]

open_ear = calculate_ear(open_eye)
closed_ear = calculate_ear(closed_eye)

print("Open eye EAR  :", round(open_ear, 2))
print("Closed eye EAR:", round(closed_ear, 2))

assert open_ear > 0.25, "Open eye EAR should be high"
assert closed_ear < 0.15, "Closed eye EAR should be low"
assert open_ear > closed_ear

print("All tests passed!")
