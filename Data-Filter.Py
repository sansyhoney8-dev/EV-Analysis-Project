import sqlite3

def filter_ev_data():
    conn = sqlite3.connect('ev_performance.db')
    cursor = conn.cursor()

    # User Input simulation
    min_range = 400.0
    
    # 1. SQL Query with Filtering Logic
    print(f"Filtering for EVs with range > {min_range} km...")
    cursor.execute("SELECT * FROM ev_data WHERE range > ?", (min_range,))
    
    rows = cursor.fetchall()

    # 2. Display the filtered results
    print("-" * 30)
    print(f"Total Matches Found: {len(rows)}")
    print("-" * 30)
    
    # Show first 5 matches for verification
    for row in rows[:5]:
        print(f"ID: {row[0]} | Model: {row[1]} | Battery: {row[2]}kWh | Range: {row[3]:.2f}km")

    conn.close()

if __name__ == "__main__":
    filter_ev_data()
