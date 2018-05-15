#まずリストを二つ使える時の解答
a = ['a', 'a', 'b', 'b', 'c']
b = []
for i in a:
    if not i in b: #if notでiがbにないことを確認する
        b.append(i) #appendはリストに追加する
print(b)


#次にリストが一つの時の解答
a = ['a', 'a', 'b', 'b', 'c']
for i, j in enumerate(a): #enumerateでindexを用いる
   if j in a[i+1:]: #スライスしてi+1以降に現れないことを確認
        a.remove(j) #removeで削除
print(a)
