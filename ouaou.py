
hlikia = int(input('Παρακαλώ τυπώστε την ηλικία σας: '))
mounara = int(input('How would you score your looks? : '))
lefta_aisthhmata = int(input('How much money do you have in the bank? : '))

if (hlikia <= 17) and (mounara == 10 or lefta_aisthhmata >= 100000) and not (input('What is your religion: ') == 'Jewish'):
    print('Iaso kokla')

else:
    print('Ta legame')


