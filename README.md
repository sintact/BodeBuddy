# BodeBuddy

BodeBuddy calculates the magnitude and phase response of a linear, time-invariant (LTI) system
based on its transfer function and then plots the results as a Bode plot.

The transfer function is a mathematical representation of the system's behavior and describes the relationship between its input and output.

Bode plots are widely used in control systems engineering, signal processing, and electronics to analyze and design LTI systems. They provide valuable insights into the system's stability, gain, and phase margin, which are essential for designing robust and efficient control systems.

Potential applications for this include:

- Analyzing the frequency response of filters, amplifiers, or controllers in electronics and communication systems.
- Evaluating the stability of feedback control systems and determining the required compensator design to achieve desired performance.
- Studying the resonance and damping characteristics of mechanical or electrical systems.
- Designing equalizers to compensate for the frequency-dependent attenuation of communication channels.

---

There are 2 different transfer functions.

1. H(s) = s + z1 / s + p1
2. H(s) = (s + z1)(s + z2) / (s + p1)(s + p2)

Inputs:

- A transfer function number (1, 2).
- Radian frequencies of the Transfer function poles p1, p2, ... , and zeros z1, z2, ... .
- Frequency range of s (start & stop)

Outputs:

- A table depicting:
  - The frequency in left column (output as a log sweep).
  - |H(jω)| in the middle column.
  - Phase of H(jω) in the right column.
- A Bode plot of the table output, with the magnitude plot on top and the phase plot on bottom.
