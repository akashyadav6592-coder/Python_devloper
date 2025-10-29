import requests

# URL jiska HTML fetch karna hai
url = "https://example.com"

# Request bhejna
response = requests.get(url)

# Agar request successful hai
if response.status_code == 200:
    print("✅ Page fetched successfully!")
    print(response.text)  # HTML print karega
else:
    print("❌ Failed to fetch page:", response.status_code)