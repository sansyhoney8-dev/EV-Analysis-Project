import sqlite3
import time
import random
import matplotlib.pyplot as plt

def run_performance_test():
    # 1. Database Setup
    conn = sqlite3.connect('ev_performance.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS ev_data')
    cursor.execute('''
        CREATE TABLE ev_data (
            id INTEGER PRIMARY KEY,
            model TEXT,
            battery REAL,
            range REAL
        )
    ''')

    # 2. Benchmark Parameters
    data_sizes = [1000, 5000, 10000, 20000, 50000]
    rendering_times = []

    # 3. Execution & Timing
    for count in data_sizes:
        # Generate dummy EV data
        payload = [("Model_EV", random.uniform(40, 100), random.uniform(200, 500)) for _ in range(count)]
        
        start = time.time()
        cursor.executemany('INSERT INTO ev_data (model, battery, range) VALUES (?, ?, ?)', payload)
        conn.commit()
        end = time.time()
        
        duration = end - start
        rendering_times.append(duration)
        print(f"Rendered {count} rows: {duration:.4f}s")

    conn.close()

    # 4. Visualization
    plt.figure(figsize=(8, 5))
    plt.plot(data_sizes, rendering_times, marker='o', color='green')
    plt.title('Amount of Data Rendered to DB vs Time')
    plt.xlabel('Number of Rows')
    plt.ylabel('Time (Seconds)')
    plt.grid(True)
    plt.savefig('performance_results.png')
    plt.show()

if __name__ == "__main__":
    run_performance_test()
