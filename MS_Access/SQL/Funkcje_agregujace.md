# Funkcje agregujące

**COUNT()** - zlicza rekordy.
```sql
SELECT COUNT(*) FROM Uczniowie;
```

**SUM()** - oblicza sumę.
```sql
SELECT SUM(Punkty) FROM Wyniki;
```

**AVG()** - oblicza średnią.
```sql
SELECT AVG(Punkty) FROM Wyniki;
```

**MIN()** - zwraca najmniejszą wartość.
```sql
SELECT MIN(Punkty) FROM Wyniki;
```

**MAX()** - zwraca największą wartość.
```sql
SELECT MAX(Punkty) FROM Wyniki;
```