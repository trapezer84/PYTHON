"""
    create : 2016. 06. 29
    author : Leina

"""

def rental_car_cost(days, fee_a_day=40):
    """
    렌트카 대여 비용 계산
    :param days: 대여일
    :param fee_a_day: 하루 다여일
    :return: 최종 가격
    """
    total = days * fee_a_day
    if days >= 7 :
        return total - 50
    elif days >=3 :
        return total - 20
    else :
        return total



