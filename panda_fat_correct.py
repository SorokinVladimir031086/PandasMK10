import pandas
import telebot
from openpyxl import Workbook

excel_data_df = pandas.read_excel('result_mk10_0521.xlsx')
df = pandas.DataFrame(excel_data_df)
print(df)
print(df.Player1.unique())
print(df.Player2.unique())
list2=[]
fighter1=[]
fighter2=[]
dohod=[]
TOKEN = '1260366546:AAHmSnNqjDUBfpQwr2D4mTpZKG9_4o4dVUw'
bot = telebot.TeleBot(TOKEN)


for i in df.Player1.unique():
    df1 =df.loc[df['Player1'] == i]
    print(df1)
    for j in df1.Player2.unique():
        df2 = df1.loc[df1['Player2'] == j]
        print(df2)
        list1 = df2['TotalScore'].to_list()
        print(list1)
        for list in list1:
            score1 = list.split(':')[0]
            print(score1)
            score2 = list.split(':')[1]
            print(score2)
            list2.append(int(score1))
            list2.append(int(score2))
            print(list2)
            print(sum(list2))
        fatal = df2['R1'].str.contains('F').sum() + df2['R2'].str.contains('F').sum() + df2['R3'].str.contains(
            'F').sum() + df2['R4'].str.contains('F').sum() + df2['R5'].str.contains('F').sum() + df2['R6'].str.contains(
            'F').sum() + df2['R7'].str.contains('F').sum() + df2['R8'].str.contains('F').sum() + df2['R9'].str.contains(
            'F').sum()
        print(fatal)

        print(df2['Player1'].to_list()[0])
        print(df2['Player2'].to_list()[0])




        df2.loc[df2['R1'].str.contains('F', na=False), 'R1'] = 'F'
        df2.loc[df2['R2'].str.contains('F', na=False), 'R2'] = 'F'
        df2.loc[df2['R3'].str.contains('F', na=False), 'R3'] = 'F'
        df2.loc[df2['R4'].str.contains('F', na=False), 'R4'] = 'F'
        df2.loc[df2['R5'].str.contains('F', na=False), 'R5'] = 'F'
        df2.loc[df2['R6'].str.contains('F', na=False), 'R6'] = 'F'
        df2.loc[df2['R7'].str.contains('F', na=False), 'R7'] = 'F'
        df2.loc[df2['R8'].str.contains('F', na=False), 'R8'] = 'F'
        df2.loc[df2['R9'].str.contains('F', na=False), 'R9'] = 'F'
        print(df2.eq("F").sum(axis=1) * (df2["Fatality"] - 1))
        print((df2.eq("F").sum(axis=1) * (df2["Fatality"] - 1)).sum())

        pluss = float((df2.eq("F").sum(axis=1) * (df2["Fatality"] - 1)).sum() - (sum(list2) - fatal))

        print(pluss)

        if pluss > 0:
            fighter1.append(df2['Player1'].to_list()[0])
            fighter2.append(df2['Player2'].to_list()[0])
            dohod.append(pluss)

        list2.clear()
        df2['Player1'].to_list().clear()
        df2['Player2'].to_list().clear()

df = pandas.DataFrame.from_dict(
    {'Fighter1': fighter1, 'Fighter2': fighter2, 'Dohod s fat': dohod})
df.to_excel('result_fatality.xlsx', header=True, index=False)
