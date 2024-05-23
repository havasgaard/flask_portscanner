import socket
import platform

# Common ports with descriptions, potential vulnerabilities, and detailed fixes
PORTS_INFO = {
    21: {
        "name": "FTP",
        "description": "File Transfer Protocol",
        "vulnerabilities": [
            "Anonymous authentication can allow unauthorized access.",
            "Data sent in clear text."
        ],
        "fixes": {
            "windows": [
                "Disable FTP service if not needed:\n- Open 'Services' and stop the 'FTP Publishing Service'.\n- Set the startup type to 'Disabled'.",
                "Use FTPS instead of FTP to encrypt data:\n- Install an FTPS server (e.g., FileZilla Server) and configure it to use SSL/TLS."
            ],
            "mac": [
                "Disable FTP service if not needed:\n- Open 'System Preferences' > 'Sharing' and uncheck 'FTP Access'.",
                "Use FTPS instead of FTP to encrypt data:\n- Configure your FTP server (e.g., Pure-FTPd) to use SSL/TLS."
            ],
            "linux": [
                "Disable FTP service if not needed:\n- Stop the FTP service: `sudo systemctl stop vsftpd`\n- Disable it: `sudo systemctl disable vsftpd`.",
                "Use FTPS instead of FTP to encrypt data:\n- Install and configure vsftpd for FTPS: edit `/etc/vsftpd.conf` to enable SSL."
            ]
        }
    },
    22: {
        "name": "SSH",
        "description": "Secure Shell",
        "vulnerabilities": [
            "Brute force attacks on passwords.",
            "Vulnerable to man-in-the-middle attacks if host keys are not verified."
        ],
        "fixes": {
            "windows": [
                "Use strong passwords and enable key-based authentication:\n- Install OpenSSH and configure `sshd_config` to use public key authentication.",
                "Regularly update SSH software to the latest version:\n- Use Windows Update or manually update OpenSSH."
            ],
            "mac": [
                "Use strong passwords and enable key-based authentication:\n- Configure SSH keys in `~/.ssh/authorized_keys`.",
                "Regularly update SSH software to the latest version:\n- Ensure your macOS is up-to-date."
            ],
            "linux": [
                "Use strong passwords and enable key-based authentication:\n- Configure SSH keys in `/home/user/.ssh/authorized_keys`.",
                "Regularly update SSH software to the latest version:\n- Update OpenSSH: `sudo apt-get update && sudo apt-get upgrade openssh-server`."
            ]
        }
    },
    23: {
        "name": "Telnet",
        "description": "Telnet protocol",
        "vulnerabilities": [
            "Data sent in clear text.",
            "Weak authentication mechanisms."
        ],
        "fixes": {
            "windows": [
                "Disable Telnet service:\n- Open 'Services' and stop the 'Telnet' service.\n- Set the startup type to 'Disabled'.",
                "Use SSH instead of Telnet for secure communication:\n- Install OpenSSH and configure it as an alternative."
            ],
            "mac": [
                "Disable Telnet service:\n- Use `sudo launchctl unload -w /System/Library/LaunchDaemons/telnet.plist`.",
                "Use SSH instead of Telnet for secure communication:\n- Use built-in SSH: `ssh user@hostname`."
            ],
            "linux": [
                "Disable Telnet service:\n- Stop the Telnet service: `sudo systemctl stop telnet.socket`\n- Disable it: `sudo systemctl disable telnet.socket`.",
                "Use SSH instead of Telnet for secure communication:\n- Use built-in SSH: `ssh user@hostname`."
            ]
        }
    },
    25: {
        "name": "SMTP",
        "description": "Simple Mail Transfer Protocol",
        "vulnerabilities": [
            "Open relay issues can be exploited for spam.",
            "Data sent in clear text."
        ],
        "fixes": {
            "windows": [
                "Configure the SMTP server to require authentication:\n- Use IIS Manager to configure SMTP authentication settings.",
                "Use SMTPS (SMTP over SSL) to encrypt data:\n- Configure your mail server (e.g., hMailServer) to use SSL/TLS."
            ],
            "mac": [
                "Configure the SMTP server to require authentication:\n- Edit the Postfix configuration in `/etc/postfix/main.cf`.",
                "Use SMTPS (SMTP over SSL) to encrypt data:\n- Configure Postfix or another mail server to use SSL/TTLS."
            ],
            "linux": [
                "Configure the SMTP server to require authentication:\n- Edit `/etc/postfix/main.cf` and set `smtpd_recipient_restrictions` to require authentication.",
                "Use SMTPS (SMTP over SSL) to encrypt data:\n- Edit `/etc/postfix/main.cf` to enable SSL/TLS."
            ]
        }
    },
    80: {
        "name": "HTTP",
        "description": "Hypertext Transfer Protocol",
        "vulnerabilities": [
            "Sensitive data sent in clear text.",
            "Vulnerable to various web-based attacks (e.g., XSS, CSRF)."
        ],
        "fixes": {
            "windows": [
                "Use HTTPS instead of HTTP to encrypt data:\n- Obtain an SSL certificate and configure IIS to use HTTPS.",
                "Implement web application firewalls (WAF):\n- Use a WAF solution like ModSecurity with IIS."
            ],
            "mac": [
                "Use HTTPS instead of HTTP to encrypt data:\n- Obtain an SSL certificate and configure Apache to use HTTPS.",
                "Implement web application firewalls (WAF):\n- Use a WAF solution like ModSecurity with Apache."
            ],
            "linux": [
                "Use HTTPS instead of HTTP to encrypt data:\n- Obtain an SSL certificate and configure Apache or Nginx to use HTTPS.",
                "Implement web application firewalls (WAF):\n- Use a WAF solution like ModSecurity with Apache or Nginx."
            ]
        }
    },
    110: {
        "name": "POP3",
        "description": "Post Office Protocol v3",
        "vulnerabilities": [
            "Data sent in clear text.",
            "Vulnerable to man-in-the-middle attacks."
        ],
        "fixes": {
            "windows": [
                "Use POP3S (POP3 over SSL) to encrypt data:\n- Configure your mail server (e.g., hMailServer) to use SSL/TLS.",
                "Encourage the use of secure email clients:\n- Recommend clients that support SSL/TLS."
            ],
            "mac": [
                "Use POP3S (POP3 over SSL) to encrypt data:\n- Configure your mail server (e.g., Dovecot) to use SSL/TLS.",
                "Encourage the use of secure email clients:\n- Recommend clients that support SSL/TLS."
            ],
            "linux": [
                "Use POP3S (POP3 over SSL) to encrypt data:\n- Configure your mail server (e.g., Dovecot) to use SSL/TLS.",
                "Encourage the use of secure email clients:\n- Recommend clients that support SSL/TLS."
            ]
        }
    },
    443: {
        "name": "HTTPS",
        "description": "Hypertext Transfer Protocol Secure",
        "vulnerabilities": [
            "SSL/TLS vulnerabilities (e.g., Heartbleed).",
            "Misconfigured SSL/TLS can lead to security issues."
        ],
        "fixes": {
            "windows": [
                "Ensure SSL/TLS configurations follow best practices:\n- Use tools like SSL Labs to test your SSL/TLS configuration.",
                "Regularly update SSL/TLS libraries:\n- Keep your web server and SSL/TLS libraries up-to-date via Windows Update."
            ],
            "mac": [
                "Ensure SSL/TLS configurations follow best practices:\n- Use tools like SSL Labs to test your SSL/TLS configuration.",
                "Regularly update SSL/TLS libraries:\n- Keep your system up-to-date via macOS updates."
            ],
            "linux": [
                "Ensure SSL/TLS configurations follow best practices:\n- Use tools like SSL Labs to test your SSL/TLS configuration.",
                "Regularly update SSL/TLS libraries:\n- Keep your web server and SSL/TLS libraries up-to-date via your package manager (e.g., `sudo apt-get update && sudo apt-get upgrade`)."
            ]
        }
    },
    445: {
        "name": "SMB",
        "description": "Server Message Block",
        "vulnerabilities": [
            "Vulnerable to exploits such as EternalBlue.",
            "Can be used for lateral movement within a network."
        ],
        "fixes": {
            "windows": [
                "Disable SMBv1:\n- Open 'Control Panel' > 'Programs' > 'Turn Windows features on or off' and uncheck 'SMB 1.0/CIFS File Sharing Support'.",
                "Use strong passwords and enable network-level authentication:\n- Configure network security policies in Group Policy."
            ],
            "mac": [
                "Disable SMBv1 in the server configuration:\n- Edit the SMB configuration file (usually `/etc/nsmb.conf`).",
                "Use strong passwords and enable network-level authentication:\n- Configure SMB settings in macOS Server."
            ],
            "linux": [
                "Disable SMBv1 using `smb.conf`:\n- Edit `/etc/samba/smb.conf` and add `server min protocol = SMB2`.",
                "Use strong passwords and enable network-level authentication:\n- Configure Samba settings in `/etc/samba/smb.conf`."
            ]
        }
    }
}


def scan_ports(target):
    results = {}

    for port, info in PORTS_INFO.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            results[port] = {
                "status": "Open",
                "name": info["name"],
                "description": info["description"],
                "vulnerabilities": info["vulnerabilities"],
                "fixes": info["fixes"]
            }
        else:
            results[port] = {
                "status": "Closed",
                "name": info["name"],
                "description": info["description"]
            }
        sock.close()

    return results


def get_os():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        return 'windows'
    elif 'darwin' in os_name:
        return 'mac'
    elif 'linux' in os_name:
        return 'linux'
    else:
        return 'unknown'
