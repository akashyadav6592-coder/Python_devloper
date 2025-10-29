import requests
from bs4 import BeautifulSoup

# Step 1: URL define karo
url = "https://example.com"  # Yahan apna URL likho

# Step 2: Request bhejo
response = requests.get(url)

# Step 3: Agar request successful hai
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Title tag extract karo
    title_tag = soup.title.text.strip() if soup.title else "No title found"

    # Sabhi <h2> tags extract karo
    h2_tags = [h2.text.strip() for h2 in soup.find_all("h2")]

    # Step 4: File me likho
    with open("titles.txt", "w", encoding="utf-8") as file:
        file.write(f"Page Title: {title_tag}\n\n")

        if h2_tags:
            file.write("H2 Tags:\n")
            for h2 in h2_tags:
                file.write(f"- {h2}\n")
        else:
            file.write("No <h2> tags found.\n")

    print("✅ Titles saved successfully in 'titles.txt'!")

else:
    print("❌ Failed to fetch page:", response.status_code)

