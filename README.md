
# PvNSQLGuard

PvNSQLGuard is a Python-based SQL injection scanner designed to help identify SQL injection vulnerabilities in web applications by testing URL parameters with a set of common payloads.

## Features:
- Scans URLs for query parameters.
- Tests for SQL injection vulnerabilities using predefined payloads.
- Displays a splash screen with developer information.
- Provides feedback on whether a parameter is vulnerable to SQL injection.

## Installation

### For Windows:
1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. Open Command Prompt or PowerShell and run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:

   ```bash
   python PvNSQLGuard.py
   ```

### For Linux:

1. Install Python on your system if not already installed. You can install it using your package manager:

   For Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. Download the repository using `wget`:

   ```bash
   wget https://github.com/Pavan-Kamthane/PvNSQLGuard/archive/refs/heads/main.zip
   ```

3. Extract the ZIP file:

   ```bash
   unzip main.zip
   ```

4. Navigate to the project directory:

   ```bash
   cd PvNSQLGuard-main
   ```

5. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Run the tool:

   ```bash
   python3 PvNSQLGuard.py
   ```

## Usage

1. Launch the tool with the following command:

   ```bash
   python PvNSQLGuard.py
   ```

2. Enter the target URL when prompted:

   ```bash
   Enter target URL: http://example.com/search.php?test=query
   ```

3. When asked whether the URL has query parameters, you can:
   - Enter `yes` if you know the URL has parameters.
   - Enter `no` if the URL doesn't have parameters.
   - Enter `IDK` (I don't know) for automatic parameter detection.

4. The scanner will test for SQL injection vulnerabilities and display the result.

## Example

Here is an example of how to use the scanner:

```bash
Enter target URL: http://testphp.vulnweb.com/search.php?test=query
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
Detected query parameters: test
Starting SQL injection test on detected parameters...
[Vulnerable] SQL Injection detected on http://testphp.vulnweb.com/search.php?test=query with parameter: test
```

## Look of the Project

### Splash Screen:

When you run the tool, the splash screen displays the following:

```
 ____        _   _______ ____    __    ______                     __
/ __ \_   __/ | / / ___// __ \  / /   / ____/_  ______ __________/ /
/ /_/ / | / /  |/ /\__ \/ / / / / /   / / __/ / / / __ `/ ___/ __  /
/ ____/| |/ / /|  /___/ / /_/ / / /___/ /_/ / /_/ / /_/ / /  / /_/ /
/_/     |___/_/ |_//____/\___\_\/_____/\____/\__,_/\__,_/_/   \__,_/
                                                                  
```

### Developer Info:

- Developer: Pavan Kamthane
- Version: 1.0
- LinkedIn: [Pavan Kamthane](https://www.linkedin.com/in/pavankamthane/)
- GitHub: [PvNSQLGuard](https://github.com/Pavan-Kamthane/PvNSQLGuard)
- Contact: Pavan.Kamthane@studentambassadors.com

## License

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
