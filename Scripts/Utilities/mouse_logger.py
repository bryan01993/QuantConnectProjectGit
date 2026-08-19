"""
mouse_logger.py
===============
Mouse movement tracker and reproducible playback utility for Windows.

Monitors and logs all mouse movements and click events to a repeatable CSV format.
Also supports replaying/reproducing previously recorded mouse trajectories with
exact timing deltas.

Usage:
    # Record mouse movements (logs initial [x,y] position and screen resolution):
    poetry run python Scripts/Utilities/mouse_logger.py --mode record --output my_mouse_log.csv

    # Replay recorded mouse movements:
    poetry run python Scripts/Utilities/mouse_logger.py --mode replay --input my_mouse_log.csv

    # Record for 10 seconds at 100Hz:
    poetry run python Scripts/Utilities/mouse_logger.py --duration 10 --interval 0.01
"""

from __future__ import annotations

import argparse
import csv
import ctypes
import ctypes.wintypes
from datetime import datetime
import os
from pathlib import Path
import sys
import time
from typing import Dict, List, Optional, Tuple

# Windows API Constants & Structures
VK_LBUTTON = 0x01
VK_RBUTTON = 0x02
VK_MBUTTON = 0x04

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def get_mouse_position() -> Tuple[int, int]:
    """Retrieve current mouse cursor (x, y) screen coordinates."""
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return int(pt.x), int(pt.y)


def get_screen_resolution() -> Tuple[int, int]:
    """Retrieve primary monitor resolution (width, height)."""
    width = ctypes.windll.user32.GetSystemMetrics(0)
    height = ctypes.windll.user32.GetSystemMetrics(1)
    return int(width), int(height)


def get_button_states() -> Dict[str, bool]:
    """Check current state of Left, Right, and Middle mouse buttons."""
    # GetAsyncKeyState returns negative value if highest bit is set (button pressed)
    return {
        "LEFT": bool(ctypes.windll.user32.GetAsyncKeyState(VK_LBUTTON) & 0x8000),
        "RIGHT": bool(ctypes.windll.user32.GetAsyncKeyState(VK_RBUTTON) & 0x8000),
        "MIDDLE": bool(ctypes.windll.user32.GetAsyncKeyState(VK_MBUTTON) & 0x8000),
    }


def set_mouse_position(x: int, y: int) -> None:
    """Set mouse cursor position on screen."""
    ctypes.windll.user32.SetCursorPos(int(x), int(y))


def send_mouse_click(button: str, pressed: bool) -> None:
    """Simulate mouse click event for replay."""
    flag = 0
    if button == "LEFT":
        flag = MOUSEEVENTF_LEFTDOWN if pressed else MOUSEEVENTF_LEFTUP
    elif button == "RIGHT":
        flag = MOUSEEVENTF_RIGHTDOWN if pressed else MOUSEEVENTF_RIGHTUP
    elif button == "MIDDLE":
        flag = MOUSEEVENTF_MIDDLEDOWN if pressed else MOUSEEVENTF_MIDDLEUP

    if flag != 0:
        ctypes.windll.user32.mouse_event(flag, 0, 0, 0, 0)


