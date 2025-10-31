import pandas as pd

df = pd.read_csv("coal_dataset_10k_5years.csv")

gas_columns = ['CO2_ppm', 'CH4_ppm', 'SO2_ppm', 'NOx_ppm', 'PM2_5', 'PM10']
df = df.dropna(subset=gas_columns + ['Date'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

avg_emissions = df[gas_columns].mean().round(2).to_dict()

df['Month'] = df['Date'].dt.month_name().str[:3]
monthly_avg = (
    df.groupby('Month')[['CO2_ppm', 'CH4_ppm', 'PM2_5', 'PM10']]
    .mean()
    .reindex(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    .reset_index()
)

output_data = {
    "average_emissions_ppm": avg_emissions,
    "monthly_data": monthly_avg.to_dict(orient='records')
}

print(output_data)
