<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=2600&pause=900&color=39FF14&center=true&vCenter=true&width=640&lines=Aspiring+Cybersecurity+Engineer+%40+INPT;Red+Teaming+%2F+Pentesting+enthusiast;Blockchain+%26+Web3+security+enthusiast;6+HTB+boxes+rooted+%C2%B7+every+one+written+up" alt="typing banner" />
</p>

```console
youssef@inpt:~$ neofetch
                      .:--==+++++++++==-:.                      __   __                    __
                 :-=+*********+++++********+=-:                 \ \ / /__ _  _ ______ ___ / _|
            .:-+****+++++++++++++++++++++++++***+-:              \ V / _ \ || (_-<_-</ -_)  _|
          -==:=*****+++++++++++++++++++++++++++++=-==.            |_|\___/\_,_/__/__/\___|_|
        =+-  :***#*++++++++++++++++++++++++++++++:. :++.         _                              _
      -+- .:-**+******************++==--==-:-==+=:-.  :++       | |   __ _ __ _ _ _ _  _ ___ __| |_
     **--=+++========-----====---:..........:..:::::    -#.     | |__/ _` / _` | '_| || / -_) _| ' \
    #*=++======-===-=+*#%%@#:---:..::::::::::::.::...... :#.    |____\__,_\__,_|_|  \_, \___\__|_||_|
   #*====----==+=---#@@@@@@**#*#*:.::::::::::::..:::::... :%                        |__/
  -# ..  ..+@@@@#####%%%%%###**=-.:::::::::::::::......... ++
  #-    .::+%@@##############*+-::...::::::::..:.......... :%   youssef@inpt
  #:    ..:.=##*==+*###########%*-.:::.......::.............%   ------------
  #:    ... -%*##*###########*+-:.......    ..... ........ :%   Role       Aspiring Cybersecurity Engineer @ INPT
  =*   ..  ..+##*********####*+=--:             .      ... ++   Focus      Red Teaming / Pentesting
   %:         -*##*#############*=:...                  . :%    Passion    Blockchain & Web3 security
   :#:.::::::..:=*#############*+----:    .              :#.    OS         Kali Linux · Windows AD labs
    .#*--======--===+**##***++==-==--:..:-::.::..   ..  =#.     Uptime     on GitHub since 2025-07
      +*=-------------===-------==--=--==--=-=--=:. ..-*+       Pwned      6 HTB boxes, all written up
       :+*=----------------------=====-------------:-++.        Packages   8 projects · 13 tools from scratch
         :+*+=-----:---------:::.:::-----===-----=+*=.          Langs      Python, TypeScript, Bash
            :=++=-- :-----------::.......::::-=++=:             Arsenal    nmap, burp, bloodhound, impacket, hedera-sdk
               :-===-==----:.:---:-:::::::--==-.
                   .::-=====-======+===--::.                    ███ ███ ███ ███ ███ ███ ███ ███
                            ......

youssef@inpt:~$ cat /etc/motd
Building labs, not just collecting certs.
I build stuff, break stuff, write down what broke, and see where it goes.
```

---

```console
youssef@inpt:~$ nmap -sV -p- youssef-laaryech
Starting Nmap 7.95 ( https://nmap.org )
Nmap scan report for youssef-laaryech (github.com)
Host is up, caffeine-bound.

PORT       STATE  SERVICE        VERSION
22/tcp     open   ssh            curiosity 2.0 (never closes)
1337/tcp   open   red-team       htb: 6 boxes rooted, 2 on the bench, every kill chain written up
3268/tcp   open   ldap-gc        active directory: bloodhound -> genericall -> rbcd -> SYSTEM
8545/tcp   open   web3-rpc       hedera + x402, autonomous agents paying for threat intel
31337/tcp  open   ctf            100 blockchain challenges authored, 150 players
5601/tcp   open   blue-lab       wazuh + sysmon + sigma: knowing what the defender sees

Service Info: Host: inpt; OSs: Linux (Kali/Ubuntu), Windows (AD); Role: aspiring cybersecurity engineer
Nmap done: 1 IP address (1 host up) scanned. 0 boring ports found.
```

