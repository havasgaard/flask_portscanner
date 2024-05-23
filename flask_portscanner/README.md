# Flask Port Scanner

## Overview

The Flask Port Scanner is a web-based application that scans a given target IP address for open ports and provides detailed information about potential vulnerabilities and recommended fixes for each open port. The application is built using Flask, a lightweight web framework for Python, and includes both a user-friendly web interface and a powerful port scanning backend.

## Features

- Scan a target IP address for common ports.
- Display port status (open/closed) with additional details for open ports.
- Provide descriptions, potential vulnerabilities, and quick fixes for open ports.
- Cross-platform support with specific recommendations for Windows, macOS, and Linux.
- User-friendly web interface with a responsive design.


## Installation

Follow these steps to install and run the Flask Port Scanner on your local machine.

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/flask-portscanner.git
    cd flask-portscanner
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

      ```sh
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```sh
      source venv/bin/activate
      ```

4. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**

    ```sh
    flask run --host=0.0.0.0 --port=3001
    ```

6. **Access the application**

    Open your web browser and go to `http://127.0.0.1:3001`.

## Usage

1. Open the Flask Port Scanner in your web browser.
2. Enter the target IP address you want to scan.
3. Click on the "Scan" button to start the scan.
4. The results page will display the status of common ports, including additional details for open ports such as descriptions, potential vulnerabilities, and quick fixes.

## Customization

You can customize the list of ports and the corresponding information in the `scanner.py` file located in the `app/scanner/` directory. Add or modify entries in the `PORTS_INFO` dictionary to suit your needs.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows best practices and includes appropriate tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Socket](https://docs.python.org/3/library/socket.html) - Used for network communication.

---

Thank you for using the Flask Port Scanner! If you have any questions or feedback, feel free to open an issue on GitHub.
