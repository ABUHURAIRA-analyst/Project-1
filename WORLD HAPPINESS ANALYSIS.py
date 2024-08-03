import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# File path
csv_file_path = "C:/Users/ABU HURAIRAH & SONS/Downloads/archive/World-happiness-report-2024.csv"

# Load the dataset
df = pd.read_csv(csv_file_path)

# Data cleaning
df = df.dropna()  # Drop rows with missing values

# Visualization
# Distribution of happiness scores
plt.figure(figsize=(10, 6))
sns.histplot(df['Ladder score'], kde=True)
plt.title('Distribution of Happiness Scores')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
# Selecting only numeric columns for correlation
numeric_df = df.select_dtypes(include=[float, int])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Pairplot of selected features
selected_features = ['Ladder score', 'Log GDP per capita', 'Social support', 'Healthy life expectancy',
                     'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']
sns.pairplot(df[selected_features])
plt.show()

# Data Visualization
# Bar chart for top 10 happiest countries
top_10_happiest = df.nlargest(10, 'Ladder score')
fig = px.bar(top_10_happiest, x='Country name', y='Ladder score', title='Top 10 Happiest Countries')
fig.show()

# Scatter plot for Happiness Score vs. GDP per Capita
fig = px.scatter(df, x='Log GDP per capita', y='Ladder score',
                 title='Happiness Score vs. GDP per Capita',
                 labels={'Log GDP per capita': 'GDP per Capita', 'Ladder score': 'Happiness Score'},
                 hover_data=['Country name'])
fig.show()

# Heat map for global happiness scores
fig = px.choropleth(df, locations="Country name",
                    locationmode='country names',
                    color="Ladder score",
                    hover_name="Country name",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='Global Happiness Scores')
fig.show()

# Detailed Analysis
# Analysis of regional happiness
numeric_columns = df.select_dtypes(include=[float, int]).columns
region_group = df.groupby('Regional indicator')[numeric_columns].mean().reset_index()
fig = px.bar(region_group, x='Regional indicator', y='Ladder score',
             title='Average Happiness Score by Region')
fig.show()

# Relationship between social support and happiness
fig = px.scatter(df, x='Social support', y='Ladder score',
                 title='Happiness Score vs. Social Support',
                 labels={'Social support': 'Social Support', 'Ladder score': 'Happiness Score'},
                 hover_data=['Country name'])
fig.show()

# Relationship between life expectancy and happiness
fig = px.scatter(df, x='Healthy life expectancy', y='Ladder score',
                 title='Happiness Score vs. Healthy Life Expectancy',
                 labels={'Healthy life expectancy': 'Healthy Life Expectancy', 'Ladder score': 'Happiness Score'},
                 hover_data=['Country name'])
fig.show()

# Relationship between freedom to make life choices and happiness
fig = px.scatter(df, x='Freedom to make life choices', y='Ladder score',
                 title='Happiness Score vs. Freedom to Make Life Choices',
                 labels={'Freedom to make life choices': 'Freedom to Make Life Choices', 'Ladder score': 'Happiness Score'},
                 hover_data=['Country name'])
fig.show()

print("Analysis Completed")