---

```console
youssef@inpt:~$ ps aux --sort=-%cpu | grep youssef
USER     PID  %CPU STAT COMMAND
youssef  101  35.0 R    htb pwn abducted     # samba null session, the door is somewhere
youssef  102  25.0 R    htb pwn paperwork    # cmd injection via job name
youssef  203  15.0 S    htb-academy --path cjca
youssef  304  10.0 S    web3-sec --study reentrancy,oracles,mev
youssef  405   8.0 S    home-lab --siem wazuh --telemetry sysmon   # attack it, then watch the logs
youssef  506   7.0 T    30-days-of-cyber --day 16   # 13/30 shipped. paused, not dead
```

---

```console
youssef@inpt:~$ ls -la ~/projects/
total 8
drwxr-xr-x  cim-cyber-intel-marketplace/  shipped   AI agents pay per query in HBAR (x402) for threat intel · ETHOnline 2026
drwxr-xr-x  ibc-ctf-platform/             shipped   100 challenges · 17 blockchain attack classes · 150 players · Astro on CTFd
drwxr-xr-x  clavis/                       shipped   secure file sharing · email OTP MFA · encryption at rest · ACL · audit log
drwxr-xr-x  deleg-it/                     shipped   toolkit for INPT class reps: file collection, treasury, voting · React + Express
drwxrwxr-x  home-lab/                     active    attack/defense lab · Wazuh · Sysmon · Sigma · ATT&CK
drwxrwxr-x  writeups/                     active    6 HTB writeups · 26 tool notes · 20 technique notes · 7 cheatsheets
drwxrwxr-x  30-days-of-cyber/             paused    13/30 security tools built from scratch, from port scanner to mini SIEM
drwxr-xr-x  ml-ransomware-detection/      done      CTGAN · TVAE · synthetic data for scarce malware datasets

youssef@inpt:~$ cat ~/projects/cim-cyber-intel-marketplace/NOTES
agent discovers feed -> gets HTTP 402 -> pays HBAR on Hedera -> consumes intel -> writes threat report
every paid request is logged to Hedera HCS · providers gated by World ID (anti-Sybil)
real payment settled on testnet, receipt on HashScan. not a mockup.
```

