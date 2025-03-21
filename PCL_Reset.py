import socket
import time
from datetime import datetime

def send_hp_print_request(printer_ip, printer_port=9100):
    try:
        # Create a TCP socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the printer's IP and port
        sock.connect((printer_ip, printer_port))
        print(f"Connected to printer at {printer_ip}:{printer_port}")

        # Send a simple PCL reset command to the printer (PCL Reset)
        # PCL Reset Command (Esc @) (or use an HP Printer Status Query if needed)
        pcl_reset_command = b'\x1B\x40'  # ESC @ is the PCL reset command (common in HP printers)
        sock.sendall(pcl_reset_command)
        print("Sent PCL reset command to the printer.")

        # Wait for a response from the printer
        sock.settimeout(5)  # Set timeout for response (5 seconds)
        response = sock.recv(1024)  # Buffer size of 1024 bytes

        if response:
            print("Response from printer:", response)
        else:
            print("No response received.")

        # Close the socket connection
        sock.close()

    except socket.timeout:
        print("Printer did not respond within the timeout period.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    counter = 0
    while True:
        printer_ip = '10.22.82.39'  # Replace with your printer's IP address
        send_hp_print_request(printer_ip)
        counter += 1
        hour, minute = datetime.now().hour, datetime.now().minute
        print(f"Iteration ({counter}) ended at {hour}:{minute} on {datetime.today().strftime('%m-%d-%Y')}.\n-----------------------------------------------------------------")
        time.sleep(1800)
