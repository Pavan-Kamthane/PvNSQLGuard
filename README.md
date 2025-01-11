
# PvNSQLGuard - SQL Injection Scanner

**Developer:** Pavan Kamthane  
**Version:** 1.0  
**LinkedIn:** [Pavan Kamthane](https://www.linkedin.com/in/pavankamthane/)  
**GitHub:** [PavanBoss](https://github.com/PavanBoss)  

---

## Introduction

PvNSQLGuard is a simple Python tool designed to help detect SQL injection vulnerabilities in web applications. It scans URLs and their query parameters to check if they are vulnerable to SQL injection attacks by testing common payloads.

This tool is ideal for penetration testers and developers who want to quickly test their websites or applications for SQL injection vulnerabilities.

---

## Features

- **Automatic detection of query parameters** in the provided URL.
- **Payload-based testing** for SQL injection on detected parameters.
- **Clear output** showing whether a vulnerability is detected or not.

---

## Requirements

To run this tool, you need the following dependencies installed:

- Python 3.x
- `requests` library
- `pyfiglet` library
- `colorama` library

You can install these dependencies using pip:

```bash
pip install requests pyfiglet colorama
```

---

## How to Use

1. **Clone the repository** or download the Python file `PvNSQLGuard.py`.
2. Make sure you have the payloads file (`payloads.txt`) in the same directory as the script. You can find various SQL injection payloads online or create your own.
3. Run the script:

```bash
python PvNSQLGuard.py
```

4. **Provide the target URL** when prompted. The tool will ask if the URL contains query parameters. If you're unsure, you can type `IDK` to automatically scan for query parameters.

---

## Example

### Example 1: URL with known query parameters
```
Enter target URL: http://testphp.vulnweb.com/search.php?test=query
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
Detected query parameters: test
Starting SQL injection test on detected parameters...
[Vulnerable] SQL Injection detected on http://testphp.vulnweb.com/search.php?test=query with parameter: test
```

### Example 2: URL without query parameters
```
Enter target URL: http://example.com
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
No query parameters found.
```

---

## Workflow

1. **Input URL:** The user is prompted to enter the target URL for scanning.
2. **Query Parameters Detection:** If the user does not know whether the URL contains query parameters, the tool will automatically check for them.
3. **SQL Injection Test:** Once parameters are detected, the tool tests them with various SQL injection payloads.
4. **Output:** The result will indicate whether the URL is vulnerable or safe based on the response received.

---

## Customizing Payloads

You can customize the payloads used by the scanner by editing the `payloads.txt` file. Each line in the file should contain a different SQL injection payload.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- The SQL injection payloads used in this tool are taken from publicly available resources for testing purposes.
- Special thanks to the open-source community for their contributions.

