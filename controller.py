from view import menu, show_contacts, print_message, input_contact, input_return
from model import *
from view import text

path = r'D:\Python\PB_console\phones.txt'
book = PhoneBook(path)
def start():
    while True:
        choice = menu()
        match choice:
            # Показать все контакты
            case 1:
                show_contacts(text.hander, book.phone_book)

            # Поиск контакта
            case 2:
                word = input_return(text.search_word)
                show_contacts(text.hander, book.search_contact(word))

            # Создать контакт
            case 3:
                max_id = 0
                for contact in book.phone_book:
                    if contact['id'] > str(max_id):
                        max_id = int(max(contact['id']))
                print(max_id)
                data = input_contact(text.new_contact)
                new_contact = Contact(data['name'], data['phone'], data['comment'], max_id + 1)
                book.add_contact(new_contact.contact)
                print_message(text.contact_creat(new_contact.contact['name']))

            # Удалить контакт
            case 4: 
                id_contact = int(input_return(text.delete_id_contact))
                book.delet_contact(id_contact)
                print_message(text.del_contact)

            # Изменить контакт
            case 5: 
                id_contact = int(input_return(text.delete_id_contact))
                new = input_contact(text.input_new_contact)
                book.change_contact(id_contact, new)
                print_message(text.contact_saved(new.get('name')))

            # Сохранить справочник
            case 6: 
                book.save_phone_book()
                print_message(text.save_phone_book)

            # Закрыть справочник
            case 7: 
                break
