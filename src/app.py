from position import Position
import dics.default_position as dp
from cv import Cv

cv = Cv.from_file('.pdf')

position = Position() \
    .set_name(dp.name) \
    .set_description(dp.description) \
    .gen_characteristics()

print(position.description)
print(position.characteristics)
print(cv.name)
print(position.rate_cv(cv))

