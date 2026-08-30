Grand Line Guardian is a lightweight, real-time terminal-based process monitoring application inspired by tools like htop and btop++. Built with a Straw Hat Pirates navigation theme, it acts as a system monitor where every running process represents an active ship sailing across the Grand Line (Linux operating system).

# Tech Stack & Requirements

* Language: Python 3
* Terminal UI: curses (Python standard library)
* Kernel & System Telemetry: psutil
* Target Environment: Linux / Unix Terminal / macOS

# Approach & System Architecture

The application is structured into three main operational layers:

# 1. Kernel Interface & Process Querying (/proc)

The core requirement of this task is reading system and process information from the Linux Virtual Filesystem (/proc).

* In Linux, process information is exposed by the kernel as pseudo-files under /proc/[PID]/.
* Instead of spawning external binary calls (ps, top), psutil acts as an efficient wrapper reading these virtual files (/proc/stat, /proc/meminfo, /proc/[PID]/stat).
* The system fetches:

  * PID (Process Identifier)
  * Process Name
  * CPU Usage (%)
  * Memory Usage (%)
  * Total Active Process Count

# 2. Live Rendering Loop (curses)

To create a smooth, non-flickering terminal interface, Python's curses library is used:

* Double Buffering: Screen contents are drawn in memory and pushed using stdscr.refresh().
* Sub-Second Refresh Rate: The event loop utilizes stdscr.timeout(500), triggering a complete telemetry pull and screen update every 500 milliseconds (0.5s), satisfying the sub-second updates requirement.
* Non-Blocking Execution: curses.nodelay(True) ensures the application loop runs continuously without blocking for keyboard input.

# 3. Data Processing & Formatting

* Dynamic process sorting ranks active processes by CPU consumption in descending order.
* Output strings are formatted and clamped dynamically based on terminal dimensions (getmaxyx()) to prevent text wrapping issues across different screen sizes.

# Installation & Execution

# Prerequisites

* Python 3.8 or higher installed on a Unix-like environment (Linux, WSL, or macOS).

# Steps

1. Navigate to the task directory:

   ```bash
   cd TASK-05
   ```
