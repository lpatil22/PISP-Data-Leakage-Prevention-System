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


# How to run
Step 1: Go to Your Project Folder
    Open PowerShell or Command Prompt as Adminstrator and navigate to your project path:
    cd go to the drectory where the code is present.
Step 2: Check Python Installation:
    python --version
Step 3: Install Required Packages:
    pip install requests
Step 4: Open Two Terminals:
    Terminal A -> runs the DLP POST server
    Terminal B -> sends requests
    In Terminal A: Start the POST Server:
        python post_server.py
        You should see something like Starting POST server at http://localhost:8000
    In Terminal B: Run the Dynamic Payload Sender:
        python send_payload_http.py
        You will see somthing like Enter payload to send:
Step 5: Send Test Payloads:
    Try sending sensitive and non-sensitive data:
        Sensitive Data:
            email=alice@example.com
            password=TopSecret@123
            cc=4111-1111-1111-1111
            ssn=123-45-6789
        output:
            [2025-11-09 14:30:12] ALERT Potential Email Address leak detected
            Data: email=alice@example.com

        Non Sensitive Data:
            message=HelloWorld
            feedback=GreatProject
        No alert, meaning data is clean.



