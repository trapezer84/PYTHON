"""
연락처 등록
연락처 조회
연락처 삭제
연락처 업데이트
"""

import pickle


def regist_contact(contact) :
    # 저장된 dic 을 불러온다 (복원)
    f = open("contact.dat", "rb")
    contacts = pickle.load(f)
    # dic에 추가
    contacts.append(contact)

    # wb : write binary
    with open("contact.dat", "wb") as f :
        # ket : name
        # pickle로 저장하기
        pickle.dump(contacts, f)


def view_all_contact () :
    """
    저장된 컨텍트를 불러오는 메소드
    :return:
    """
    f = open("contact.dat", "rb")
    return pickle.load(f)

def remove_contact(name) :
    """
    컨텐트 삭제하기
    :param name:
    :return:
    """
    pass

def update_contact(name) :
    """
    컨텍트 업데이트
    :param name:
    :return:
    """
    pass
