import os, json, re
from datetime import datetime
from utils import mask_sensitive_data, partial_mask

BASE_DIR = os.path.dirname(__file__)
RULES_PATH = os.path.join(BASE_DIR, "rules.json")
LOG_PATH = os.path.join(BASE_DIR, "alerts.log")

def load_rules():
    """Load DLP detection rules."""
    with open(RULES_PATH, "r") as f:
        return json.load(f)

def log_alert(title, data):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{ts}] ALERT {title}\nData: {data}\n" + "-"*60 + "\n"
    print(message)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(message)

def analyze_payload(payload, rules=None):
    if rules is None:
        rules = load_rules()

    alert_triggered = False

    for rule in rules.get("patterns", []):
        try:
            matches = re.finditer(rule["regex"], payload)
            for match in matches:
                sensitive_data = match.group(0)
                masked_data = partial_mask(sensitive_data)
                alert_triggered = True
                log_alert(f"Potential {rule['name']} leak detected", masked_data)
        except re.error:
            continue

    return alert_triggered
