from profanity_check import predict_prob, predict
# print(predict_prob(['shit'])[0])
import re

text = 'rohoe'
pattern = r'\b(?:rohoe|ROHOE|Rohoe|rOhoe|R)\b'
print(re.match(pattern, text))


