price_list = {
    'Billie Eilish CD': 0.05,
    '50 Shades Of Gray': 10.18,
    'Celery': 0.22,
    'Orthopedic Cement': 5.17
}
print(price_list['Billie Eilish CD'])

x = int(input('How easy is this client? : '))
new_values = {}

new_values = {key: value * (1+x) for key, value in price_list.items()}

print(new_values)
