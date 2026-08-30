# Task 05: Grand Line Guardian

A real-time terminal process monitor designed for the Straw Hat Pirates to keep track of active processes across the Grand Line (Linux System).

# Approach & Architecture

1. **Kernel Telemetry Interface (`/proc`)**:
   Queries system and process state from Linux's `/proc` virtual filesystem using `psutil`. Reads process IDs (PID), names, CPU usage, and RAM consumption.

2. **Terminal Rendering (`curses`)**:
   Uses Python's standard `curses` library to continuously draw and update the terminal display every 500 milliseconds without flicker.

# Setup & Execution

1. Navigate to the project directory:
   cd grand-line-guardian
 
