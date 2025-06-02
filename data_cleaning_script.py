import pandas as pd

df = pd.read_csv('marketing_campaign.csv', sep='\t')
print(df.columns)
print("\n🔍 First 5 rows:")
print(df.head())

print("\n📌 Column Names:")
print(df.columns)

print("\n❓ Missing Values Before Cleaning:")
print(df.isnull().sum())
if 'Income' in df.columns:
    df['Income'] = df['Income'].fillna(df['Income'].mean())

df = df.drop_duplicates()
print(f"\n✅ Dataset after removing duplicates: {df.shape}")
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')
for col in ['Education', 'Marital_Status']:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()

df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

if 'year_birth' in df.columns:
    df['year_birth'] = df['year_birth'].astype(int)


df.to_csv('cleaned_customer_data.csv', index=False)
print("\n💾 Cleaned dataset saved as 'cleaned_customer_data.csv'!")


print("\n🧾 Final Dataset Info:")
print(df.info())
