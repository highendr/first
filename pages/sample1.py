import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample2.csv')  # CSV: 연도별 인구수 예시

df.plot(x='년도', y='인구수', kind='line')
plt.title('년도별 인구 변화')
plt.xlabel('년도')
plt.ylabel('인구수')
plt.show()
