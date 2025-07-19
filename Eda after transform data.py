plt.figure(figsize=(10, 6))
sns.heatmap(df_agg[['PM2.5', 'PM10', 'AQI']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Aggregated Air Quality Metrics')
plt.savefig('/kaggle/working/correlation_matrix_agg.png')
print("Correlation matrix (aggregated data) saved to /kaggle/working/correlation_matrix_agg.png")

# AQI trends for Delhi
delhi_df = df[df['City'] == 'Delhi'].groupby('Year')['AQI'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='AQI', data=delhi_df, marker='o')
plt.title('Average AQI in Delhi (2015-2020)')
plt.xlabel('Year')
plt.ylabel('Average AQI')
plt.savefig('/kaggle/working/delhi_aqi_trend.png')
print("Delhi AQI trend plot saved to /kaggle/working/delhi_aqi_trend.png")

# AQI category distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='AQI_Category', data=df, order=['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe'])
plt.title('Distribution of AQI Categories (Transformed Data)')
plt.xlabel('AQI Category')
plt.ylabel('Count')
plt.savefig('/kaggle/working/aqi_category_distribution.png')
print("AQI category distribution plot saved to /kaggle/working/aqi_category_distribution.png")
