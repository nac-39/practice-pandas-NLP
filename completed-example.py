import pandas as pd
import MeCab
# pandas
# カラム名と値の位置ずれを制御
pd.set_option('display.unicode.east_asian_width', True)

# csvを読み込んでDataFrameにする
# 区切り文字が\tなのでread_tableメソッドを使う（カンマならread_csv）
noun_df = pd.read_table('pn.csv.m3.120408.trim', names=(
    "word", "emotion", "polarity", "sb/ob"))
verb_df = pd.read_table('wago.121808.pn', names=("emotion", "word"))
# 頭と尻の５行見る
print(noun_df.head())
print(noun_df.tail())

# 感情の内訳を確認
print(noun_df["emotion"].value_counts())
# 感情のうち、p/e/nの項目のみを抽出
noun_df = noun_df[(noun_df["emotion"] == 'p') | (
    noun_df["emotion"] == 'e') | (noun_df["emotion"] == 'n')]

# ネガポジ辞書を見てみよう
# 辞書配列みたいにデータを取り出せる
print(noun_df[["word", "emotion"]]) 

# ilocメソッド
# 複数の要素の値を選択する
print(noun_df.iloc[10:20:2, 2])  # スライス記法で取り出せる

# locメソッド
# 行や列の名前で情報を取り出せる
print(noun_df.loc[:, "word"])  # 列名で取り出す

# データの書き換え
# https://note.nkmk.me/python-pandas-replace/
# 用言のemotionをネガとポジだけにする
verb_df["emotion"] = verb_df["emotion"].str.replace(r"\（.*\）", "", regex=True)
verb_df["word"] = verb_df["word"].str.replace(" ", "")

# いらない列を消す
# https://note.nkmk.me/python-pandas-drop/#dataframe_1
noun_df.drop(columns="sb/ob", inplace=True)
noun_df.drop(columns="polarity", inplace=True)


print(noun_df.head())
print(verb_df.head())


################################################################
# Mecab
################################################################
def generate_lyric_df(lyric_txt_path: str) -> pd.DataFrame:
    tagger = MeCab.Tagger()
    
    try:
        with open(lyric_txt_path, "r") as f:
            node = tagger.parseToNode(f.read())
    except Exception as e:
        print(e)
    
    col_names = ["word", "basic_form", "pos", "emotion"]
    df = pd.DataFrame(columns=col_names)
    print(df)
    while node:
        # 単語、品詞、詳細情報をタブ区切りで表示
        t = node.feature.split(",")
        if t[0] in ("名詞", "動詞", "副詞", "形容詞"):
            pos = t[0]
            basic_form = t[7]
            row = pd.DataFrame([[node.surface, basic_form, pos, None]], columns=col_names)
            # row = pd.Series([node.surface, basic_form, pos, None]) # これはうまくいかないからDFを使う
            df = pd.concat([df, row], ignore_index=True) # axis=0 == axis='index', 1=>columns
        # 次の要素を取得
        node = node.next
    print(df)
    return df


##################################
# ネガポジ分析
##################################
lyric_df = generate_lyric_df("./lyrics/アイデア.txt")

def fill_emotion(lyric_df: pd.DataFrame) -> pd.DataFrame:
    for index, word, basic_form, pos, emotion in lyric_df.itertuples():
        if pos == "名詞":
            emotion = noun_df.loc[noun_df["word"] == word]
        elif pos == "動詞":
            emotion = verb_df.loc[verb_df["word"] == word]
        if not (emotion is None):
            if not(emotion.empty):
                # 値を代入するときは代入先を一つに指定しないといけない
                lyric_df.iloc[index, 3]= emotion.iat[0,1]
    return lyric_df

lyric_df = fill_emotion(lyric_df)
print(lyric_df)


print(lyric_df.groupby("emotion").count())