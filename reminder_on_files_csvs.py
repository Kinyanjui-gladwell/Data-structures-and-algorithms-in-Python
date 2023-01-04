import csv

file_name = 'countries.csv'
header = ['name', 'area', 'countrycode2', 'countrycode3']
data = [
    ['Afghanistan', 652090, 'AF', 'AFG'],
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']]
with open(file_name, 'w', newline='') as file_object:
    writer = csv.writer(file_object)
    #write the header
    writer.writerow(header)
    #write the data into rows
    writer.writerows(data)


#writing using dictwriter
fieldnames = ['name', 'area', 'country_code2', 'country_code3']
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]
with open('country_codes.csv', "w", newline='') as fp:
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)