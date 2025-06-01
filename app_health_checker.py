import requests
import sys

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        if 200 <= response.status_code < 400:
            print(f"Application is UP (HTTP {response.status_code})")
            return True
        else:
            print(f"Application is DOWN (HTTP {response.status_code})")
            return False
    except requests.RequestException as e:
        print(f"Application is DOWN (Exception: {e})")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_health_checker.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    check_app_health(url)
