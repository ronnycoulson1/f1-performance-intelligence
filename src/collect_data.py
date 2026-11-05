
import requests
import pandas as pd
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Download all 2025 race results
url = "https://api.jolpi.ca/ergast/f1/2025/results/"

rows = []
offset = 0
limit = 100

print("Downloading 2025 F1 season results...")

while True:
    response = requests.get(
        url,
        params={"limit": limit, "offset": offset},
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    races = data["MRData"]["RaceTable"]["Races"]

    if not races:
        break

    count = 0

    for race in races:
        for result in race["Results"]:
            driver = result["Driver"]

            rows.append({
                "Race": race["raceName"],
                "Round": int(race["round"]),
                "Date": race["date"],
                "Driver": (
                    driver["givenName"] + " " +
                    driver["familyName"]
                ),
                "Team": result["Constructor"]["name"],
                "GridPosition": int(result["grid"]),
                "FinishPosition": int(result["position"]),
                "Points": float(result["points"]),
                "Status": result["status"]
            })

            count += 1

    print(f"Downloaded {count} results at offset {offset}")

    if count < limit:
        break

    offset += limit

df = pd.DataFrame(rows)

df = df.sort_values(
    ["Round", "FinishPosition"]
).reset_index(drop=True)

output = DATA_DIR / "f1_2025_results.csv"
df.to_csv(output, index=False)

print("\nData downloaded successfully!")
print("Total races:", df["Round"].nunique())
print("Total driver results:", len(df))
print("Missing values:\n", df.isnull().sum())
print("\nSaved to:", output)