def record_mouse_movements(
    output_filepath: Path,
    interval_sec: float = 0.01,
    duration_sec: float = 0.0,
) -> None:
    """Record mouse position and button state transitions to a CSV file.

    Parameters
    ----------
    output_filepath : Path
        Path where the recorded CSV log file will be saved.
    interval_sec : float, default 0.01
        Sampling rate interval in seconds (0.01s = 100Hz).
    duration_sec : float, default 0.0
        Max recording duration in seconds. 0.0 records until Ctrl+C.
    """
    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    screen_w, screen_h = get_screen_resolution()
    initial_x, initial_y = get_mouse_position()
    start_time = time.time()
    start_iso = datetime.fromtimestamp(start_time).isoformat()

    print("=" * 60)
    print(" [MOUSE LOGGER] RECORDING STARTED")
    print(f"  - Screen Resolution : {screen_w} x {screen_h}")
    print(f"  - Initial Position  : [{initial_x}, {initial_y}]")
    print(f"  - Start Time        : {start_iso}")
    print(f"  - Sampling Interval : {interval_sec} s ({1.0/interval_sec:.0f} Hz)")
    print(f"  - Output File       : {output_filepath}")
    print("  - Stop Condition    : Press Ctrl+C" + (f" or wait {duration_sec}s" if duration_sec > 0 else ""))
    print("=" * 60)

    fieldnames = ["timestamp", "elapsed_sec", "event_type", "x", "y", "button", "pressed"]

    prev_x, prev_y = initial_x, initial_y
    prev_buttons = get_button_states()
    point_count = 0

    with open(output_filepath, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Log initial point immediately on start
        writer.writerow({
            "timestamp": start_iso,
            "elapsed_sec": 0.0,
            "event_type": "INITIAL_POS",
            "x": initial_x,
            "y": initial_y,
            "button": "NONE",
            "pressed": False,
        })
        point_count += 1

        try:
            while True:
                current_time = time.time()
                elapsed = current_time - start_time

                if duration_sec > 0 and elapsed >= duration_sec:
                    print(f"\n[INFO] Reached duration limit ({duration_sec}s). Stopping recording.")
                    break

                curr_x, curr_y = get_mouse_position()
                curr_buttons = get_button_states()
                now_iso = datetime.fromtimestamp(current_time).isoformat()

                # Detect movement
                if curr_x != prev_x or curr_y != prev_y:
                    writer.writerow({
                        "timestamp": now_iso,
                        "elapsed_sec": round(elapsed, 4),
                        "event_type": "MOVE",
                        "x": curr_x,
                        "y": curr_y,
                        "button": "NONE",
                        "pressed": False,
                    })
                    point_count += 1
                    prev_x, prev_y = curr_x, curr_y

                # Detect button state changes
                for btn_name in ["LEFT", "RIGHT", "MIDDLE"]:
                    if curr_buttons[btn_name] != prev_buttons[btn_name]:
                        is_pressed = curr_buttons[btn_name]
                        event_type = "CLICK_DOWN" if is_pressed else "CLICK_UP"
                        writer.writerow({
                            "timestamp": now_iso,
                            "elapsed_sec": round(elapsed, 4),
                            "event_type": event_type,
                            "x": curr_x,
                            "y": curr_y,
                            "button": btn_name,
                            "pressed": is_pressed,
                        })
                        point_count += 1

                prev_buttons = curr_buttons
                time.sleep(interval_sec)

        except KeyboardInterrupt:
            print("\n[INFO] KeyboardInterrupt received. Stopping recording cleanly.")

        # Log completion event
        end_time = time.time()
        end_elapsed = round(end_time - start_time, 4)
        end_iso = datetime.fromtimestamp(end_time).isoformat()
        writer.writerow({
            "timestamp": end_iso,
            "elapsed_sec": end_elapsed,
            "event_type": "STOP",
            "x": prev_x,
            "y": prev_y,
            "button": "NONE",
            "pressed": False,
        })
        point_count += 1

    print("-" * 60)
    print(f" [OK] Recorded {point_count} mouse events over {end_elapsed}s.")
    print(f" [OK] Output saved to: {output_filepath.resolve()}")
    print("-" * 60)


def replay_mouse_movements(input_filepath: Path) -> None:
    """Replay recorded mouse movements and clicks from a CSV file.

    Parameters
    ----------
    input_filepath : Path
        Path to the recorded CSV file.
    """
    if not input_filepath.exists():
        raise FileNotFoundError(f"Input CSV file does not exist: {input_filepath}")

    print("=" * 60)
    print(" [MOUSE LOGGER] REPLAY STARTED")
    print(f"  - Input File : {input_filepath}")
    print("=" * 60)

    rows: List[Dict[str, str]] = []
    with open(input_filepath, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)

    if not rows:
        print("[WARNING] CSV file is empty. Nothing to replay.")
        return

    print(f"[INFO] Loaded {len(rows)} recorded log entries.")
    print("[INFO] Replay beginning in 3 seconds... (Move mouse to take control if needed)")
    time.sleep(3.0)

    replay_start_time = time.time()

    for idx, row in enumerate(rows):
        target_elapsed = float(row["elapsed_sec"])
        event_type = row["event_type"]
        x = int(row["x"])
        y = int(row["y"])
        button = row["button"]
        pressed = row["pressed"].lower() == "true"

        # Precise timing sleep until event's elapsed delta
        current_elapsed = time.time() - replay_start_time
        sleep_duration = target_elapsed - current_elapsed
        if sleep_duration > 0:
            time.sleep(sleep_duration)

        if event_type in ("INITIAL_POS", "MOVE", "STOP"):
            set_mouse_position(x, y)
        elif event_type in ("CLICK_DOWN", "CLICK_UP"):
            set_mouse_position(x, y)
            send_mouse_click(button, pressed)

    total_replay_time = round(time.time() - replay_start_time, 4)
    print("-" * 60)
    print(f" [OK] Replay complete! Executed {len(rows)} events in {total_replay_time}s.")
    print("-" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Mouse Movement Recorder and Reproducible Playback Utility"
    )
    parser.add_argument(
        "--mode",
        choices=["record", "replay"],
        default="record",
        help="Operation mode: 'record' mouse events or 'replay' a recorded log CSV (default: record).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="",
        help="Path for output CSV file in record mode (default: Scripts/Utilities/mouse_log_<timestamp>.csv).",
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default="",
        help="Path to input CSV file for replay mode.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.01,
        help="Sampling rate interval in seconds for record mode (default: 0.01 = 100Hz).",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=0.0,
        help="Maximum duration in seconds to record (default: 0.0 = until Ctrl+C).",
    )

    args = parser.parse_args()

    if args.mode == "record":
        if args.output:
            output_path = Path(args.output)
        else:
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = Path("Scripts/Utilities") / f"mouse_log_{timestamp_str}.csv"

        record_mouse_movements(
            output_filepath=output_path,
            interval_sec=args.interval,
            duration_sec=args.duration,
        )

    elif args.mode == "replay":
        if not args.input:
            print("[ERROR] Replay mode requires specifying --input <path/to/mouse_log.csv>")
            sys.exit(1)
        replay_mouse_movements(input_filepath=Path(args.input))


if __name__ == "__main__":
    main()
