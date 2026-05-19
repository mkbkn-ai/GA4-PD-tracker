# Pipedrive PPC Tracker

This project provides a simple Python server (Flask) & HTML form to capture leads with PPC tracking info and send them to Pipedrive.

## How it Works

- Website visitors land from PPC ads (UTM or GCLID in URL).
- The lead form captures these parameters in hidden fields.
- Upon form submit, the backend sends the lead and source info to Pipedrive via API.

## Setup

1. Clone this repo and navigate to the folder.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Set your Pipedrive API key in your environment:
    ```bash
    export PIPEDRIVE_API_TOKEN=YOUR_API_TOKEN
    ```
4. Run the app:
    ```bash
    python app.py
    ```
5. Open [http://localhost:5000](http://localhost:5000) and submit a sample lead!

## Notes

- You must create the corresponding custom fields (e.g., utm_source, gclid) in Pipedrive and adjust the `utils.py` accordingly.
- For real-world use, secure the API token and add error handling.
