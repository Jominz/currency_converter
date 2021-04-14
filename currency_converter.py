import requests
from terminaltables import AsciiTable

# supported currencies
currencies = [['ID', 'Currency Name', 'ISO code'],
              ['0', 'United States dollar', 'USD'], ['1', 'Euro', 'EUR'], ['2', 'Japanese yen', 'JPY'],
              ['3', 'Pound sterling', 'GBP'], ['4', 'Australian dollar', 'AUD'], ['5', 'Canadian dollar', 'CAD'],
              ['6', 'Swiss franc', 'CHF'], ['7', 'Renminbi', 'CNY'], ['8', 'Hong Kong dollar', 'HKD'],
              ['9', 'New Zealand dollar', 'NZD'], ['10', 'Swedish krona', 'SEK'], ['11', 'South Korean won', 'KRW'],
              ['12', 'Singapore dollar', 'SGD'], ['13', 'Norwegian krone', 'NOK'], ['14', 'Mexican peso', 'MXN'],
              ['15', 'Indian rupee', 'INR'], ['16', 'Russian ruble', 'RUB'], ['17', 'South African rand', 'ZAR'],
              ['18', 'Turkish lira', 'TRY'], ['19', 'Brazilian real', 'BRL'],
              ['21', 'Danish krone', 'DKK'], ['22', 'Polish złoty', 'PLN'], ['23', 'Thai baht', 'THB'],
              ['24', 'Indonesian rupiah', 'IDR'], ['25', 'Hungarian forint', 'HUF'], ['26', 'Czech koruna', 'CZK'],
              ['27', 'Israeli new shekel', 'ILS'], ['28', 'Chilean peso', 'CLP'], ['29', 'Philippine peso', 'PHP'],
              ['30', 'UAE dirham', 'UAE'], ['31', 'Colombian peso', 'COP'], ['32', 'Saudi riyal', 'SAR'],
              ['33', 'Malaysian ringgit', 'MYR'], ['34', 'Romanian leu', 'RON']]

print(AsciiTable(currencies).table)

try:
    first_currency = input('\nPlease select the number of the first currency:\n')
    first_currency_code = currencies[int(first_currency)+1][2]
    second_currency = input('\n Please select the number of the second currency:\n')
    second_currency_code = currencies[int(second_currency) + 1][2]
    amount = input(
        '\n Please select the amount of ' + first_currency_code + ' to convert in ' + second_currency_code + '\n')

except ValueError:
    print("Sorry, I didn't understand that. Be sure to select the correct numbers!")
    exit()

r = requests.get('https://api.exchangeratesapi.io/latest?base=' + first_currency_code + '&symbols=' + second_currency_code)
json = r.json()
rate = json["rates"][second_currency_code]
converted = str(float(amount)*rate)

print('Here your conversion: \n')
print(amount + ' ' + first_currency_code + ' equals to ' + converted + ' ' + second_currency_code)
