from correct import Corrector

correction = Corrector()

text = "改革開放以來，中國農村發生了天翻地復的變化"
print(correction.correct_with_bert(text))