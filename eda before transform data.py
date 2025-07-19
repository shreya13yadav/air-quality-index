print("\nFirst 5 rows of raw data:")
print(df.head())

# Number of unique cities and their list
unique_cities = df['City'].nunique()
city_list = df['City'].unique()
print(f"\nNumber of unique cities: {unique_cities}")
print("List of cities:", city_list)

# Percentage of missing data for key columns
missing_percent = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'AQI']].isna().mean() * 100
print("\nPercentage of missing data in key columns:")
print(missing_percent)

# Descriptive statistics
print("\nDescriptive statistics for raw data (before transform):")
print(df[['PM2.5', 'PM10', 'NO2', 'SO2', 'AQI']].describe())

# Histogram of AQI for raw data
plt.figure(figsize=(10, 6))
sns.histplot(df['AQI'], bins=30, kde=True)
plt.title('Distribution of AQI (Raw Data)')
plt.xlabel('AQI')
plt.ylabel('Count')
plt.savefig('/kaggle/working/aqi_histogram_raw.png')
print("AQI histogram (raw data) saved to /kaggle/working/aqi_histogram_raw.png")

# Bar plot of average AQI for top 5 polluted cities
top_cities_aqi = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities_aqi.values, y=top_cities_aqi.index)
plt.title('Top 5 Cities by Average AQI (Raw Data)')
plt.xlabel('Average AQI')
plt.ylabel('City')
plt.savefig('/kaggle/working/top_cities_aqi_raw.png')
print("Top 5 cities AQI plot saved to /kaggle/working/top_cities_aqi_raw.png")
