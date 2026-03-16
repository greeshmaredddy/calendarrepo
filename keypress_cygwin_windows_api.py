#!/usr/bin/env python3
"""
Cygwin/Windows API solution using ctypes
Works on Cygwin by calling native Windows API
"""

import time
import ctypes
import sys

# Windows key codes
VK_SPACE = 0x20
VK_BACK = 0x08

def press_key_windows(key_code):
    """Press and release a key using Windows API"""
    try:
        # Load user32.dll for Windows API
        user32 = ctypes.windll.user32
        
        # Simulate key press
        user32.keybd_event(key_code, 0, 0, 0)  # Press
        time.sleep(0.05)
        user32.keybd_event(key_code, 0, 2, 0)  # Release
    except AttributeError:
        print("Error: Windows API not available on this platform")
        sys.exit(1)

def main():
    interval = 3 * 60  # 3 minutes
    
    print("Starting key press automation (Windows API - Cygwin compatible)...")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(interval)
            
            print(f"[{time.strftime('%H:%M:%S')}] Pressing SPACE...")
            press_key_windows(VK_SPACE)
            
            time.sleep(0.5)
            
            print(f"[{time.strftime('%H:%M:%S')}] Pressing BACKSPACE...")
            press_key_windows(VK_BACK)
            
    except KeyboardInterrupt:
        print("\n\nScript stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
        print("This script requires Windows API access (Cygwin)")

if __name__ == "__main__":
    main()
