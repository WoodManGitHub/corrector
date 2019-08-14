from pypinyin import lazy_pinyin

def get_chinese_char():
    return set(list(open('./data/chinese_5039.txt', 'r', encoding='utf-8').read().strip()))

def get_sim_pronunciation(char):
    pronunciation = lazy_pinyin(char)[0]
    if 'zh' in pronunciation or 'ch' in pronunciation or 'sh' in pronunciation or 'ng' in pronunciation:
        pronunciation = pronunciation.replace('zh', 'z').replace('ch', 'c').replace('sh', 's').replace('ng', 'n')
    return pronunciation