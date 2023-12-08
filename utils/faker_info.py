from faker import Faker

faker = Faker('zh_CN')


def fake_data():
    '''
    fake信息获取接口
    :return:
    '''
    letters_cn = '藏川鄂甘赣贵桂黑沪吉冀津晋京辽鲁蒙闽宁青琼陕苏皖湘新渝豫粤云浙'
    letters_num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fake_res = {
        'name': faker.name(),
        'ssn': faker.ssn(),
        'phone_number': faker.phone_number(),
        'plate_number': faker.lexify(text='?', letters=letters_cn) + faker.bothify(text='?#####', letters=letters_num)
    }
    return fake_res


for i in range(30):
    print(fake_data())
