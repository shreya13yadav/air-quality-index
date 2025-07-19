df['Date'] = pd.to_datetime(df['Date'])
df.fillna({'PM2.5': df['PM2.5'].median(), 'PM10': df['PM10'].median(), 
           'NO2': df['NO2'].median(), 'SO2': df['SO2'].median()}, inplace=True)
df['AQI_Category'] = pd.cut(df['AQI'], 
                           bins=[0, 50, 100, 200, 300, 400, 500], 
                           labels=['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe'])
df['Year'] = df['Date'].dt.year
df_agg = df.groupby(['City', 'Year']).agg({'PM2.5': 'mean', 'PM10': 'mean', 'AQI': 'mean'}).reset_index()

# Save to CSV for use in Load step
df_agg.to_csv('/kaggle/working/air_quality_transformed.csv', index=False)
print("Data transformed and saved to /kaggle/working/air_quality_transformed.csv")
