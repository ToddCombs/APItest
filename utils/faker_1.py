from faker import Faker

faker = Faker('zh_CN')

for i in range(5):
    print('姓名', faker.name())
    print('身份证号码：', faker.ssn())
    print('手机号：', faker.phone_number())