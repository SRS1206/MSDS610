import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocess_data(live_df):
 
    # Drop unnecessary columns
    drop_columns = ["id", "name", "host_id", "host_name", "neighbourhood_group", "last_review"]
    live_df = live_df.drop(columns=drop_columns)

    # Fill missing values
    live_df['reviews_per_month'].fillna(0, inplace=True)

    # Encode categorical variables
    label_encoder = LabelEncoder()
    live_df["neighbourhood"] = label_encoder.fit_transform(live_df["neighbourhood"])
    live_df["room_type"] = label_encoder.fit_transform(live_df["room_type"])

    # Round and convert 'reviews_per_month'
    live_df['reviews_per_month'] = np.ceil(live_df['reviews_per_month'] * 1000) / 1000
    live_df['reviews_per_month'] = np.ceil(live_df['reviews_per_month']).astype(int)

    return live_df
