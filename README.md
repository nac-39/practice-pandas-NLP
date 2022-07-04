# pandasとMecabを使って遊ぼう

ゼミでの発表資料として作りました．

pandasの基本操作を触ってみることが目的です．ただ触ってるだけでも面白くないと思うので，最終的にネガポジ辞書を使ってなんちゃって自然言語処理をしようというのが最終目的です．

以下の参考記事は自分のメモです．
# 参考記事
https://qiita.com/y_itoh/items/4693bd8f64ac811f8524
https://www.teamxeppet.com/python-mecab-unidic-lite_mac/

- ネガポジ辞書
https://www.cl.ecei.tohoku.ac.jp/Open_Resources-Japanese_Sentiment_Polarity_Dictionary.html

- pandasで任意の位置の値を取得・変更するat, iat, loc, iloc
https://note.nkmk.me/python-pandas-at-iat-loc-iloc/

- MecabのTagger
https://qiita.com/Haruka-Ogawa/items/c2116f0eb5c859955d63

- Mecabのipa辞書のmacに入れる方法
[Python3からMeCabを使う - Qiita](https://qiita.com/taroc/items/b9afd914432da08dafc8)

- Mecabのデフォルト辞書について（Mac）
https://qiita.com/shimajiroxyz/items/e488e9b28a56e908e7cb

- pos-id一覧を見る（M1Mac with homebrew)
```iconv -f euc-jp -t utf-8 /opt/homebrew/Cellar/mecab-ipadic/2.7.0-20070801/lib/mecab/dic/ipadic/pos-id.def```

- 結果

```text
その他,間投,*,* 0
フィラー,*,*,* 1
感動詞,*,*,* 2
記号,アルファベット,*,* 3
記号,一般,*,* 4
記号,括弧開,*,* 5
記号,括弧閉,*,* 6
記号,句点,*,* 7
記号,空白,*,* 8
記号,読点,*,* 9
形容詞,自立,*,* 10
形容詞,接尾,*,* 11
形容詞,非自立,*,* 12
助詞,格助詞,一般,* 13
助詞,格助詞,引用,* 14
助詞,格助詞,連語,* 15
助詞,係助詞,*,* 16
助詞,終助詞,*,* 17
助詞,接続助詞,*,* 18
助詞,特殊,*,* 19
助詞,副詞化,*,* 20
助詞,副助詞,*,* 21
助詞,副助詞／並立助詞／終助詞,*,* 22
助詞,並立助詞,*,* 23
助詞,連体化,*,* 24
助動詞,*,*,* 25
接続詞,*,*,* 26
接頭詞,形容詞接続,*,* 27
接頭詞,数接続,*,* 28
接頭詞,動詞接続,*,* 29
接頭詞,名詞接続,*,* 30
動詞,自立,*,* 31
動詞,接尾,*,* 32
動詞,非自立,*,* 33
副詞,一般,*,* 34
副詞,助詞類接続,*,* 35
名詞,サ変接続,*,* 36
名詞,ナイ形容詞語幹,*,* 37
名詞,一般,*,* 38
名詞,引用文字列,*,* 39
名詞,形容動詞語幹,*,* 40
名詞,固有名詞,一般,* 41
名詞,固有名詞,人名,一般 42
名詞,固有名詞,人名,姓 43
名詞,固有名詞,人名,名 44
名詞,固有名詞,組織,* 45
名詞,固有名詞,地域,一般 46
名詞,固有名詞,地域,国 47
名詞,数,*,* 48
名詞,接続詞的,*,* 49
名詞,接尾,サ変接続,* 50
名詞,接尾,一般,* 51
名詞,接尾,形容動詞語幹,* 52
名詞,接尾,助数詞,* 53
名詞,接尾,助動詞語幹,* 54
名詞,接尾,人名,* 55
名詞,接尾,地域,* 56
名詞,接尾,特殊,* 57
名詞,接尾,副詞可能,* 58
名詞,代名詞,一般,* 59
名詞,代名詞,縮約,* 60
名詞,動詞非自立的,*,* 61
名詞,特殊,助動詞語幹,* 62
名詞,非自立,一般,* 63
名詞,非自立,形容動詞語幹,* 64
名詞,非自立,助動詞語幹,* 65
名詞,非自立,副詞可能,* 66
名詞,副詞可能,*,* 67
連体詞,*,*,* 68
```

- 品詞体系の意味
https://miner.hatenablog.com/entry/323

- pandas公式チートシート
https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

- pandas, dataframeの基礎
https://note.nkmk.me/python-pandas-dataframe-values-columns-index/

- 行の追加方法
https://note.nkmk.me/python-pandas-assign-append/
`df.append`はdeprecatedらしい
→https://max999blog.com/pandas-add-row-to-dataframe/
dataframe同士じゃないとうまくconcatできないらしい