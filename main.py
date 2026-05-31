import json
import os

FILE_NAME = "data.json"

# 讀取資料
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"income": [], "expense": []}

# 存資料
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    data = load_data()

    while True:
        print("\n====================")
        print("1. 新增收入")
        print("2. 新增支出")
        print("3. 查看結算")
        print("4. 離開")
        print("====================")

        choice = input("請選擇：")

        if choice == "1":
            amount = int(input("輸入收入："))
            data["income"].append(amount)
            save_data(data)
            print("✔ 已新增收入")

        elif choice == "2":
            amount = int(input("輸入支出："))
            data["expense"].append(amount)
            save_data(data)
            print("✔ 已新增支出")

        elif choice == "3":
            total_income = sum(data["income"])
            total_expense = sum(data["expense"])
            print("\n📊 結算結果")
            print("總收入：", total_income)
            print("總支出：", total_expense)
            print("結餘：", total_income - total_expense)

        elif choice == "4":
            print("👋 結束程式")
            break

        else:
            print("⚠ 請輸入 1~4")

if __name__ == "__main__":
    main()
