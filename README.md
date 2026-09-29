# Hey, I'm Youssef 👋

**Cybersecurity student @ INPT** · I just build stuff, break stuff, and see where it goes

---

## What I'm Working On

| | Project | Status |
|---|---|---|
| ⛓️ | **CIM — Cyber Intel Marketplace** — Autonomous AI agents pay per query via x402 on Hedera for cybersecurity threat intelligence. Real on-chain HBAR payments settled end-to-end. Built for ETHOnline 2026. | Shipped |
| 🔴 | **IBC CTF Platform** — 100 blockchain security challenges for a live CTF (150 participants). Custom Astro + React headless frontend on CTFd. | Active |
| 🔑 | **Clavis** — Secure collaborative file management platform with MFA (OTP), AES-256 file encryption, versioning, ACL, real-time notifications via WebSocket, and a full audit log. | Shipped |
| 🛠️ | **30 Days of Cyber** — 30 security tools built from scratch in Python, one per day. 13 shipped so far. | In progress |
| 🛡️ | **SOC Home Lab** — Wazuh SIEM + Sysmon + custom Sigma detection rules mapped to MITRE ATT&CK | Active |
| 📚 | **HTB CJCA** — Networking, Linux, Windows, offensive & defensive security fundamentals | In progress |
| 🤖 | **ML for Security** — Ransomware detection using synthetic data augmentation (CTGAN / TVAE) | Completed |

---

## Skills & Tools

| Domain | Stack |
|---|---|
| **SIEM & Detection** | Wazuh, Sigma rules, Sysmon, log analysis |
| **Network Security** | Wireshark, tcpdump, Nmap, protocol analysis |
| **Web3 & Blockchain** | Hedera (HBAR), x402, HCS, Fastify, TypeScript |
| **Web & CTF** | CTFd, Astro, React, Flask, Docker, Nginx, Socket.IO, ctfcli |
| **Penetration Testing** | Burp Suite, ffuf, sqlmap, Metasploit/msfvenom, Hydra, John, Netcat, Nikto |
| **Exploitation** | Path traversal, unrestricted file upload RCE, SSRF, credential reuse, Git object crafting, CVE exploitation |
| **Enumeration** | nmap, enum4linux-ng, SMB/RPC, vhost fuzzing, subdomain discovery, API endpoint discovery |
| **Post-Exploitation** | Privilege escalation, container escape, credential harvesting, lateral movement, systemd service abuse |
| **Operating Systems** | Linux (Ubuntu/Kali), Windows, Active Directory |
| **Scripting** | Python, Bash, PowerShell, TypeScript |
| **ML for Security** | Scikit-learn, CTGAN, TVAE, Pandas |
| **Frameworks** | MITRE ATT&CK, NIST CSF, PASTA, World ID |

---

## Projects

