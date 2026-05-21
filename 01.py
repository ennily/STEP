#単語のsort
def sort_word(word):
    n = 1
    for i in range (len(word)-1):
        if word[i] > word[i+1]:
            word[i], word[i+1] = word[i+1], word[i] #i文字目とi+1文字目を入れ替える方法がわからない。
            while n < i:
                if word[i-(n+1)] > word[i-n]:
                    word[i-(n+1)], word[i-n] = word[i-n], word[i-(n+1)]
                    n += 1
                else:
                    n += 1
        else:
            pass
    return word

#辞書のsort
def sort_dict():


#新しい辞書を作る
new_dict = [] #sortされた単語だけの辞書
true_dict = {} #sortされた単語：元の単語の辞書型辞書
with open("words.txt", "r") as file: #調べてしまった。with ~~ as fileで自動でcloseしてくれる。
    for line in file:
        new_dict.append(sort_word(line))
        true_dict[sort_word(line)] = line
    new_dict = sort_dict(new_dict)

#二分探索で探す
def search(keyword):
    sorted_keyword = sort_word(keyword)
    search_from = new_dict

    while search_from > 1:
        #中央値を出す
        if len(search_from) % 2 == 1:
            mid_num = (len(search_from)+1) / 2
        else:
            mid_num = len(search_from) / 2
        #範囲を狭めてく
        if sorted_keyword < search_from[mid_num]:
            search_from = search_from[0:(mid_num-1)]
        else:
            search_from = search_from[mid_num:-1]
    
    return true_dict[search_from[0]] #同じsortされた単語から複数の単語を復活させれちゃう可能性がある。dictだからバグる？


if __name__ == "__main__":
    keyword = input("Enter the keyword:")
    answer = search(keyword)
    if answer:
        print(answer)
    else:
        print ("Couldn't find anything.")