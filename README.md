# Gravity Sandbox

An Interactive 2D Gravity Simulation Using Python and Pygame

![Gravity Simulation](https://img.shields.io/badge/Physics-Simulation-blue) ![Python](https://img.shields.io/badge/Python-3.6%2B-green) ![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-orange)

## Project Overview

Gravity Sandbox is an interactive physics simulation that visualizes how celestial bodies interact under gravity. Users can create planets, assign mass, size, and initial velocity, and observe real-time motion governed by Newton's Law of Universal Gravitation. Planets leave trails to visualize their paths, and their colors change dynamically based on mass and speed, providing a clear and engaging representation of orbital mechanics.

## Features

- **Planet Creation**: Click and drag to place planets and set their initial velocity
- **Adjustable Parameters**: Sliders for planet size, mass, and gravitational constant (G)
- **Dynamic Visualization**: Planets leave trails and change color based on speed and mass
- **Real-Time Simulation**: Motion updates frame-by-frame using gravitational calculations
- **Reset Functionality**: Press R to clear all planets and restart the simulation

## How It Works

- Each planet calculates gravitational acceleration due to every other planet
- Velocity and position are updated continuously using a time-step approach
- Forces follow Newton's Law of Universal Gravitation:
  
  ```
  F = G * (m1 * m2) / r²
  ```
  
- Interactive sliders allow real-time adjustment of simulation parameters

## Technologies Used

- **Language**: Python
- **Library**: Pygame (for graphics, input handling, and UI)
- **Tools**: Any Python IDE or code editor

## Educational & Creative Impact

- Provides a hands-on platform to explore gravity and orbital mechanics
- Helps visualize abstract physics concepts intuitively
- Encourages experimentation with different planetary masses, velocities, and gravitational constants
- Combines programming, physics, and interactive design for learning and engagement

## How to Run

1. Ensure Python is installed on your system
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the script:
   ```bash
   python gravity_sandbox.py
   ```
4. Click and drag on the screen to create planets and observe their motion

## Controls

- **Click and Drag**: Create planets with initial velocity
- **R Key**: Reset the simulation (clear all planets)
- **Sliders**: Adjust planet size, mass, and gravitational constant

## Future Improvements

- Add collision detection and merging between planets
- Implement preset planetary systems (like the solar system)
- Add energy graphs showing kinetic and potential energy
- Allow saving/loading simulations

---

*Experience the beauty of orbital mechanics in this interactive gravity playground!*
