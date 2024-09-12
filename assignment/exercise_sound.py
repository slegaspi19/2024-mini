#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime
import time

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

R = 0
C = 523
D = 587
E = 659
G = 784

jingle_bells = [E, E, E, R, E, E, E, R, E, G, C, D, E]

for note in jingle_bells:
    if note == 0:
        time.sleep(duration * 3)
        continue
    print(note)
    playtone(note, duration)
    quiet()
    time.sleep(duration * 2)
    

# Turn off the PWM
quiet()
