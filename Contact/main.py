"""


"""

from contact import Contact
import contact_service

c = Contact("lee", "lee@naver.com", '010-1231-1232', 'seoul')
contact_service.regist_contact(c)

# contact 주소 전체보기
contacts = contact_service.view_all_contact()

for contact in contacts  :
    print(contact.name, contact.email, contact.phone_number, contact.address)



