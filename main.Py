import json
import urllib.error
import urllib.request

API_URL = "https://restful-booker.herokuapp.com/booking"


def test_invalid_date_logic():
  """اختبار رفض الـ API للحجوزات التي يكون فيها تاريخ الخروج قبل تاريخ الدخول."""
  payload = {
      "firstname": "Fahad",
      "lastname": "Al-Otaibi",
      "totalprice": 250,
      "depositpaid": True,
      "bookingdates": {"checkin": "2026-08-15", "checkout": "2026-08-12"},
      "additionalneeds": "Breakfast",
  }

  headers = {"Content-Type": "application/json"}
  req = urllib.request.Request(
      API_URL, data=json.dumps(payload).encode("utf-8"), headers=headers
  )

  try:
    with urllib.request.urlopen(req, timeout=10) as response:
      if response.getcode() == 200:
        print(
            "[FAIL] Test Failed: API accepted a checkout date prior to checkin"
            " date."
        )
        return False
  except urllib.error.HTTPError as e:
    if e.code == 400:
      print(
          "[PASS] Test Passed: API correctly rejected invalid booking dates"
          " (400 Bad Request)."
      )
      return True
    elif e.code == 418:
      print(
          "[PASS/WARNING] API rejected invalid dates, but returned"
          " non-standard status code 418."
      )
      return True
    else:
      print(f"[FAIL] Unexpected HTTP status code: {e.code}")
      return False
  except Exception as e:
    print(f"[ERROR] Execution error: {e}")
    return False


if __name__ == "__main__":
  print("--- Running Nuzul Release Safeguard Suite ---")
  test_invalid_date_logic()
