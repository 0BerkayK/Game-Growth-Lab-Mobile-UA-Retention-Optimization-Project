import pandas as pd
import numpy as np
import os
from datetime import timedelta, datetime

# Constant seed
np.random.seed(42)

# Add Folder
os.makedirs("data", exist_ok=True)

# Random date generator
def random_date(start, end):
    return start + timedelta(days=np.random.randint((end - start).days))

# Date range (for 30 days)
start_date = datetime.today() - timedelta(days=30)
end_date = datetime.today()


# 1. user_acquisition.csv

platforms = ["TikTok", "Meta", "Google UAC"]
creatives = ["A", "B", "C", "D"]
ua_data = []

for i in range(200):
    platform = np.random.choice(platforms)
    creative = np.random.choice(creatives)
    impressions = np.random.randint(5000, 20000)
    clicks = int(impressions * np.random.uniform(0.01, 0.05))
    installs = int(clicks * np.random.uniform(0.2, 0.6))
    cost = round(np.random.uniform(50, 300), 2)
    ua_data.append([platform, creative, impressions, clicks, installs, cost])

df_ua = pd.DataFrame(ua_data, columns=["platform", "creative_id", "impressions", "clicks", "installs", "cost"])
df_ua.to_csv("../data/user_acquisition.csv", index=False)


# 2. installs.csv

install_data = []
for i in range(1000):
    user_id = f"user_{i}"
    platform = np.random.choice(platforms)
    install_date = random_date(start_date, end_date)
    install_data.append([user_id, platform, install_date.date()])

df_installs = pd.DataFrame(install_data, columns=["user_id", "platform", "install_date"])
df_installs.to_csv("../data/installs.csv", index=False)


# 3. sessions.csv

session_data = []
for i in range(1000):
    user_id = f"user_{i}"
    num_sessions = np.random.randint(1, 10)
    for _ in range(num_sessions):
        session_date = random_date(start_date, end_date)
        session_data.append([user_id, session_date.date()])

df_sessions = pd.DataFrame(session_data, columns=["user_id", "session_date"])
df_sessions.to_csv("../data/sessions.csv", index=False)


# 4. purchases.csv

purchase_data = []
items = ["coins", "booster", "lives", "skin"]
for i in range(300):
    user_id = f"user_{np.random.randint(0, 1000)}"
    purchase_date = random_date(start_date, end_date)
    amount = round(np.random.uniform(0.99, 49.99), 2)
    item = np.random.choice(items)
    purchase_data.append([user_id, purchase_date.date(), amount, item])

df_purchases = pd.DataFrame(purchase_data, columns=["user_id", "purchase_date", "amount", "item"])
df_purchases.to_csv("../data/purchases.csv", index=False)

# 5. retention.csv

retention_data = []
for i in range(1000):
    user_id = f"user_{i}"
    install_date = random_date(start_date, end_date)
    d1 = np.random.choice([0, 1], p=[0.4, 0.6])
    d7 = np.random.choice([0, 1], p=[0.7, 0.3])
    d30 = np.random.choice([0, 1], p=[0.9, 0.1])
    retention_data.append([user_id, install_date.date(), d1, d7, d30])

df_retention = pd.DataFrame(retention_data, columns=["user_id", "install_date", "d1_retained", "d7_retained", "d30_retained"])
df_retention.to_csv("../data/retention.csv", index=False)


# 6. game_updates.csv

update_data = []
features = ["New Levels", "UI Overhaul", "Halloween Event", "Bug Fixes", "Daily Rewards", "Multiplayer Mode"]
for i in range(10):
    update_date = random_date(start_date, end_date)
    feature = np.random.choice(features)
    description = f"{feature} released with update #{i+1}"
    update_data.append([update_date.date(), feature, description])

df_updates = pd.DataFrame(update_data, columns=["update_date", "feature", "description"])
df_updates.to_csv("../data/game_updates.csv", index=False)


print("All csv files was created.")
