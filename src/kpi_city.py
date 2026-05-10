import sqlite3
import os

def city_kpi(city: str):
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT city, COUNT(*) as total_customers, AVG(monthly_spend) as avg_spend, SUM(churned) as churned_count FROM customers_raw WHERE city = ?"
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        city_name, total_customers, avg_spend, churned_count = result
        churn_rate = (churned_count / total_customers) * 100 if total_customers > 0 else 0
        print(f"City: {city_name}")
        print(f"Total Customers: {total_customers}")
        print(f"Average Monthly Spend: ${avg_spend:.2f}")
        print(f"Churned Customers: {churned_count}")
        print(f"Churn Rate: {churn_rate:.1f}%")
        print("-" * 40)
    else:
        print(f"No data found for city: {city}")
        print("-" * 40)

if __name__ == "__main__":
    print("Testing Mumbai:")
    city_kpi("Mumbai")
    
    print("Testing SQL Injection Attempt:")
    city_kpi("Mumbai' OR 1=1 --")
