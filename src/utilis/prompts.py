from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

find_name_from_cv = PromptTemplate(
    template="""
The content of the resume will be presented to you.
Find in it and return only the name of the applicant.
The resume:
```
{resume}
```
The name of the applicant:  """,
input_variables=["resume"],
)

describe_position = PromptTemplate(
    template="""
Poszukuje pracownika na stanowisko: {name} \n
Opis stanowiska: {description} \n
Jakie jest {n} najważniejszych cech i umiejętności jakie powinna spełniać osoba ubiegająca się \n
o stanowisko? Wypisz TYLKO cechy bez opisów, w formie listy języka python. Odpowedź podaj w języku angielskim.
{format_instructions}
""",
    input_variables=["name", "description", "n"],
    partial_variables={"format_instructions": CommaSeparatedListOutputParser().get_format_instructions()}
)

rate_cv = PromptTemplate(
    template="""
Zostanie ci przedstawiona treść CV osoby ubiegającej się o stanowisko.
Nazwa stanowiska: "{name}" \n
Opis stanowiska: "{description}" \n
Oceń cv kandydata w każdej podanej kategorii \n
Kategorie:
```
${characteristics}
```
Jako wynik podaj listę ocen w skali od 0 do 100 w tej samej kolejności co kategorie.
Ocenę poszcególnej kategorii kandydata pobierz z tabelki na podstawie jego doświadczenia.
Tabelka:
{table_cryteria}
Dodatkowo, jeśli osoba posiada dodatkowe zdolności lub projektu, możesz do oceny dodać
wartość 10.
CV Kandydata:
```
{cv}
```
{format_instructions}""",
    input_variables=["name", "description", "characteristics", "cv","table_cryteria"],
    partial_variables={"format_instructions": CommaSeparatedListOutputParser().get_format_instructions()},
)

