def yb_operate(key):
    """yb字体"""
    yb_dict = {'A': '/A/', 'B': '/B/', 'C': '/C/', 'D': '/D/', 'E': '/E/', 'F': '/F/', 'G': '/G/', 'H': '/H/', 'I': '/I/', 'O': '/O/', 'S': '/S/', 'V': '/V/', 'W': '/W/', 'X': '/X/', 'Y': '/Y/', 'Z': '/Z/', 'EW': '/?/'}
    print(key.upper())
    if key.upper() in yb_dict.keys():
        value = yb_dict[key.upper()]
        print('value:', value)
        return value

def yb_guess(key):
    #猜拳游戏无声音
    yb_dict = {'/A/':"a",'/B/':"b",'/C/':"c",'/D/':"d",'/E/':"e",'/F/':'f','/G/':'g', '/H/':'h','/I/':'i','/O/':'o','/S/':'s','/V/':'v','/W/':"w",'/X/':'x','/Y/':'y','/Z/':'z'}
    print(key)
    if key in yb_dict.keys():
        value = yb_dict[key]
        print('value:', value)
        return value


def yb_letter(key):
    """yb字体"""

    yb_dict = {'/ɑ/':'a', '/ɜ/':'b', '/ɔ/': 'c', '/ð/': 'd' , '/ə/': 'e' , '/ɒ/': 'f' , '/g/': 'g' , '/ʊ/': 'h' ,
               '/ɪ/': 'i' , '/θ/': 'o', '/ʃ/': 's', '/ʌ/': 'v', '/ʒ/': 'w', '/ɛ/': 'x', '/ŋ/': 'y', '/æ/': 'z',
               '/ˈ/': 'e'}
    if key in yb_dict.keys():
        value = yb_dict[key]
        print(("value",value))
        return value

def yb_letter_write(key):
    """yb字体"""

    yb_dict = {'/ɑ/':'a', '/ɜ/':'b', '/ɔ/': 'c', '/ð/': 'd' , '/ə/': 'e' , '/ɒ/': 'f' , '/g/': 'g' , '/ʊ/': 'h' ,
               '/ɪ/': 'i' , '/θ/': 'o', '/ʃ/': 's', '/ʌ/': 'v', '/ʒ/': 'w', '/ɛ/': 'x', '/ŋ/': 'y', '/æ/': 'z',
               '/ˈ/': "ew"}
    if key in yb_dict.keys():
        value = yb_dict[key]
        print(("value",value))
        return value
def yb_letter_select(key):
    """yb字体"""

    yb_dict = {'/ɑ/':'a', '/ɜ/':'b', '/ɔ/': 'C', '/ð/': 'd' , '/ə/': 'e' , '/ɒ/': 'f' , '/g/': 'g' , '/ʊ/': 'h' ,
               '/ɪ/': 'i' , '/θ/': 'o', '/ʃ/': 's', '/ʌ/': 'v', '/ʒ/': 'w', '/ɛ/': 'x', '/ŋ/': 'y', '/æ/': 'z',
               '/ˈ/': "ew"}
    if key in yb_dict.keys():
        value = yb_dict[key]
        print(("value",value))
        return value

