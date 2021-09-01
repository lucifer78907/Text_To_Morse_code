import pandas as pd

# making lists out of the provided data using pandas
data = pd.read_csv('MORSE.csv')
letter_list = data['LETTER'].to_list()
morse_list = data['CODE'].to_list()

# user input
inp_str = input("Enter a String\n")
output_list=[]
for char in inp_str:
    index_in_char_list = letter_list.index(char)
    morse_char = morse_list[index_in_char_list]
    output_list.append(morse_char)

morse_code = "".join(output_list)
print(f'The Morse Code Generated is {morse_code}')