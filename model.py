phone_book = []
path = 'PB_console\phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in str(value).lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field

def save_contact(book: list[dict[str, str]]):
    new_book = []
    for  contact in range(len(book)):
        line = book[contact]
        uid = str(line.get('id'))
        name = str(line.get('name'))
        phone = str(line.get('phone'))
        comment = str(line.get('comment'))
        new_book.append(uid + ':' + name + ':' + phone + ':' + comment)                
    with open(path, 'w', encoding='UTF-8') as file:
        for contact in new_book:
            file.write(str(contact) + '\n')

def delet_contact(book: list[dict[str, str]], id_contact: int):
    del book[id_contact - 1]
    while id_contact <= len(book):
        book[id_contact - 1]['id'] = id_contact
        id_contact += 1 
            