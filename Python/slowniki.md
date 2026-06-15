# Słowniki

Słowniki przechowują dane w formacie **klucz: wartość**.

---

## Tworzenie słownika

```python
samochod = {
    "marka": "Honda",
    "model": "Civic",
    "rok_produkcji": 2008,
    "czy_elektryczny": False,
    "kolory": ["Czarny", "Biały", "Beżowy", "Czerwony"]
}
```

---

## Podstawowe operacje

```python
print(samochod) # {'marka': 'Honda', 'model': 'Civic', 'rok_produkcji': 2008, 'czy_elektryczny': False, 'kolory': ['Czarny', 'Biały', 'Beżowy', 'Czerwony']}

print(samochod["model"]) # Civic
print(samochod["kolory"]) # ['Czarny', 'Biały', 'Beżowy', 'Czerwony']
print(len(samochod)) # 5
print(type(samochod)) # <class 'dict'>
```

---

## Sprawdzenie czy klucz istnieje

```python
if "model" in samochod:
    print("Klucz model jest w słowniku 'samochod'")

if "drzwi_ilosc" in samochod:
    print("Klucz drzwi_ilosc jest w słowniku 'samochod'")
else:
    print("Nie ma klucza drzwi_ilosc w słowniku 'samochod'")
```

---

## Zmiana wartości

```python
samochod["model"] = "Accord"  # Zamienia Civic na Accord
print(samochod) # {'marka': 'Honda', 'model': 'Accord', 'rok_produkcji': 2008, 'czy_elektryczny': False, 'kolory': ['Czarny', 'Biały', 'Beżowy', 'Czerwony']}
```

---

## Tworzenie słownika funkcją `dict()`

```python
komputer = dict(procesor = "Intel", ram_GB = 32, zasilacz_W = 750)
print(komputer) # {'procesor': 'Intel', 'ram_GB': 32, 'zasilacz_W': 750}
```

---

## Pobieranie kluczy

```python
klucze = komputer.keys()
print(klucze) # dict_keys(['procesor', 'ram_GB', 'zasilacz_W'])
```

---

## Dodawanie nowego elementu

```python
komputer["Karta_graficzna"] = "Nvidia"
print(komputer) # {'procesor': 'Intel', 'ram_GB': 32, 'zasilacz_W': 750, 'Karta_graficzna': 'Nvidia'}
```

---

## Usuwanie elementu

```python
komputer.pop("Karta_graficzna")
print(komputer) # {'procesor': 'Intel', 'ram_GB': 32, 'zasilacz_W': 750}
```

---

## Iterowanie po słowniku

```python
# Wyświetla klucze
for i in komputer:
    print(i)

# Wyświetla wartości
for i in komputer:
    print(komputer[i])
```