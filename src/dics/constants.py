max_output = 10
position = 'Senior Java Developer'
cv_analysis_user_message = f""" 
Poszukuję kandydata na stanowisko {position}. Który z podanych \n
kandydatów jest najlepszy na to stanowisko? Wypisz TYLKO procentowe ocenienie kandydatów \n
"""
cv_analysis_system_message =  f"""
Zostaną pokazane tobie CV kandydatów w postaci listy w języku python. Twoim zadaniem \n
będzie procentowe ocenienie kompatybilności kandydatów z stanowiskiem oferownaym przez \n
użytkownika. Ocena będzie przedstawiona w formie procentowej kompatybilności z podanym \n
stanowiskiem na podstawie trzech kategori: Umiejętności wymagane na dane stanowisko, \n
Doświadczenie zawodowe, Wykształcenie w kierunku danej pozycji. Rezulaty oceny przedstawiaj \n
w formacie JSON z uwzględnieniem TYLKO oceny procentowej w trzech kategoriach:
Umiejętności
Wykształcenie
Doświadczenie
Następnie stwórz kolejną wartość, zwaną "Ocena Końcowa", będącą średnią trzech powyższych kategorii
"""
cv_analysis_system_basic_message = f"""
Zostną tobie pokazane CV kandydatów w postaci listy w języku python. Twoim zadniem jest \n
ich analiza i odpowiedź na pytanie {cv_analysis_user_message}, w oparciu o wcześniej ]n
wypisane cechy.
"""
postion_perfect_description = f""""
Jakie jest {max_output} najważniejszych cech jakie powinna spełniać osoba ubiegająca się \n
o stanowisko {position}? Wypisz TYLKO cechy bez opisów, w formie listy.
"""
