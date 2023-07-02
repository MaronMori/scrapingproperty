# scrapingproperty
This is a project that corrects much data from Japanese property website.
pythonで初めての作品を作り、初めてGithubに投稿ました。
スクレイピング技術を活用して、不動産情報サイトのSuumoから特定の条件の物件をcsvに情報を書き出すツールです。
使ったディレクトリーはselenium, pandas, tkinterです。
苦労した点はwhile文の中で特定の要素をスクレイピングするときに、指定した物件数以下ならSuumoの次のページに行くのですがその度にすでに取得した要素が古いため使用できません、とエラーが出たことです。
解決策としてページ移動するごとにwhile文が繰り返されるのですが、ページごとにデータフレームに取得した要素を入れるように改良したら直りました。

