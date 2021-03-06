import datetime

from my_service import connect_db


def query_analyze(user_data):
    print("load data for analyze ==> wait...")
    data_analyze = []

    normal_spend = 0
    essential_spend = 0
    transport_spend = 0
    online_spend = 0
    food_spend = 0
    normal_income = 0
    salary_income = 0

    income_sum = 0
    spend_sum = 0
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:
        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:
            income_sum = income_sum + data['income']
            spend_sum = spend_sum + data['spend']

            if data['type'] == "ค่าอาหาร":
                food_spend = food_spend + data['spend']
            elif data['type'] == "ค่าเดินทาง":
                transport_spend = transport_spend + data['spend']
            elif data['type'] == "ค่าใช้จ่ายทั่วไป":
                normal_spend = normal_spend + data['spend']
            elif data['type'] == "ค่าใช้จ่ายออนไลน์":
                online_spend = online_spend + data['spend']
            elif data['type'] == "ค่าใช้จ่ายของใช้ที่จำเป็น":
                essential_spend = essential_spend + data['spend']
            elif data['type'] == "รายรับทั่วไป":
                normal_income = normal_income + data['income']
            elif data['type'] == "รายรับเงินเดือน":
                salary_income = salary_income + data['income']

        print("load data for analyze ==> Calculate Percent...")
        if spend_sum == 0:
            normal_pt_spend = 0
            essential_pt_spend = 0
            transport_pt_spend = 0
            online_pt_spend = 0
            food_pt_spend = 0
        else:
            normal_pt_spend = round((normal_spend * 100) / spend_sum, 2)
            essential_pt_spend = round((essential_spend * 100) / spend_sum, 2)
            transport_pt_spend = round((transport_spend * 100) / spend_sum, 2)
            online_pt_spend = round((online_spend * 100) / spend_sum, 2)
            food_pt_spend = round((food_spend * 100) / spend_sum, 2)
            
        if income_sum == 0:
            normal_pt_income = 0
            salary_pt_income = 0
        else:
            normal_pt_income = (normal_income * 100) / income_sum
            salary_pt_income = (salary_income * 100) / income_sum

        print("Sum income ==> {} Bath.".format(income_sum))
        print("Sum spend ==> {} Bath.".format(spend_sum))
        print("Food spend ==> {} Bath. | {} %".format(food_spend, food_pt_spend))
        print("Transport spend ==> {} Bath. | {} %".format(transport_spend, transport_pt_spend))
        print("Normal spend ==> {} Bath. | {} %".format(normal_spend, normal_pt_spend))
        print("Online spend ==> {} Bath. | {} %".format(online_spend, online_pt_spend))
        print("Essentail spend ==> {} Bath. | {} %".format(essential_spend, essential_pt_spend))
        print("Normal spend ==> {} Bath. | {} %".format(normal_income, normal_pt_income))
        print("Salary spend ==> {} Bath. | {} %".format(salary_income, salary_pt_income))

        data_analyze = {'income_sum': income_sum,
                        'spend_sum': spend_sum,
                        'food_spend': food_spend,
                        'transport_spend': transport_spend,
                        'normal_spend': normal_spend,
                        'online_spend': online_spend,
                        'essential_spend': essential_spend,
                        'normal_income': normal_income,
                        'salary_income': salary_income,
                        'food_spend_pt': food_pt_spend,
                        'transport_spend_pt': transport_pt_spend,
                        'normal_spend_pt': normal_pt_spend,
                        'online_spend_pt': online_pt_spend,
                        'essential_spend_pt': essential_pt_spend,
                        'normal_income_pt': normal_pt_income,
                        'salary_income_pt': salary_pt_income
                        }
        print("load data for analyze ==> success")

    else:
        print("This user not have transaction.")
        normal_pt_spend = 0
        essential_pt_spend = 0
        transport_pt_spend = 0
        online_pt_spend = 0
        food_pt_spend = 0
        normal_pt_income = 0
        salary_pt_income = 0
        data_analyze = {'income_sum': income_sum,
                        'spend_sum': spend_sum,
                        'food_spend': food_spend,
                        'transport_spend': transport_spend,
                        'normal_spend': normal_spend,
                        'online_spend': online_spend,
                        'essential_spend': essential_spend,
                        'normal_income': normal_income,
                        'salary_income': salary_income,
                        'food_spend_pt': food_pt_spend,
                        'transport_spend_pt': transport_pt_spend,
                        'normal_spend_pt': normal_pt_spend,
                        'online_spend_pt': online_pt_spend,
                        'essential_spend_pt': essential_pt_spend,
                        'normal_income_pt': normal_pt_income,
                        'salary_income_pt': salary_pt_income
                        }
        print("load data for analyze ==> success")

    print("-"*30)
    return (data_analyze)


