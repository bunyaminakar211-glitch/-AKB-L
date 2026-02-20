import json
import os

BANK_NAME = "BPTR"
DATA_FILE = "bptr_accounts.json"

# Veri dosyası yoksa oluştur
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_accounts():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

def create_account():
    accounts = load_accounts()
    username = input("Kullanıcı adı: ")

    if username in accounts:
        print("❌ Bu kullanıcı zaten var.")
        return

    password = input("Şifre: ")
    accounts[username] = {
        "password": password,
        "balance": 0.0
    }

    save_accounts(accounts)
    print("✅ Hesap oluşturuldu!")

def login():
    accounts = load_accounts()
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    if username in accounts and accounts[username]["password"] == password:
        print(f"\n🏦 {BANK_NAME} Bankasına Hoş Geldin {username}!")
        user_menu(username)
    else:
        print("❌ Hatalı giriş.")

def user_menu(username):
    while True:
        print("\n1- Bakiye Görüntüle")
        print("2- Para Yatır")
        print("3- Para Çek")
        print("4- Transfer Yap")
        print("5- Çıkış")

        choice = input("Seçim: ")
        accounts = load_accounts()

        if choice == "1":
            print(f"💰 Bakiyen: {accounts[username]['balance']} TL")

        elif choice == "2":
            amount = float(input("Yatırılacak miktar: "))
            accounts[username]["balance"] += amount
            save_accounts(accounts)
            print("✅ Para yatırıldı.")

        elif choice == "3":
            amount = float(input("Çekilecek miktar: "))
            if amount <= accounts[username]["balance"]:
                accounts[username]["balance"] -= amount
                save_accounts(accounts)
                print("✅ Para çekildi.")
            else:
                print("❌ Yetersiz bakiye.")

        elif choice == "4":
            target = input("Gönderilecek kullanıcı adı: ")
            amount = float(input("Miktar: "))

            if target in accounts and amount <= accounts[username]["balance"]:
                accounts[username]["balance"] -= amount
                accounts[target]["balance"] += amount
                save_accounts(accounts)
                print("✅ Transfer başarılı.")
            else:
                print("❌ Transfer başarısız.")

        elif choice == "5":
            break

        else:
            print("❌ Geçersiz seçim.")

def main():
    while True:
        print(f"\n🏦 {BANK_NAME} Banka Sistemi")
        print("1- Hesap Oluştur")
        print("2- Giriş Yap")
        print("3- Çıkış")

        choice = input("Seçim: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
