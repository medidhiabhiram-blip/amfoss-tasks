import curses
import psutil

def draw_header(stdscr, total_procs, cpu_total, mem_total):
    height, width = stdscr.getmaxyx()
    header_str = " --- GRAND LINE GUARDIAN: STRAW HAT NAVIGATION SYSTEM --- "
    stdscr.attron(curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(0, max(0, (width - len(header_str)) // 2), header_str[:width])
    stdscr.attroff(curses.A_BOLD | curses.color_pair(1))

    stats_str = f" Active Ships (Processes): {total_procs} | Total CPU: {cpu_total:5.1f}% | RAM: {mem_total:5.1f}% "
    stdscr.addstr(1, max(0, (width - len(stats_str)) // 2), stats_str[:width])
    
    controls = "Press [Q] or [Ctrl+C] to Exit"
    stdscr.addstr(2, max(0, (width - len(controls)) // 2), controls[:width], curses.A_DIM)

    # Column Headers
    cols = f"{'PID':<8} {'SHIP NAME (PROCESS)':<35} {'CPU %':<10} {'MEM %':<10}"
    stdscr.attron(curses.A_REVERSE)
    stdscr.addstr(4, 2, cols[:width - 4].ljust(width - 4))
    stdscr.attroff(curses.A_REVERSE)

def main(stdscr):
    # Setup curses
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)
    stdscr.nodelay(True)
    stdscr.timeout(500)  # Refresh interval: 500ms (< 1s requirement)

    # Initial call to seed CPU percentage calculation
    psutil.cpu_percent()

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        max_rows = height - 5  # Space for header

        # System statistics
        cpu_total = psutil.cpu_percent()
        mem_total = psutil.virtual_memory().percent

        # Collect process telemetry
        processes = []
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                p_info = p.info
                processes.append({
                    'pid': p_info['pid'],
                    'name': p_info['name'] or 'Unknown',
                    'cpu': p_info['cpu_percent'] or 0.0,
                    'mem': p_info['memory_percent'] or 0.0
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # Sort by CPU usage descending
        processes.sort(key=lambda x: x['cpu'], reverse=True)
        total_procs = len(processes)

        draw_header(stdscr, total_procs, cpu_total, mem_total)

        # Render process list up to terminal height
        for idx, proc in enumerate(processes[:max_rows]):
            row_str = f"{proc['pid']:<8} {proc['name'][:34]:<35} {proc['cpu']:<10.1f} {proc['mem']:<10.1f}"
            y_pos = 5 + idx
            if y_pos >= height - 1:
                break
            stdscr.addstr(y_pos, 2, row_str[:width - 4])

        stdscr.refresh()

        # Exit check
        key = stdscr.getch()
        if key in (ord('q'), ord('Q')):
            break

if __name__ == '__main__':
    curses.wrapper(main)
