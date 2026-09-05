# Nuzul Booking Validation Safeguard

## Rationale
This tool provides automated boundary and integration testing for booking endpoints to catch date-logic anomalies and bad payloads before deployment. It directly targets the vulnerability exploited in ticket NZL-217.

## How to Run
1. Clone the repository:
   `git clone https://github.com/laotof/main.py.git`
2. Run the test suite:
   `python main.py`

## Expected Behavior & Output
- **PASS**: The API blocks invalid checkout dates (returns 400 Bad Request).
- **PASS / WARNING**: The API blocks the invalid request but returns a non-standard status code (e.g., 418).
- **FAIL**: The API accepts an invalid checkout date (returns 200 OK).
