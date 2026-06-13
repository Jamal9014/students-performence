import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/student_performance.csv')

plt.figure(figsize=(10,4))
plt.bar(df['name'],df['math'],color='yellow',alpha=0.8)
plt.xlabel("Student Name")
plt.ylabel("Math Score")
plt.title("Math score of each student")
plt.tight_layout()
plt.savefig('output/bar_chart.png')
plt.show()