### ⛓️ [CIM — Cyber Intel Marketplace](https://github.com/zayd-mzn/ethonline2026) · [Live Demo](https://ethonline-dun.vercel.app/) · [ETHOnline 2026 Certificate](certificates/ETHOnline2026/ethonline2026-youssef-laaryech-certificate.pdf)
Built for **ETHOnline 2026**. A marketplace where autonomous AI agents pay per query — via x402 on Hedera — for cybersecurity threat intelligence, with providers gated behind World human-verification.
- **Full agent loop** working end-to-end: discover → HTTP 402 → HBAR micro-payment → consume → threat report
- **Real on-chain payment** settled and verified on Hedera testnet via Blocky402 ([HashScan proof](https://hashscan.io/testnet/transaction/0.0.7162784@1788996589.198259785))
- **Stack:** TypeScript everywhere — Fastify backend, autonomous agent (`@hashgraph/sdk` + `@x402/hedera`), React 19 + Vite + Tailwind frontend
- **Hedera HCS** audit log: every paid request written as an immutable on-chain record
- **World ID Selfie Check** gates provider publishing (anti-Sybil); agent human-backing via AgentKit
- **Live SSE dashboard** streams every stage of the agent loop in real time

### 🔗 [IBC CTF — Human Blockchain Simulation](https://github.com/4bd0z4/inpt-ibc-ctf)
A full CTF competition platform built for INPT Blockchain Club's October 2026 event.
- **100 challenge files** across 17 blockchain security concepts
- **Custom headless frontend** in Astro 5 + React 19 replacing CTFd's default UI
- **Same-origin deployment** via Nginx method-split routing (no CORS, native cookie auth)
- Challenges cover: Proof of Work, Merkle trees, double-spend forensics, 51% attack game theory, smart contract vulnerabilities (reentrancy, integer overflow, missing access control), flash loan oracle manipulation, ECDSA nonce reuse, selfish mining, zero-knowledge proofs, MEV/sandwich attacks, Sybil resistance, blockchain forensics

### 🔑 [Clavis — Secure File Management Platform](https://github.com/yousseflarynv-gif/Clavis)
A full-stack collaborative file management web app built as an INPT course project. Security-first from the ground up.
- **MFA via email OTP** — every login requires a one-time code
- **AES-256 file encryption** — all uploaded files encrypted at rest with Fernet
- **Versioning & file locking** — full version history + TTL-based auto-release locks
- **Granular ACL** — per-file, per-user access control
- **Complete audit log** — every action recorded
- **Real-time notifications** via Socket.IO WebSocket
- **Anti brute-force** — 5 failed attempts → 15-minute lockout; bcrypt (14 rounds) for passwords
- **Stack:** Python 3.12 + Flask · React 19 · SQLite (WAL) · JWT + OTP auth · Socket.IO · SMTP (Brevo)

### 🧪 [30 Days of Cyber](https://github.com/Youssef-Laaryech/30-days-of-cyber)
30 cybersecurity tools built from scratch, one per day — no copy-pasting, no shortcuts.

Tools shipped: multi-cipher encoder · port scanner · DNS lookup CLI · hash cracker · metadata scraper · network traffic analyzer · Linux CIS hardening auditor · SSH brute force detector · systemd persistence scanner · secrets scanner · canary token generator · mini SIEM · HTTP security header scanner

**Stack:** Python · CLI · built to understand, not just to run

### 🔐 [Ransomware Data Augmentation](https://github.com/Youssef-Laaryech/ransomware-data-augmentation)
ML-based ransomware detection addressing the real-world problem of scarce labeled malware datasets. Uses CTGAN, TGAN, and TVAE to generate synthetic ransomware feature vectors for model training.

### 📝 [HTB Writeups & Cybervault](https://github.com/Youssef-Laaryech/writeups)
A structured personal knowledge base for offensive security — built in Obsidian, written like a field manual.

**Machines rooted (6):**

| Machine | OS | Difficulty | Key Techniques |
|---|---|---|---|
| **Nexus** | Linux | Easy | Vhost fuzzing · Git commit history leakage · CVE-2026-38526 (unrestricted file upload → RCE) · `os.path.join()` path traversal · Raw Git object crafting · SSH privesc |
| **Silentium** | Linux | Medium | Flowise account takeover (CVE-2025-58434) · Flowise `Function()` RCE (CVE-2025-59528) · Container env credential dump · Gogs symlink traversal + sshCommand injection (CVE-2025-8110) |
| **Abducted** | Windows | — | SMB/RPC enumeration · enum4linux-ng · Null session · User/share discovery |
| **Cohort** | Linux | — | SSRF · loopback filter bypass (`127.1`) · Internal port discovery · API enumeration |
| **Orion** | Linux | — | In progress |
| **2Million** | Linux | — | In progress |

**Attack phases covered in cheatsheets:** Recon · Web · PrivEsc · Reverse shells · Pivoting · Linux permissions · HTTP reference

**Tools with dedicated notes:** nmap · ffuf · Burp Suite · sqlmap · metasploit · msfvenom · meterpreter · netcat · hydra · john · nikto · wireshark · tcpdump · curl · git · shodan · aircrack-ng · cdk

**Technique concepts documented:** Path traversal · Unrestricted file upload RCE · Git commit history leakage · Raw Git object crafting · Credential reuse · Vhost fuzzing · SMB enumeration

---

## Certifications

- ✅ [ETHOnline 2026 — Certificate of Participation](certificates/ETHOnline2026/ethonline2026-youssef-laaryech-certificate.pdf) · Project: [CIM](https://ethglobal.com/showcase/cim-uvx7x)
- ✅ Google Cybersecurity Professional Certificate
- 🔄 HTB Certified Junior Cybersecurity Associate *(in progress)*

---

## How I Work

I learn by building, breaking, and documenting.
Every detection rule I write gets tested against real attack simulations.
Every concept I study gets explained in my own words and pushed to GitHub.

I document mistakes, not just successes — because troubleshooting IS the skill.

---

## Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-laaryech)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Youssef-Laaryech)

---

<sub>Last updated: September 2026</sub>
