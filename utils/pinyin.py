from pypinyin import lazy_pinyin

def get_sim_pronunciation(char):
    pronunciation = lazy_pinyin(char)[0]
    if 'zh' in pronunciation or 'ch' in pronunciation or 'sh' in pronunciation or 'ng' in pronunciation:
        pronunciation = pronunciation.replace('zh', 'z').replace('ch', 'c').replace('sh', 's').replace('ng', 'n')
    return pronunciation