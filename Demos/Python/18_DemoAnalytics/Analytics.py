# Step 1 - Import required libraries
import pandas as pd;
import matplotlib.pyplot as plt;

# Step 2 - Loading the sales data and target data from CSV and Excel files respectively
sales_df = pd.read_csv('sales_data.csv');
target_df = pd.read_excel('sales_targets.xlsx');

# Step 3 - Data Cleaning: Handling missing values and duplicates

# Dropping duplicate rows
sales_df.drop_duplicates(inplace=True);

# Convert Sales_Amount Column to numeric, coercing errors to NaN
sales_df['Sales_Amount'] = pd.to_numeric(sales_df['Sales_Amount'], errors='coerce');

# Dropping rows with any missing values
sales_df.dropna(inplace=True);

# Verify the Cleaned Data
print("Cleaned Sales Data:");
# print(sales_df.info());
# print(sales_df.head());

# Step 4 -  Data Analysis: Merging sales data with target data and calculating performance metrics
# Filter the data & analyze only for East region sales
# east_sales = sales_df[sales_df['Region'] == 'East'];
# print("East Region Sales Data:");
# print(east_sales);

# Grouping the data by region
region_group = sales_df.groupby('Region');

# Aggregating the sales data to calculate total sales and average sales per region
# region_sales = region_group['Sales_Amount'].agg(['sum', 'mean']);
region_sales = region_group["Sales_Amount"].sum();
# print("Sales Performance by Region:");
# print(region_sales);

# Average sales per City
# city_avg = sales_df.groupby('City')['Sales_Amount'].mean();
# print(city_avg);

# Multiple Aggregations
# summary = sales_df.groupby("Region")["Sales_Amount"].agg(
#     ["sum", "mean", "max", "min"]
# );
# print(summary);

# Step 5 - Merge Sales Data & Sales Target Data
# actual_sales = sales_df.groupby(
#     "Region"
# )["Sales_Amount"].sum().reset_index();

# performance = pd.merge(
#     actual_sales,
#     target_df,
#     on="Region"
# );

# performance["Achievement %"] = (
#     performance["Sales_Amount"] /
#     performance["Target_Sales"]
# ) * 100;

# print(performance);

# Step 6 - Data Visualization
# Line Chart
# customer_type_sales = sales_df.groupby("Customer_Type")["Sales_Amount"].sum();
# print(customer_type_sales);
# customer_type_sales.plot(kind = "line", marker = "o", figsize = (15, 5));
# plt.title("Customer Type Sales Trend");
# # plt.xlabel("Customer Type");
# # plt.ylabel("Sales");
# plt.grid(True);
# plt.show();

# Pie Chart
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7,7)
)

plt.title("Regional Sales Contribution")
plt.ylabel("")
plt.show()