Import subprocess

# Run the service corresponding to the user_app
def ticket_booking_service():
    subprocess.Popen(["python", "Plane_ticket_app/app.py"])

if __name__ == '__main__':
    
    ticket_booking_service()

    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\\nTerminating both the processes. Alvida!")
