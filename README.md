# vsftpd-3.0.3-DoS

## Overview

This is a Python script to exploit a remote Denial of Service (DoS) vulnerability in **vsftpd 3.0.3** by overwhelming the FTP server with connections. The script repeatedly makes connections to the server, potentially blocking legitimate users.

The script has been fixed to address syntax errors and improve functionality, making it ready for practical testing.

## Features

- Tests if the target server's port is open.
- Executes a DoS attack by making multiple simultaneous connections.
- Customizable connection limits and target ports.

### References
- [Exploit-DB](https://www.exploit-db.com/exploits/49719)
- [CVE-2021-30047 - NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-30047)

## Requirements

- **Python 3.x**
- Network access to the target

## Usage

Run the script using Python 3, specifying the target IP, port, and optional maximum number of connections.

### Basic Usage
```bash
python3 vsftpd303-dos.py <TARGET> <PORT(DEFAULT:21)> <MAX_CONNS(DEFAULT:50)>
```
### Example Usage
```bash
python3 vsftpd303-dos.py x.x.x.x 21 44
```
```
._________________.
|     VS-FTPD     |
|      D o S      |
|_________________|
|                 |
|By XYN/DUMP/NSKB3|
|_________________|
|                 |
|_modifed version_|
|---kuppamjohari--|
|_________________|
|_|_|_|_____|_|_|_|
|_|_|_|_|_|_|_|_|_|

Exploit Author: xynmaps
Modified By: kuppamjohari
Press Ctrl+C to cancel the program at any time.

[!] Testing if x.x.x.x:21 is open
[+] Port 21 open, starting attack...
[+] Attack started on x.x.x.x:21!

```
