from clases import User, Wishes
import db

def main():
    print("Welcome to wish service !!!")
    while True:
        action = input("Выберите действие:\n"
                       "1. Оставить пожелание \n"
                       "2. Проверить пожелание \n"
                       "3. Выход \n")

        if action == "1":
            try:
                phone = input("Введите свой номер:\n")
                text = input("Введите текст пожелания: \n")
                recipient = input("Введите номер получателя: \n")

                if len(phone.strip()) > 0 and len(text.strip()) > 0 and len(recipient.strip()) > 0:
                    try:
                        user = User(phone=phone)
                        db.inserting_user(user, recipient)
                        wish = Wishes(text=text, sender_id =db.find_sender_id(phone), recipient_id =db.find_recipient_id(recipient))
                        db.inserting_wish(wish)
                    except:
                        print("У вас закончились попытки!")
                    finally:
                        print("Ваше желание отправленно успешно!")


                else:
                     print("Error!")

            except Exception as ex:
                print(ex)

            finally:
                pass
        elif action == "2":
            phone = input("Введите номер для проверки почты: \n")
            phone = db.find_phone(phone)
            if db.check_box(phone) > 0:
                db.show_text(phone)
            else:
                print("К сожалению вам ещё не отправляли пожелание!")

        elif action == "3":
            print("До скорой встречи :)")
            db.close_conn()
            break
        else:
            print("Error!\n")
main()
