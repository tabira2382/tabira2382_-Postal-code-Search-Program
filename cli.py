import my_zipcloud
import my_formatter


def main():
    # ユーザーから入力（郵便番号）を受け取る
    zipcode = input ('郵便番号　> ')

    # 受け取った郵便番号を使ってWebAPIを呼び出して、地名を取得する
    # ex: 8480046 -> 佐賀県伊万里市伊万里町乙
    address = my_zipcloud.fetch_address (zipcode)

    # 取得した地名を最終出力の形式に整形する
    output = my_formatter.simple_formatter (zipcode, address)

    # 　最終的な出力内容を出力する
    print (output)


if __name__ == '__main__':
    main ()
