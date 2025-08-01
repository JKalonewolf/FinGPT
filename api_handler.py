import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

RBI_API_KEY = os.getenv("579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b")
SEBI_API_KEY = os.getenv("SEBI_API_KEY")
FOREX_API_KEY = os.getenv("1085a43e952adc9c18e19a06943231ea")


class APIHandler:
    def __init__(self):
        self.rbi_base_url = "https://rbi.org.in/"
        self.sebi_base_url = "https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=4&smid=7"
        self.currency_api_url = "https://openexchangerates.org/api/latest.json"
        self.currency_api_key = os.getenv("CURRENCY_API_KEY")

    # ---------------- RBI Updates ----------------
    def get_rbi_updates(self):
        try:
            response = requests.get(f"{self.rbi_base_url}Scripts/BS_PressReleaseDisplay.aspx")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            updates = soup.find_all("a", class_="link1")
            return [{"title": update.text.strip(), "link": f"{self.rbi_base_url}{update['href']}"} for update in updates[:5]]
        except Exception as e:
            print(f"Error fetching RBI updates: {e}")
            return []

    # ---------------- SEBI Circulars ----------------
    def get_sebi_circulars(self):
        try:
            response = requests.get(self.sebi_base_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            circulars = soup.find_all("a", class_="pdf-link")
            return [{"title": circ.text.strip(), "link": circ['href']} for circ in circulars[:5]]
        except Exception as e:
            print(f"Error fetching SEBI circulars: {e}")
            return []

    # ---------------- Currency Exchange Rates ----------------
    def get_currency_rates(self):
        try:
            response = requests.get(f"{self.currency_api_url}?app_id={self.currency_api_key}")
            response.raise_for_status()
            data = response.json()
            return data.get("rates", {})
        except Exception as e:
            print(f"Error fetching currency rates: {e}")
            return {}

# Test the API Handler
if __name__ == "__main__":
    api_handler = APIHandler()
    print("RBI Updates:", api_handler.get_rbi_updates())
    print("SEBI Circulars:", api_handler.get_sebi_circulars())
    print("Currency Rates:", api_handler.get_currency_rates())


def get_rbi_updates():
    return None


def get_sebi_circulars():
    return None


def get_forex_rates():
    return None