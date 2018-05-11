
def vob_operate(key):
    """vob的正确的字典"""
    vob_dict = {"Apple":"苹果（首字母大写,自定义去除最后一个字母）","Hello":"你好（首字母大写,自定义去除最后一个字母）","like":"喜欢（自定义去除最后一个字母）","over":"结束（自定义去除最后一个字母）","but":'但是（自定义去除最后一个字母）',"like is":"词组"}
    value = vob_dict[key]
    print(value)
    return value

def vob_operate_word(key):
    vob_dict = {"苹果（首字母大写,自定义去除最后一个字母）":"Apple","你好（首字母大写,自定义去除最后一个字母）":"Hello","喜欢（自定义去除最后一个字母）":"like","结束（自定义去除最后一个字母）":"over",'但是（自定义去除最后一个字母）':"but","词组":"like is"}
    value = vob_dict[key]
    print(value)
    return value

def reconstruction_guess(key):
    '''猜词游戏正确的字典'''
    guess_dict = {"苹果（首字母大写,自定义去除最后一个字母）":"Apple","你好（首字母大写,自定义去除最后一个字母）":"Hello","喜欢（自定义去除最后一个字母）":"like","结束（自定义去除最后一个字母）":"over",'但是（自定义去除最后一个字母）':"but","词组":"like is"}
    value = guess_dict[key]
    value_guess= value.lower()
    return value_guess


def reconstruction_write(key):
    '''默写正确的字典'''
    guess_dict = {"苹果（首字母大写，自定义去除最后一个字母）":"Apple","你好（首字母大写，自定义去除最后一个字母）":"Hello","喜欢（自定义去除最后一个字母）":"like","结束（自定义去除最后一个字母）":"over","但是（自定义去除最后一个字母）":"but","词组":"like is"}
    value = guess_dict[key]
    value_guess= value.lower()
    print(value_guess)
    return value_guess

def reconstruction_self(key):
    '''默写正确的字典'''
    guess_dict = {"苹果（首字母大写，自定义去除最后一个字母）":"e","你好（首字母大写，自定义去除最后一个字母）":"o","喜欢（自定义去除最后一个字母）":"e","结束（自定义去除最后一个字母）":"r","但是（自定义去除最后一个字母）":"t","词组":"s"}
    value = guess_dict[key]
    value_guess= value.lower()
    print(value_guess)
    return value_guess