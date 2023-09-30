import requests


def main():
    # zipcode = input("郵便番号<ハイフン無し7桁>は？")
    zipcode = "0287111"

    response = requests.get(
        f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    )

    dic = response.json()

    prefecture_name = dic["results"][0]["address1"]
    city_name = dic["results"][0]["address2"]
    town_name = dic["results"][0]["address3"]

    address = f"{prefecture_name}{city_name}{town_name}"
    print(address)


if __name__ == "__main__":
    # # zipcode = input("郵便番号<ハイフン無し7桁>は？")
    # zipcode = "0287111"

    # response = requests.get(
    #     f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    # )

    # dic = response.json()

    # prefecture_name = dic["results"][0]["address1"]
    # city_name = dic["results"][0]["address2"]
    # town_name = dic["results"][0]["address3"]

    # address = f"{prefecture_name}{city_name}{town_name}"
    # print(address)
    main()
