import json
import os
from datetime import datetime

FEEDBACK_FILE = "feedback.json"


def save_feedback(rating):

    feedback_entry = {"rating": rating, "timestamp": datetime.now().isoformat()}

    # If file exists, load existing data
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(feedback_entry)

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file, indent=4)
