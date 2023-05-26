# Project Name

CVE-2021-22555 attack script

## Description

This project is an automatic attack tool implemented in Python. It performs various security tests and attacks on a target system running Ubuntu 20.04 with kernel version 5.8.0-48. The tool includes functionalities such as ping, live host detection, full open scan, SSH brute force, and exploitation of the CVE-2021-2255 vulnerability. This project is a part of Network Security course project at National Yang Ming Chiao Tung University.

**Notice**: Since the requirement of the project is single executeable file so we only create a single python file here.

**Target Operating System**: Ubuntu 20.04 with kernel version 5.8.0-48

**Attacker Operating System**: Kali Linux (Version X.X.X)

## Features

- Ping: Checks the reachability of a host.
- Live Host Detection: Identifies live hosts on the network.
- Full Open Scan: Performs a comprehensive scan of open ports on the target system.
- SSH Brute Force: Attempts to guess the SSH credentials using a brute force approach.
- Exploitation of CVE-2021-2255: Executes the exploit for the CVE-2021-2255 vulnerability on the target system.

## Requirements

To run this tool, you need the following:

- Python (version 3.9.13)
- icmplib (version 3.0.3)
- ping3 (version 4.0.4)
- pymetasploit3 (version 1.0.3)
- python-nmap (version 0.7.1)


## Usage

1. Clone the repository:

```bash
git clone https://github.com/masjohncook/netsec-project.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Modify the configuration files or scripts according to your requirements.

4. Execute the main script to run the automatic attack tool:

```bash
sh run_exploit.sh <target-ip>
```

Note: Make sure you have the necessary permissions and legal authorization before conducting any attacks on target systems.

## License


## Disclaimer

The usage of this tool for any unauthorized activities is strictly prohibited. You are solely responsible for any actions you perform using this tool. Make sure to obtain proper authorization and permissions before conducting any security testing or attacks. The developers and contributors of this tool will not be held responsible for any misuse or illegal activities carried out with it.

## Contributing

If you want to contribute to this project, please follow these guidelines:

* Fork the repository and create your own branch for the new feature or bug fix.
* Ensure your code follows the project's coding conventions and style guidelines.
* Provide clear and concise documentation for any changes or additions.
* Test your changes thoroughly to ensure they do not introduce any regressions.
* Submit a pull request, clearly explaining the purpose and changes introduced by your contribution.
* Be responsive to any feedback or suggestions during the review process.

## Issues

If you encounter any issues, bugs, or have suggestions for improvements, please report them in the Issues section of the repository. Follow these guidelines when submitting an issue:

Check if the issue has already been reported by searching through the existing issues.
* Provide a clear and descriptive title for the issue.
* Include all relevant details such as steps to reproduce, error messages, and your environment setup.
* If applicable, provide sample code or scripts to help reproduce the issue.
