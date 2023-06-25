class PhoneBook:
   
    def __init__(self, path: str) -> None:
        self.phone_book = []
        self.path = path
        self.open_phone_book()

    # Открытие файла
    def open_phone_book(self) -> None:
        with open(self.path, 'r', encoding = 'UTF=8') as file:
            data = file.readlines()
        for contact in data:
            user_id, name, phone, comment, *_ = contact.strip().split(':')
            self.phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})
   
    # Сохранение файла
    def save_phone_book(self) -> None:
        with open(self.path, 'w', encoding = 'UTF=8') as file:
            for contact in range(len(self.phone_book)):
                line = self.phone_book[contact]
                uid = str(line.get('id'))
                name = str(line.get('name'))
                phone = str(line.get('phone'))
                comment = str(line.get('comment'))
                file.write(f'{uid}:{name}:{phone}:{comment}' + '\n')

    # Добавление контакта
    def add_contact(self, contact: dict) -> None:
        self.phone_book.append(contact)
    
    # Удаление контакта
    def delet_contact(self, id_contact: int) -> None:
        for index_contact in range(len(self.phone_book)):
            if self.phone_book[index_contact].get('id') == str(id_contact):
                self.phone_book.pop(index_contact)
                break
    
    # Изменение контакта
    def change_contact(self, id_contact: int, new_data: dict) -> None:
        for index_contact in range(len(self.phone_book)):
            if self.phone_book[index_contact].get('id') == str(id_contact):
                self.phone_book[index_contact].update(new_data)
                break
    
    # Поисск контакта
    def search_contact(self, word: str) -> list[dict]:
        result = []
        for contact in self.phone_book:
            for value in contact.values():
                if word.lower() in value.lower():
                    result.append(contact)
                    break
        return result
    
class Contact:
    def __init__(self, name: str, phone: str, comment: str, id: int) -> None:
        self.contact = {'id':str(id), 'name':name, 'phone':phone, 'comment':comment} 
