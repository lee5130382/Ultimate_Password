import random
import playsound

def game(ans=None, range_inti=0, range_end=100, seed=123):
    print('這是一個遊戲，叫做終極密碼，來挑戰吧! \n')
    if ans is None:
        if seed is None:
            ans = random.randint(range_inti, range_end)
        else:    
            random.seed(seed)
            ans = random.randint(range_inti, range_end)

    while True:
        try: 
            guess = int(input(f"請在 {range_inti} 到 {range_end} 中猜猜一個數字: \n"))
            if not(range_inti <= guess <= range_end):
                print('建議您念個數學系，人生會更好 \n')
            elif guess == ans:
                print('################')
                print('你真聰明!答對了!')
                print('################')
                break 
            elif guess < ans:
                print('*** 你沒猜中 哈哈哈哈 *** \n')
                range_inti = guess
            else:
                print('*** 你沒猜中 哈哈哈哈 *** \n')
                range_end = guess                
        except ValueError:
            print('*** 請輸入數字!很難嘛...  \n')
        
if __name__ == '__main__':
    game()   



# 在command line寫下方指令即可將程式轉換為exe檔
# pyinstaller --onefile Ultimate_password.py