> `xdg-open` →
> [CIM](https://github.com/zayd-mzn/ethonline2026) ([live demo](https://ethonline-dun.vercel.app/) · [showcase](https://ethglobal.com/showcase/cim-uvx7x) · [on-chain proof](https://hashscan.io/testnet/transaction/0.0.7162784@1788996589.198259785)) ·
> [Deleg-IT](https://github.com/Youssef-Laaryech/Deleg-IT) ·
> [Writeups](https://github.com/Youssef-Laaryech/writeups) ·
> [30 Days of Cyber](https://github.com/Youssef-Laaryech/30-days-of-cyber) ·
> [Ransomware ML](https://github.com/Youssef-Laaryech/ransomware-data-augmentation)

---

```console
youssef@inpt:~$ cat ~/writeups/htb/scoreboard.txt
BOX         OS               DIFF     STATUS   KILL CHAIN
orion       linux            hard     rooted   second-order SQLi -> TOTP/2FA bypass -> ssh-agent socket hijack -> sudo
silentium   linux            medium   rooted   Flowise ATO + RCE -> container env creds -> Gogs symlink traversal (CVE-2025-8110)
cohort      linux            medium   rooted   SSRF (127.1 bypass) -> Marimo WebSocket RCE -> PackageKit TOCTOU -> root
support     windows (DC)     easy     rooted   .NET RE -> LDAP creds -> BloodHound GenericAll -> RBCD -> S4U -> SYSTEM
nexus       linux            easy     rooted   vhost fuzz -> git history leak -> upload RCE -> raw git object crafting
twomillion  linux            easy     rooted   JS deobfuscation -> API BOLA -> cmd injection -> OverlayFS (CVE-2023-0386)
abducted    linux (samba)    medium   wip      smb null session -> rpc enum -> ...
paperwork   linux            medium   wip      cmd injection via unsanitized job name -> ...
```

> `xdg-open` → [writeups & Cybervault](https://github.com/Youssef-Laaryech/writeups), an Obsidian vault written like a field manual

---

```console
youssef@inpt:~$ sudo -l
User youssef may run the following commands on inpt:

    (RECON)      nmap, ffuf, enum4linux-ng, smbmap, ldapsearch, shodan
    (WEB)        burpsuite, sqlmap, nikto, curl
    (EXPLOIT)    path-traversal, file-upload-rce, ssrf, sqli, cmd-injection, cve-exploitation
    (AD)         bloodhound, impacket, evil-winrm, genericall-abuse, rbcd, kerberos-s4u
    (POST-EXPL)  privesc, container-escape (cdk), credential-reuse, pivoting, metasploit
    (CRACK)      hydra, john
    (RE)         ilspycmd (.NET)
    (VULN-MGMT)  nessus, openvas
    (BLUE-LAB)   wazuh, sysmon, sigma, wireshark, tcpdump
    (BUILD)      python, bash, powershell, typescript, react, flask, fastify, express, docker, nginx
    (WEB3)       hedera sdk, x402, hcs, smart-contract vulns, ctfd
    (ML)         scikit-learn, pandas, ctgan, tvae
    (FRAMEWORK)  mitre-att&ck, nist-csf, pasta
```

---

```console
youssef@inpt:~$ history | cut -c8-
2025-07  git init                                    # hello, github
2026-04  python train.py --augment ctgan,tvae        # ML meets malware
2026-06  npm run dev --prefix deleg-it               # fixing my own school's paperwork
2026-08  ./30-days-of-cyber --day 15                 # 13 tools, zero copy-paste
2026-09  ethonline submit cim                        # agents paying agents for threat intel
2026-09  htb pwn nexus silentium cohort               # 3 boxes, 3 writeups
2026-09  htb pwn support twomillion orion            # AD rabbit hole + first hard box
2026-10  vim cybervault/pentest-process/*.md         # 8 phases, from scoping to the final report
2026-10  ctfd deploy ibc-ctf --players 150           # 100 challenges, 0 sleep
```

---

```console
youssef@inpt:~$ ls -l ~/certs/
-rw-r--r--  google-cybersecurity-professional.pdf
-rw-r--r--  ethonline-2026-participation.pdf
-rw-------  htb-cjca.pdf.part                       # download in progress

youssef@inpt:~$ cat ~/.config/how-i-work.conf
learn      = build, break, document
offense    = every attack I run, I also try to detect
concepts   = explained in my own words, pushed to GitHub
mistakes   = documented, not hidden   # troubleshooting IS the skill
```

> `xdg-open` → [ETHOnline 2026 certificate](certificates/ETHOnline2026/ethonline2026-youssef-laaryech-certificate.pdf)

---

```console
youssef@inpt:~$ whois youssef-laaryech
linkedin:  linkedin.com/in/youssef-laaryech
github:    github.com/Youssef-Laaryech
```

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-laaryech)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Youssef-Laaryech)
[![HTB Writeups](https://img.shields.io/badge/HTB_Writeups-9FEF00?style=flat&logo=hackthebox&logoColor=black)](https://github.com/Youssef-Laaryech/writeups)

<details>
<summary><code>youssef@inpt:~$ ls -a</code> &nbsp;(there's a hidden file)</summary>

```console
youssef@inpt:~$ ls -a
.  ..  .bashrc  .flag  projects  writeups  certs

youssef@inpt:~$ cat .flag
SU5QVHt5MHVfcjM0ZF90aDNfd2gwbDNfcjM0ZG0zX24wd19sM3RzX3Q0bGt9

# decode it. you know how.
```

</details>

```console
youssef@inpt:~$ exit
logout
Connection to inpt closed.
```
