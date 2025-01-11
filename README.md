
# PvNSQLGuard

## Description:
PvNSQLGuard is a lightweight and effective SQL injection scanner designed to help security professionals and developers quickly identify SQL injection vulnerabilities in web applications. It allows users to easily test URLs for potential vulnerabilities by scanning query parameters and injecting common SQL payloads. The tool outputs whether a vulnerability is detected or not, providing a simple way to enhance web application security.

## Features:
- Automatic detection of query parameters.
- SQL injection payload testing on detected parameters.
- Color-coded output for ease of use and clarity.
- Easy-to-use command-line interface.

## Project Look:
Here’s what you will see when you run the `PvNSQLGuard` tool:

```
    ____        _   _______ ____    __    ______                     __
   / __ \_   __/ | / / ___// __ \  / /   / ____/_  ______ __________/ /
  / /_/ / | / /  |/ /\__ \/ / / / / /   / / __/ / / / __ `/ ___/ __  /
 / ____/| |/ / /|  /___/ / /_/ / / /___/ /_/ / /_/ / /_/ / /  / /_/ /
/_/     |___/_/ |_//____/\___\_\/_____/\____/\__,_/\__,_/_/   \__,_/   


Developer: Pavan Kamthane
LinkedIn: https://www.linkedin.com/in/pavankamthane/
GitHub: https://github.com/Pavan-Kamthane/PvNSQLGuard

Initializing SQL Injection scanner...

Enter target URL: http://testphp.vulnweb.com/search.php?test=query
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
Detected query parameters: test
Starting SQL injection test on detected parameters...
[Vulnerable] SQL Injection detected on http://testphp.vulnweb.com/search.php?test=query with parameter: test
```

## Example Usage:
```
Enter target URL: http://testphp.vulnweb.com/search.php?test=query
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
Detected query parameters: test
Starting SQL injection test on detected parameters...
[Vulnerable] SQL Injection detected on http://testphp.vulnweb.com/search.php?test=query with parameter: test
```

## Installation:
1. Clone the repository:

```bash
git clone https://github.com/Pavan-Kamthane/PvNSQLGuard.git
cd PvNSQLGuard
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tool:

```bash
python PvNSQLGuard.py
```

## License:
This release is under the MIT License.

