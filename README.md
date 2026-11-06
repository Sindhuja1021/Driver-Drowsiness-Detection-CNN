# Driver Drowsiness Detection

A simple Python project that watches the driver's eyes through a webcam
and rings an alarm if the eyes stay closed for too long.

## How it works

1. The webcam captures video frame by frame (OpenCV).
2. MediaPipe Face Mesh finds the face and the eye landmark points.
3. We calculate the **Eye Aspect Ratio (EAR)** for both eyes.

   `EAR = ( |p2 - p6| + |p3 - p5| ) / ( 2 * |p1 - p4| )`

4. Open eye -> EAR is high (about 0.30). Closed eye -> EAR is low (below 0.20).
5. If EAR stays below the threshold for 20 frames in a row, the alarm rings.

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Main program: camera loop, detection, alert |
| `eye_utils.py` | EAR formula and landmark helper functions |
| `alarm.py` | Creates and plays the beep sound |
| `config.py` | Settings (threshold, frame limit, camera) |
| `test_ear.py` | Small test for the EAR formula |
| `requirements.txt` | Libraries to install |

## Setup

Python 3.9 to 3.11 is recommended.

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac / Linux

# 3. Install libraries
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Press **q** to quit.

## Test

```bash
python test_ear.py
```

## Tuning

Open `config.py`:
- Alarm rings too easily -> decrease `EAR_THRESHOLD` (for example 0.19)
- Alarm is not ringing -> increase `EAR_THRESHOLD` (for example 0.23)
- Want a faster or slower alarm -> change `CLOSED_FRAMES_LIMIT`

## Limitations

- Needs good lighting and a clear view of the face.
- Thick glasses or sunlight reflection can reduce accuracy.
- EAR values differ a little from person to person.

## Future improvements

- Add yawning detection (Mouth Aspect Ratio)
- Add head-nod detection
- Save alert history to a file

## Team

- Member 1: G Mohana Sindhuja(23STUCHH010563)
- Member 2: K Sriteja(23STUCHH010723)
