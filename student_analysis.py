import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('student_data.csv')

data['Result'] = data['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

average_marks = data['Marks'].mean()
average_hours = data['StudyHours'].mean()

plt.figure(figsize=(8,5))
sns.scatterplot(x='StudyHours', y='Marks', hue='Result', data=data)
plt.title('Study Hours vs Marks')
plt.tight_layout()
plt.savefig('screenshots/marks_vs_hours.png')
plt.show()

result_count = data['Result'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(result_count, labels=result_count.index, autopct='%1.1f%%')
plt.title('Pass vs Fail Distribution')
plt.tight_layout()
plt.savefig('screenshots/pass_fail_distribution.png')
plt.show()

print("Average Marks:", average_marks)
print("Average Study Hours:", average_hours)
print("\nResult Distribution:")
print(result_count)
