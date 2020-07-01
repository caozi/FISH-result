import pandas as pd
import json

def update():
    df = pd.read_excel("Book1.xls")
    update_data = {}
    for i in df.index.values:
        id = '病检号:' + df.iloc[i]['病检号'] + '\n'
        name = df.iloc[i]['姓名']
        age = '年龄:' + str(df.iloc[i]['年龄']) + '\n'
        gender = '性别:' + df.iloc[i]['性别'] + '\n'
        hospital_number = str(df.iloc[i]['住院号']) + '\n'
        pathology_number = str(df.iloc[i]['病理号']) + '\n'
        test_item = df.iloc[i]['探针名称'] + '\n'
        if df.iloc[i]['结果'] == 0:
            test_result = '(-)\n'
        else:
            test_result = '(+)\n'

        if not name in update_data:
            if hospital_number.startswith('H'):
                update_data[
                    name] = id + '姓名:' + name + '\n' + age + gender + '病理号:' + hospital_number + '原病理号:' + pathology_number + test_item + test_result
            else:
                update_data[
                    name] = id + '姓名:' + name + '\n' + age + gender + '住院号:' + hospital_number + '病理号:' + pathology_number + test_item + test_result
        else:
            if hospital_number.startswith('H'):
                update_data[
                    name] += test_item + test_result
            else:
                update_data[
                    name] += test_item + test_result

    f = open("patients_data.json", "w")
    f.write(json.dumps(update_data))
    f.close()


if __name__ == '__main__':
    update()


