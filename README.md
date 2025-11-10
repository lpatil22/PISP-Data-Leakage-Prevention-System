# Network Data Loss Prevention (DLP) System
This project simulates a Network Data Loss Prevention (DLP) system that monitors network traffic or POST requests for sensitive data like emails, passwords, credit card numbers, and SSNs.

Author: Lavannya Patil
Institution: University of North Carolina at Charlotte

# Project Structure
| File Name                   | Description                                                                 |
| ----------------------------| --------------------------------------------------------------------------- |
| network_dlp.py              | Core logic for detecting sensitive data patterns (email, CC, SSN, etc.).    |
| post_server.py              | Lightweight HTTP POST server that receives data and calls the DLP analyzer. |
| send_payload_http.py        | Interactive script to dynamically send data to the server.                  |
| rules.json                  | JSON file for custom detection rules.                                       |
| utils.py                    | Handles helper functions for data detection and masking.                    |
| README.md                   | Project guide and setup instructions.                                       |


How to Run

Step 1: Go to Your Project Folder

Open PowerShell or Command Prompt as Administrator and navigate to your project directory:

    cd path/to/your/project

Step 2: Check Python Installation

Make sure Python is installed:

    python --version

Step 3: Install Required Packages

Install the requests package:

    pip install requests

Step 4: Open Two Terminals

Terminal A → Runs the DLP POST server

Terminal B → Sends requests to the server

Step 5: Start the POST Server (Terminal A)
    python post_server.py


You should see:

    [INFO] Starting POST server at http://localhost:8000

Step 6: Run the Dynamic Payload Sender (Terminal B)

    python send_payload_http.py


You will see:

    Enter payload to send:

Step 7: Send Test Payloads

Sensitive Data Examples:

    email=alice@example.com
    password=TopSecret@123
    cc=4111-1111-1111-1111
    ssn=123-45-6789


Expected Output / Alert:

    [2025-11-09 14:30:12] ALERT Potential Email Address leak detected
    Data: email=alice@example.com


Non-Sensitive Data Examples:

    message=HelloWorld
    feedback=GreatProject


No alert will be triggered; the server will respond ALLOWED


