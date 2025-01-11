```markdown
# PvNSQLGuard

PvNSQLGuard is a simple yet effective tool designed to detect SQL injection vulnerabilities in web applications. It scans a given URL for query parameters and tests them with common SQL injection payloads to check for vulnerabilities.

## Features

- Scans URLs for query parameters
- Tests parameters with SQL injection payloads
- Displays the result as either "Vulnerable" or "Safe"
- Easy to use with color-coded output for better readability

## Requirements

- Python 3.x
- `requests` library
- `pyfiglet` library
- `colorama` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Pavan-Kamthane/PvNSQLGuard.git
    ```
   
2. Navigate into the project directory:
    ```bash
    cd PvNSQLGuard
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the `payloads.txt` file from the repository or create your own payload file.

## Usage

1. Run the tool:
    ```bash
    python PvNSQLGuard.py
    ```

2. Enter the target URL when prompted. Example:
    ```text
    http://example.com/search.php?query=test
    ```

3. Indicate whether the URL has query parameters by typing `yes`, `no`, or `IDK` (I don't know).

4. If you chose `IDK`, the tool will automatically detect query parameters and perform the SQL injection test.

5. The tool will provide feedback if any vulnerabilities are detected.

## Example

```bash
Enter target URL: http://testphp.vulnweb.com/search.php?test=query
Does this URL have query parameters? (yes/no) or 'IDK': IDK
Scanning URL for query parameters...
Detected query parameters: test
Starting SQL injection test on detected parameters...
[Vulnerable] SQL Injection detected on http://testphp.vulnweb.com/search.php?test=query with parameter: test
```

## Contact

- Developer: Pavan Kamthane
- LinkedIn: [https://www.linkedin.com/in/pavankamthane/](https://www.linkedin.com/in/pavankamthane/)
- GitHub: [https://github.com/Pavan-Kamthane/PvNSQLGuard](https://github.com/Pavan-Kamthane/PvNSQLGuard)

## License

This project is open source and available under the MIT License. See the LICENSE file for more information.
```