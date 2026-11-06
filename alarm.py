"""
Plays a beep sound when the driver is drowsy.
The beep file is created automatically using Python's built-in
modules, so we do not need to download any sound file.
"""

import math
import os
import struct
import wave

import pygame

BEEP_FILE = "alarm.wav"


def create_beep_file(filename=BEEP_FILE, frequency=1000, seconds=1.0):
    """Creates a simple beep sound and saves it as a .wav file."""
    sample_rate = 44100
    total_samples = int(sample_rate * seconds)

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)       # mono
        wav_file.setsampwidth(2)       # 16-bit
        wav_file.setframerate(sample_rate)
        for i in range(total_samples):
            value = int(20000 * math.sin(2 * math.pi * frequency * i / sample_rate))
            wav_file.writeframes(struct.pack("<h", value))


class Alarm:
    def __init__(self):
        if not os.path.exists(BEEP_FILE):
            create_beep_file()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(BEEP_FILE)
        self.is_playing = False

    def start(self):
        """Start the alarm (keeps repeating until stop() is called)."""
        if not self.is_playing:
            self.sound.play(loops=-1)
            self.is_playing = True

    def stop(self):
        """Stop the alarm."""
        if self.is_playing:
            self.sound.stop()
            self.is_playing = False
