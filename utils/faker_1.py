from faker import Faker

faker = Faker('zh_CN')
#
# for i in range(5):
#     print('姓名', faker.name())
#     print('身份证号码：', faker.ssn())
#     print('手机号：', faker.phone_number())
#     print(faker.lexify(text='车牌：?', letters='冀晋豫鲁京')+faker.bothify(text='?#####', letters='ABCDE'))

def fake_data():
    fake_res = {
        'name': faker.name(),
        'ssn': faker.ssn(),
        'phone_number': faker.phone_number(),
        'plate_number': faker.lexify(text='?', letters='冀晋豫鲁京') + faker.bothify(text='?#####', letters='ABCDE')
    }
    return fake_res
for i in range(5):
    print(fake_data())