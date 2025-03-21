# Keep-HP-Printing
Helps stop an issue where some models of HP printer stop printing after a number of hours.

# Goal:
This program sends a PCL reset packet to port 9100 on the HP printer (the port responsible for handling print jobs), in an effort to keep the printer live so that it no longer stops printing after a fixed period of time. The impacted HP devices are those that do not allow the user to turn off the sleep mode using the built-in UI. You just need to modify the 'printer_ip' variable to have the internal IP that you desire in order to keep the printer alive. You can also modify this variable to be a list using the following code snippet:
'''
if __name__ == '__main__':
    counter = 0
    while True:
        printer_ip = [255.255.255.255, 255.255.255.254]  # Replace with your printer's IP address(es)
        for printer in printer_ip:
            send_hp_print_request(printer)
        counter += 1
        hour, minute = datetime.now().hour, datetime.now().minute
        print(f"Iteration ({counter}) ended at {hour}:{minute} on {datetime.today().strftime('%m-%d-%Y')}.\n-----------------------------------------------------------------")
        time.sleep(1800)
'''
Hopefully this helps someone else.
