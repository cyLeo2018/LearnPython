def get_formated_name(first_name, last_name):
    '''
    返回完整姓名
    :param first_name:
    :param last_name:
    :return:
    '''
    return {1:first_name.title(),2:last_name.title()} #返回字典

while True:
    f_name = input("(Press 'q' or 'Q' to quit!)\nPlease input your first name:")
    if f_name == 'q' or f_name == 'Q':
        break
    l_name = input("Please input your last name:")
    if l_name == 'q' or l_name == 'Q':
        break
    print('Hi! {0}'.format(get_formated_name(f_name,l_name)))