def findDataByDay(user_data, datestart, dateend):
    print("load data for analyze by Day ==> wait...")
    datestart_c = datetime.datetime.strptime(datestart, '%d-%b-%Y')
    dateend_c = datetime.datetime.strptime(dateend, '%d-%b-%Y')

    normal_spend = 0
    essential_spend = 0
    transport_spend = 0
    online_spend = 0
    food_spend = 0
    normal_income = 0
    salary_income = 0

    income_sum = 0
    spend_sum = 0
    db = connect_db.connectMongoDB()
    if db.transaction_list.count_documents({'username': user_data[1]}) > 0:

        get_data = db.transaction_list.find({'username': user_data[1]})

        for data in get_data:

            data_date_c = datetime.datetime.strptime(data['date'], '%d-%b-%Y')
            if datestart_c <= data_date_c <= dateend_c:
                income_sum = income_sum + data['income']
                spend_sum = spend_sum + data['spend']

                if data['type'] == "ค่าอาหาร":
                    food_spend = food_spend + data['spend']
                elif data['type'] == "ค่าเดินทาง":
                    transport_spend = transport_spend + data['spend']
                elif data['type'] == "ค่าใช้จ่ายทั่วไป":
                    normal_spend = normal_spend + data['spend']
                elif data['type'] == "ค่าใช้จ่ายออนไลน์":
                    online_spend = online_spend + data['spend']
                elif data['type'] == "ค่าใช้จ่ายของใช้ที่จำเป็น":
                    essential_spend = essential_spend + data['spend']
                elif data['type'] == "รายรับทั่วไป":
                    normal_income = normal_income + data['income']
                elif data['type'] == "รายรับเงินเดือน":
                    salary_income = salary_income + data['income']

        print("load data for analyze ==> Calculate Percent...")
        if spend_sum == 0:
            normal_pt_spend = 0
            essential_pt_spend = 0
            transport_pt_spend = 0
            online_pt_spend = 0
            food_pt_spend = 0
        else:
            normal_pt_spend = (normal_spend * 100) / spend_sum
            essential_pt_spend = (essential_spend * 100) / spend_sum
            transport_pt_spend = (transport_spend * 100) / spend_sum
            online_pt_spend = (online_spend * 100) / spend_sum
            food_pt_spend = (food_spend * 100) / spend_sum
        if income_sum == 0:
            normal_pt_income = 0
            salary_pt_income = 0
        else:
            normal_pt_income = (normal_income * 100) / income_sum
            salary_pt_income = (salary_income * 100) / income_sum

        print("Sum income ==> {} Bath.".format(income_sum))
        print("Sum spend ==> {} Bath.".format(spend_sum))
        print("Food spend ==> {} Bath. | {:.2f} %".format(food_spend, food_pt_spend))
        print("Transport spend ==> {} Bath. | {:.2f} %".format(transport_spend, transport_pt_spend))
        print("Normal spend ==> {} Bath. | {:.2f} %".format(normal_spend, normal_pt_spend))
        print("Online spend ==> {} Bath. | {:.2f} %".format(online_spend, online_pt_spend))
        print("Essentail spend ==> {} Bath. | {:.2f} %".format(essential_spend, essential_pt_spend))
        print("Normal spend ==> {} Bath. | {:.2f} %".format(normal_income, normal_pt_income))
        print("Salary spend ==> {} Bath. | {:.2f} %".format(salary_income, salary_pt_income))

        data_analyze = {'income_sum': income_sum,
                        'spend_sum': spend_sum,
                        'food_spend': food_spend,
                        'transport_spend': transport_spend,
                        'normal_spend': normal_spend,
                        'online_spend': online_spend,
                        'essential_spend': essential_spend,
                        'normal_income': normal_income,
                        'salary_income': salary_income,
                        'food_spend_pt': food_pt_spend,
                        'transport_spend_pt': transport_pt_spend,
                        'normal_spend_pt': normal_pt_spend,
                        'online_spend_pt': online_pt_spend,
                        'essential_spend_pt': essential_pt_spend,
                        'normal_income_pt': normal_pt_income,
                        'salary_income_pt': salary_pt_income
                        }
        print("load data for analyze ==> success")

    else:
        print("This user not have transaction.")
        normal_pt_spend = 0
        essential_pt_spend = 0
        transport_pt_spend = 0
        online_pt_spend = 0
        food_pt_spend = 0
        normal_pt_income = 0
        salary_pt_income = 0
        data_analyze = {'income_sum': income_sum,
                        'spend_sum': spend_sum,
                        'food_spend': food_spend,
                        'transport_spend': transport_spend,
                        'normal_spend': normal_spend,
                        'online_spend': online_spend,
                        'essential_spend': essential_spend,
                        'normal_income': normal_income,
                        'salary_income': salary_income,
                        'food_spend_pt': food_pt_spend,
                        'transport_spend_pt': transport_pt_spend,
                        'normal_spend_pt': normal_pt_spend,
                        'online_spend_pt': online_pt_spend,
                        'essential_spend_pt': essential_pt_spend,
                        'normal_income_pt': normal_pt_income,
                        'salary_income_pt': salary_pt_income
                        }
        print("load data for analyze ==> success")
    print("-" * 30)
    return (data_analyze)
