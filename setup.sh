#! /bin/zsh

# mecabをインストール
brew install mecab
brew install mecab-ipa

# 感情極性辞書をダウンロード
curl http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/pn.csv.m3.120408.trim > pn.csv.m3.120408.trim
curl http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/wago.121808.pn > wago.csv.m3.120408.trim
