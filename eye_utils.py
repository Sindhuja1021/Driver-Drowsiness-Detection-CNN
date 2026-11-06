"""
Helper functions to calculate the Eye Aspect Ratio (EAR).

EAR formula:
    EAR = ( |p2 - p6| + |p3 - p5| ) / ( 2 * |p1 - p4| )

An eye has 6 important points:
    p1 = outer corner      p4 = inner corner
    p2, p3 = upper eyelid  p5, p6 = lower eyelid

When the eye is open, the vertical distances are large -> EAR is high.
When the eye is closed, the vertical distances become small -> EAR is low.
"""

import math

# MediaPipe Face Mesh landmark numbers for each eye
# Order: p1, p2, p3, p4, p5, p6
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
LEFT_EYE = [362, 385, 387, 263, 373, 380]


def distance(point_a, point_b):
    """Straight-line distance between two (x, y) points."""
    return math.dist(point_a, point_b)


def calculate_ear(eye_points):
    """Takes 6 (x, y) points of one eye and returns its EAR value."""
    p1, p2, p3, p4, p5, p6 = eye_points

    vertical_1 = distance(p2, p6)
    vertical_2 = distance(p3, p5)
    horizontal = distance(p1, p4)

    return (vertical_1 + vertical_2) / (2.0 * horizontal)


def get_eye_points(face_landmarks, eye_indices, frame_width, frame_height):
    """
    MediaPipe gives landmark positions between 0 and 1.
    This function converts them into real pixel positions (x, y).
    """
    points = []
    for index in eye_indices:
        landmark = face_landmarks[index]
        x = int(landmark.x * frame_width)
        y = int(landmark.y * frame_height)
        points.append((x, y))
    return points
