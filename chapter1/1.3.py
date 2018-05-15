a = 'Mr John Smith'
for i in a:
    if i == ' ': #空欄かを確認
        i = '%20' #空欄を変換
    print(i, end="") #printの出力を通常ではないやり方で出力
print() #出力後に改行するため
