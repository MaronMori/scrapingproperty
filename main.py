import tkinter
from tkinter import ttk
import scraping


def center_window(window):
    window.update_idletasks()  # ウィンドウのサイズを更新する
    width = window.winfo_width()  # ウィンドウの幅を取得する
    height = window.winfo_height()  # ウィンドウの高さを取得する
    screen_width = window.winfo_screenwidth()  # 画面の幅を取得する
    screen_height = window.winfo_screenheight()  # 画面の高さを取得する
    x = (screen_width - width) // 2  # ウィンドウのX座標を計算する
    y = (screen_height - height) // 2  # ウィンドウのY座標を計算する
    window.geometry(f"{width}x{height}+{x}+{y}")  # ウィンドウの位置を設定する


root = tkinter.Tk()
root.title("Suumoから不動産情報をスクレイピング")
root.geometry("800x600")

center_window(root)

# 東京の地名を選択
label = tkinter.Label(root, text="東京都-市区郡を選択:", font=("Times New Roman", 16))
label.place(x=80, y=60)
locations = ['千代田区', '中央区', '港区', '新宿区', '文京区', '渋谷区', '台東区', '墨田区', '江東区', '荒川区', '足立区', '葛飾区', '江戸川区', '品川区', '目黒区', '大田区', '世田谷区', '中野区', '杉並区', '練馬区', '豊島区', '北区', '板橋区', '八王子市', '立川市', '武蔵野市', '三鷹市', '青梅市', '府中市', '昭島市', '調布市', '町田市', '小金井市', '小平市', '日野市', '東村山市', '国分寺市', '国立市', '福生市', '狛江市', '東大和市', '清瀬市', '東久留米市', '武蔵村山市', '多摩市', '稲城市', '羽村市', 'あきる野市', '西東京市', '西多摩郡']
location_box = tkinter.StringVar()
tokyo_locations = ttk.Combobox(root, width=27, textvariable=location_box, values=locations)
tokyo_locations.grid(column=1, row=5)
tokyo_locations.place(x=390, y=60)

# 築年数を選択
label = tkinter.Label(root, text="築年数:", font=("Times New Roman", 16))
label.place(x=80, y=90)
age_house = ["新築", "5年以内", "10年以内", "15年以内", "指定しない"]
age_box = tkinter.StringVar()
age = ttk.Combobox(root, width=27, textvariable=age_box, values=age_house)
age.grid(column=1, row=5)
age.place(x=390, y=90)

# 駅徒歩
label = tkinter.Label(root, text="駅徒歩:", font=("Times New Roman", 16))
label.place(x=80, y=120)
distance = ["1分以内", "5分以内", "10分以内", "15分以内", "指定しない"]
distance_box = tkinter.StringVar()
walk_distance = ttk.Combobox(root, width=27, textvariable=distance_box, values=distance)
walk_distance.grid(column=1, row=5)
walk_distance.place(x=390, y=120)

# 間取り
label = tkinter.Label(root, text="間取り:", font=("Times New Roman", 16))
label.place(x=80, y=150)
size_of_house = ["ワンルーム", "1K", "1DK", "1LDK", "2K", "2DK", "2LDK", "3K", "3DK", "3LDK"]
size_box = tkinter.StringVar()
size = ttk.Combobox(root, width=27, textvariable=size_box, values=size_of_house)
size.grid(column=1, row=5)
size.place(x=390, y=150)

# 家賃
label = tkinter.Label(root, text="家賃:", font=("Times New Roman", 16))
label.place(x=80, y=180)
min_rent_options = ['下限なし', '3万円以上', '3.5万円以上', '4万円以上', '4.5万円以上', '5万円以上', '5.5万円以上', '6万円以上', '6.5万円以上', '7万円以上', '7.5万円以上', '8万円以上', '8.5万円以上', '9万円以上', '9.5万円以上', '10万円以上', '10.5万円以上', '11万円以上', '11.5万円以上', '12万円以上', '12.5万円以上', '13万円以上', '13.5万円以上', '14万円以上', '14.5万円以上', '15万円以上', '15.5万円以上', '16万円以上', '16.5万円以上', '17万円以上', '17.5万円以上', '18万円以上', '18.5万円以上', '19万円以上', '19.5万円以上', '20万円以上', '21万円以上', '22万円以上', '23万円以上', '24万円以上', '25万円以上', '26万円以上', '27万円以上', '28万円以上', '29万円以上', '30万円以上', '35万円以上', '40万円以上', '50万円以上', '100万円以上', "指定なし"]
max_rent_options = ['上限なし', '3万円以下', '3.5万円以下', '4万円以下', '4.5万円以下', '5万円以下', '5.5万円以下', '6万円以下', '6.5万円以下', '7万円以下', '7.5万円以下', '8万円以下', '8.5万円以下', '9万円以下', '9.5万円以下', '10万円以下', '10.5万円以下', '11万円以下', '11.5万円以下', '12万円以下', '12.5万円以下', '13万円以下', '13.5万円以下', '14万円以下', '14.5万円以下', '15万円以下', '15.5万円以下', '16万円以下', '16.5万円以下', '17万円以下', '17.5万円以下', '18万円以下', '18.5万円以下', '19万円以下', '19.5万円以下', '20万円以下', '21万円以下', '22万円以下', '23万円以下', '24万円以下', '25万円以下', '26万円以下', '27万円以下', '28万円以下', '29万円以下', '30万円以下', '35万円以下', '40万円以下', '50万円以下', '100万円以下', "指定なし"]
min_rent_box = tkinter.StringVar()
max_rent_box = tkinter.StringVar()
min_rent = ttk.Combobox(root, width=12, textvariable=min_rent_box, values=min_rent_options)
max_rent = ttk.Combobox(root, width=12, textvariable=max_rent_box, values=max_rent_options)
min_rent.grid(column=1, row=5)
max_rent.grid(column=1, row=5)
min_rent.place(x=390, y=180)
max_rent.place(x=525, y=180)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)
separator.place(x=80, y=220, relwidth=0.8)

# 取得する物件数
label = tkinter.Label(root, text="取得する物件数", font=("Times New Roman", 16))
label.place(x=80, y=230)
number_of_houses = {"5件以下": 5, "10件以下": 10, "20件以内": 20, "30件以内": 30, "40件以内": 40, "50件以内": 50, "100件以内": 100}
items = list(number_of_houses.keys())
number_of_house_box = tkinter.StringVar()
number_house = ttk.Combobox(root, width=27, textvariable=number_of_house_box, values=items)
number_house.grid(column=1, row=5)
number_house.place(x=390, y=230)


button = tkinter.Button(root, text="開始", font=("Times New Roman", 24), command=lambda: scraping.scraping(location_box, age_box, distance_box, size_box, min_rent_box, max_rent_box, number_of_house_box))
button.place(x=350, y=470)

root.mainloop()
