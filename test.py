from correct import Corrector

correction = Corrector()

text = "這場演唱會一票難求，開賣兩個小時既售磬，只剩後補的機會"
print(correction.correct_with_bert(text))
