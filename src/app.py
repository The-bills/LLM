from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from position import Position
import dics.default_position as dp
from cv import Cv


#conn.commit()
#conn.close()

position = Position.get('123e4567-e89b-12d3-a456-426614174000')
cv = Cv.from_file('.pdf')

print(cv.name)
for (q, score) in zip(position.qualifications, position.rate_cv(cv)):
    print(q, ":", score, "%")

