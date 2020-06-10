import torch
from transformers import BertTokenizer, BertForMaskedLM

from utils.pinyin import get_sim_pronunciation

class Corrector():
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
        self.model = BertForMaskedLM.from_pretrained('bert-base-chinese')
        self.model.eval()

    def predict_mask(self, sentence, error_id):
        text = '[CLS] '+' '.join(sentence)+' [SEP]'
        tokenized_text = self.tokenizer.tokenize(text)
        tokenized_text[error_id] = '[MASK]'

        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
        segments_ids = [0 for _ in range(len(sentence) + 2)]

        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        with torch.no_grad():
            predictions = self.model(tokens_tensor, segments_tensors)[0]

        predicted_index = torch.topk(predictions[0, error_id], 5)[1].cpu().numpy()
        list_mask_items = []
        for i in predicted_index:
            predicted_token = self.tokenizer.convert_ids_to_tokens([i])[0]
            list_mask_items.append(predicted_token)

        return list_mask_items

    def correct_with_bert(self, sentence):
        correct_result = []
        for i, char in enumerate(sentence):
            org_char_pinyin = get_sim_pronunciation(char)
            list_maybe_right = self.predict_mask(sentence, i + 1)
            for c in list_maybe_right:
                if get_sim_pronunciation(c) == org_char_pinyin:
                    if c != char:
                        correct_result.append([i, c])
                    break

        return correct_result
