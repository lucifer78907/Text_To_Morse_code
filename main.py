import pandas as pd

# making lists out of the provided data using pandas
data = pd.read_csv('MORSE.csv')
letter_list = data['LETTER'].to_list()
print(letter_list)
morse_list = data['CODE'].to_list()
print(morse_list)

# user input
inp_str = input("Enter a String")
output_list=[]
for char in inp_str:
    index_in_char_list = inp_str.index(char)
    morse_char = morse_list[index_in_char_list]
    output_list.append(morse_char)

morse_code = "".join(output_list)
print(morse_code)