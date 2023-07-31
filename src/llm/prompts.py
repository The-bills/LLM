from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

find_name = PromptTemplate(
    template="""
The content of the resume will be presented to you.
Find in it and return only the name of the applicant.
The resume:
```
{resume}
```
The name of the applicant:""",
input_variables=["resume"],
)

describe_position = PromptTemplate(
    template="""
Poszukuje pracownika na stanowisko: {name} \n
Opis stanowiska: {description} \n
Jakie jest {n} najważniejszych cech i umiejętności jakie powinna spełniać osoba ubiegająca się \n
o stanowisko? Wypisz TYLKO cechy bez opisów, w formie listy języka python. Odpowedź podaj w języku angielskim.
{format_instructions}""",
    input_variables=["name", "description", "n"],
    partial_variables={"format_instructions": CommaSeparatedListOutputParser().get_format_instructions()},
)

rate_cv = PromptTemplate(
    template="""
Zostanie ci przedstawiona treść CV osoby ubiegającej się o stanowisko.
Nazwa stanowiska: "{name}" \n
Opis stanowiska: "{description}" \n
Oceń cv kandydata wynikiem procentowym w każdej podanej kategorii \n
Kategorie:
```
${characteristics}
```
Jako wynik podaj TYLKO listę w języku python o długości równej długości listy kryteriów,
gdzie każdy element jest liczbą z przedziału od 0 do 100 oznaczającą wynik procentowy kandydata w danej kategorii.

CV Kandydata:
```
{cv}
```
{format_instructions}""",
    input_variables=["name", "description", "characteristics", "cv"],
    partial_variables={"format_instructions": CommaSeparatedListOutputParser().get_format_instructions()},
)