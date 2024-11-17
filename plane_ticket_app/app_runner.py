import subprocess

def run_plane_service():
    subprocess.Popen(["python", "plane_app/app.py"])

if __name__ == '__main__':
    run_plane_service()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating the process. Alvida!")