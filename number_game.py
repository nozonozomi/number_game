import random

answer = random.randint(100, 999)

print("数字当てゲーム！！")
print("100から999までの数字を当ててください")

guess = int(input("数字を入力してください: "))

if guess == answer:
    print("正解です！")
else:
    print("不正解です")

    if guess < answer:
        print("もっと大きい数字です。")
    else:
        print("もっと小さい数字です。")
        
    print(f"正解は {answer} でした。")