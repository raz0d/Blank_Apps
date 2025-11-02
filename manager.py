import subprocess
import time
import psutil

apps = [
    "dist/blank1.exe",
    "dist/blank2.exe",
    "dist/blank3.exe",
    "dist/blank4.exe",
    "dist/blank5.exe"
]

processes = []

# Start all apps
for app in apps:
    p = subprocess.Popen(app)
    processes.append(p)

# Wait 20s before closing the first one
time.sleep(20)

# Kill one by one
for p in processes:
    try:
        proc = psutil.Process(p.pid)
        proc.terminate()
    except Exception as e:
        print(f"Error closing: {e}")
    time.sleep(20)
