import pandas as pd

with open('BAND.dat') as f:
    data = f.readlines()[1]
    n = int(data.split()[-1])
    NKPTS = int(data.split()[-2])
    print(n, NKPTS)
    f.close()

with open('BAND.dat') as f:
    # 删除前两行
    data = f.readlines()[2:]


# x轴创建
x = []

for h in data[1:NKPTS+1]:
    x.append(float(h.split()[0]))
total_band = pd.DataFrame({'x': x})

for i in range(0, n, 1):
    k = []
    e1 = []
    # e2 = []

    band = data[i * (NKPTS+2):(i + 1) * NKPTS+2][1:-1]


    # 读取能带值
    for band_data in band:

        k.append(float(band_data.split()[0]))
        e1.append(float(band_data.split()[1]))
        # e2.append(float(band_data.split()[2]))

    # 创建表 x energy1 energy2 并排序
    # band = pd.DataFrame({'x': k, 'energy1': e1, 'energy2': e2})
    band = pd.DataFrame({'x': k, 'energy1': e1})
    band = band.sort_values(by='x', ascending=True).reset_index(drop=True).drop('x', axis=1)

    # 合并
    total_band = pd.concat([total_band, band], axis=1)

# 输出成excel表格
total_band.to_excel('./band.xlsx', index=False, header=False)


