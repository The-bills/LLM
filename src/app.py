from utilis import *
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from position import Position
import dics.default_position as dp
from cv import Cv

cv = Cv.from_file('cv.pdf')

position = Position() \
    .set_name(dp.name) \
    .set_description(dp.description) \
    .gen_characteristics()

print(position.characteristics)
print(cv.name)
print(position.rate_cv(cv))

