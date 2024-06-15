import os
import csv


def open_wallets():    
    wallets = []
    with open('wallets.txt') as file:
        for a in file.readlines():
            wallets.append(a.lower())
        wallets = [line.strip() for line in wallets]
    return(wallets)


def csv_reader():
    csv_path_list = []
    for i in os.listdir('./protocols'):
        a = ''.join(os.listdir(f'./protocols/{i}'))
        csv_path_list.append(f'./protocols/{i}/{a}')
    return csv_path_list


def checker(wallets, csv_file):
    for file in csv_file:
        with open(file) as file_csv:
            print(f'Read {file} file')
            reader = csv.reader(file_csv, delimiter=',')
            a = file.split('/')
            for lines in reader:
                for wallet in wallets:
                    if lines[0] == wallet:
                        with open('result.txt', 'a') as result:
                            result.write(f'{a[2]}:\n {wallet}: {lines[1]}\n')


def main():
    wallets = open_wallets()
    csv_file = csv_reader()
    checker(wallets, csv_file)


if __name__ == '__main__':
    main()