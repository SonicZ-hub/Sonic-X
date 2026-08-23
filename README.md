# Sonic X

MADE BY SONICZ
https://youtube.com/@sonicz-dev?si=gYlCjUugPIICIUn_

---

## INSTALL

### PC (Windows / Linux)

Step 1 - Download

git clone https://github.com/YOUR_USERNAME/Sonic-X.git
cd Sonic-X

Or download sonicx.py manually and place it in a folder.

Step 2 - Run

python3 sonicx.py

No extra packages needed. Uses only built-in Python modules.

---

### MOBILE (Android with Termux)

Step 1 - Install Termux
- Download Termux from F-Droid (recommended) or Google Play Store

Step 2 - Update & Install Python
Open Termux and run:

pkg update && pkg upgrade -y
pkg install python git -y

Step 3 - Download Sonic X

git clone https://github.com/YOUR_USERNAME/Sonic-X.git
cd Sonic-X

Step 4 - Run

python sonicx.py

Alternative: Download sonicx.py directly, then:

termux-setup-storage
cp /sdcard/Download/sonicx.py ~/
python sonicx.py

---

## COMMANDS

run   - Start the DDoS attack (enter target, port, method, threads)
stop  - Stop the current attack
menu  - Show commands list
about - Show credit & YouTube link
exit  - Quit program

---

## ATTACK METHODS

1 - TCP     - TCP connection flood
2 - UDP     - UDP packet flood
3 - SYN     - SYN flood (half-open connections)
4 - HTTP    - HTTP GET flood with random paths & user-agents
5 - MIXED   - Randomly switches between all methods

---

## EXAMPLE USAGE

$ python3 sonicx.py

  Target IP/URL: example.com
  Port: 80
  Method: 5
  Threads: 500

  [+] 93.184.216.34:80 | MIXED | 500 threads

  > stop
  [+] Stopped.
  > about

  MADE BY SONICZ
  https://youtube.com/@sonicz-dev?si=gYlCjUugPIICIUn_

  > exit
  Bye.

---

Sonic X - For authorized testing only.
