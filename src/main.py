import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("car.csv")

while True:
    print("Please choose an option:")
    print("1. View visualizations")
    print("2. Get statistical information")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("Visualization Options:")
        print("1. Sales Price Variation Across Car Models")
        print("2. Distribution of Units Sold Across Car Models")
        print("3. Manufacturer Total Sales")
        print("4. Sales Price Distribution by Manufacturing Year")
        print("5. Trends in Units Sold over Time")
        print("6. Outliers in Sales Price and Units Sold")
        print("7. Correlation between Sales Price and Units Sold")
        print("8. Sales Revenue Variation Across Car Models")
        print("9. Market Share of Manufacturers")
        print("10. Seasonal Patterns in Car Sales")

        visualization_choice = input("Enter the visualization option (1-10): ")

        if visualization_choice == "1":
            plt.figure(figsize=(10, 6))
            plt.bar(data['Car Model'], data['Sales Price'])
            plt.xlabel('Car Model')
            plt.ylabel('Sales Price')
            plt.title('Sales Price Variation Across Car Models')
            plt.xticks(rotation=90)
            plt.show()

        elif visualization_choice == "2":
            plt.figure(figsize=(10, 6))
            plt.bar(data['Car Model'], data['Units Sold'])
            plt.xlabel('Car Model')
            plt.ylabel('Units Sold')
            plt.title('Distribution of Units Sold Across Car Models')
            plt.xticks(rotation=90)
            plt.show()

        elif visualization_choice == "3":
            manufacturer_sales = data.groupby('Manufacturer')['Units Sold'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 6))
            manufacturer_sales.plot(kind='bar')
            plt.xlabel('Manufacturer')
            plt.ylabel('Total Units Sold')
            plt.title('Manufacturer Total Sales')
            plt.xticks(rotation=0)
            plt.show()

        elif visualization_choice == "4":
            plt.figure(figsize=(10, 6))
            data.boxplot(column='Sales Price', by='Year')
            plt.xlabel('Manufacturing Year')
            plt.ylabel('Sales Price')
            plt.title('Sales Price Distribution by Manufacturing Year')
            plt.xticks(rotation=45)
            plt.show()

        elif visualization_choice == "5":
            plt.figure(figsize=(10, 6))
            sales_by_year = data.groupby('Year')['Units Sold'].sum()
            sales_by_year.plot(kind='line', marker='o')
            plt.xlabel('Year')
            plt.ylabel('Total Units Sold')
            plt.title('Trends in Units Sold over Time')
            plt.xticks(rotation=0)
            plt.show()

        elif visualization_choice == "6":
            plt.figure(figsize=(10, 6))
            plt.boxplot([data['Sales Price'], data['Units Sold']], labels=['Sales Price', 'Units Sold'])
            plt.ylabel('Value')
            plt.title('Outliers in Sales Price and Units Sold')
            plt.show()

        elif visualization_choice == "7":
            plt.figure(figsize=(10, 6))
            plt.scatter(data['Sales Price'], data['Units Sold'])
            plt.xlabel('Sales Price')
            plt.ylabel('Units Sold')
            plt.title('Correlation between Sales Price and Units Sold')
            plt.show()

        elif visualization_choice == "8":
            data['Sales Revenue'] = data['Sales Price'] * data['Units Sold']
            plt.figure(figsize=(10, 6))
            plt.bar(data['Car Model'], data['Sales Revenue'])
            plt.xlabel('Car Model')
            plt.ylabel('Sales Revenue')
            plt.title('Sales Revenue Variation Across Car Models')
            plt.xticks(rotation=90)
            plt.show()

        elif visualization_choice == "9":
            total_sales = data['Units Sold'].sum()
            manufacturer_market_share = data.groupby('Manufacturer')['Units Sold'].sum() / total_sales
            plt.figure(figsize=(10, 6))
            manufacturer_market_share.plot(kind='pie', autopct='%1.1f%%')
            plt.ylabel('')
            plt.title('Market Share of Manufacturers')
            plt.show()

        elif visualization_choice == "10":
            monthly_sales = data.groupby(pd.to_datetime(data['Year'], format='%Y-%m-%d').dt.month)['Units Sold'].sum()
            plt.figure(figsize=(10, 6))
            monthly_sales.plot(kind='bar')
            plt.xlabel('Month')
            plt.ylabel('Total Units Sold')
            plt.title('Seasonal Patterns in Car Sales')
            plt.xticks(rotation=0)
            plt.show()

    elif choice == "2":
        print("Statistical Information Options:")
        print("1. Total units sold for all car models")
        print("2. Car model with the highest sales price")
        print("3. Car model with the lowest sales price")
        print("4. Average sales price of all car models")
        print("5. Average number of units sold for all car models")

        statistical_choice = input("Enter the statistical information option (1-5): ")

        if statistical_choice == "1":
            total_units_sold = data['Units Sold'].sum()
            print("Total units sold:", total_units_sold)

        elif statistical_choice == "2":
            car_model_max_price = data.loc[data['Sales Price'].idxmax(), 'Car Model']
            print("Car model with the highest sales price:", car_model_max_price)

        elif statistical_choice == "3":
            car_model_min_price = data.loc[data['Sales Price'].idxmin(), 'Car Model']
            print("Car model with the lowest sales price:", car_model_min_price)

        elif statistical_choice == "4":
            average_sales_price = data['Sales Price'].mean()
            print("Average sales price:", average_sales_price)

        elif statistical_choice == "5":
            average_units_sold = data['Units Sold'].mean()
            print("Average units sold:", average_units_sold)

    elif choice == "3":
        print("Exiting the program...\nProgram exit successful...\nThankyou for using :) ")
        break

    else:
        print("Invalid choice. Please try again.\n")
