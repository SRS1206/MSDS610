import pandas as pd

def feature_engineering(live_df):
    
   live_df["neighbourhood_density"] = live_df.groupby("neighbourhood")["neighbourhood"].transform("count")
   
   room_type_mapping = {0: "Entire home/apt", 1: "Private room", 2: "Shared room", 3: "Hotel room"}
   room_type_per_neighbourhood = live_df.groupby(["neighbourhood", "room_type"]).size().unstack(fill_value=0)
   room_type_per_neighbourhood.rename(columns=room_type_mapping, inplace=True)
   live_df = live_df.merge(room_type_per_neighbourhood, on="neighbourhood", how="left")

   avg_price = live_df.groupby(["neighbourhood", "room_type"])["price"].mean().reset_index()
   live_df = live_df.merge(avg_price, on=["neighbourhood", "room_type"], how="left", suffixes=("", "_avg"))
   
   return live_df
