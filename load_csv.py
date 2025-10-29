import pandas as pd

# CSV फ़ाइल का नाम (उदाहरण: data.csv)
file_path = 'data.csv'

# CSV लोड करें
df = pd.read_csv(file_path)

# पहले 5 rows दिखाएं
print(df.head())
