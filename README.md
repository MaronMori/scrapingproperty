# scrapingproperty
English:
I created my first piece of work in python and posted it to Github for the first time.
This tool utilizes scraping technology to export information from Suumo, a real estate information site, to csv for properties with specific criteria.
The directories used are selenium, pandas, and tkinter.
The difficulty was that when scraping certain elements in a while statement, if the number of properties is less than or equal to the specified number, it goes to the next page of Suuumo, but every time it does so, it throws an error saying that the element already retrieved is out of date and cannot be used.
The solution was to repeat the while statement each time I went to the next page, but I fixed the problem by modifying the data frame to include the retrieved element in the data frame each time I went to a page.

----------
Japanese:
pythonで初めての作品を作り、初めてGithubに投稿ました。
スクレイピング技術を活用して、不動産情報サイトのSuumoから特定の条件の物件をcsvに情報を書き出すツールです。
使ったディレクトリーはselenium, pandas, tkinterです。
苦労した点はwhile文の中で特定の要素をスクレイピングするときに、指定した物件数以下ならSuumoの次のページに行くのですがその度にすでに取得した要素が古いため使用できません、とエラーが出たことです。
解決策としてページ移動するごとにwhile文が繰り返されるのですが、ページごとにデータフレームに取得した要素を入れるように改良したら直りました。

