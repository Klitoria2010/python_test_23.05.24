import pandas as pd

l_conect = [
    {
        'user_name': 'kien',
        'passwords': '1234',
        'khui': '49,5'
    },
    {
        'user_name': 'qwewrt',
        'passwords': '9876',
        'khui': '4'
    }
]

df1 = pd.DataFrame(l_conect)
print(df1)
print(type(df1))