import pandas as pd

data = pd.read_csv('MORSE.csv')
letter_list = data['LETTER'].to_list()
print(letter_list)
