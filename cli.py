import my_zipcloud
import my_formatter


def main():
    zipcode = input ('郵便番号を入力してください　> ')

    address = my_zipcloud.fetch_address (zipcode)

    output = my_formatter.simple_formatter (zipcode, address)

    print (output)


if __name__ == '__main__':
    main ()
