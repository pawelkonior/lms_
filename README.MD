# LMS - learning management system

## ALgorytm implementacji funkcjonalności w Django
1. Czy potrzebuję do tego Django app?
    - `python manage.py startapp <app_name>`
    - następnie dodaj do settings.py w INSTALLED_APPS -> '<app_name>.apps.<class>'
2. Czy potrzebuję do tego dane?
    - tworzę modele w `<app_name>/models.py`
    - tworzę migracje -> `python manage.py makemigrations <app_name>`
    - aplikuję migracje -> python manage.py migrate `<app_name>`
    - ? sprawdzam fizycznie w bazie danych, czy jest ok
    - piszę unit tests
3. Czy potrzebuję obsługę z CMS (django Admin)?
    - w pliku `<app_name>/admin.py` rejestrujemy model
    - admin.site.register
4. Czy potrzebuję formularz?
    - w pliku `<app_name>/forms.py` tworzę formularz za pomocą django forms
    - piszę unit tests
5. Czy potrzebuję Widok (Logikę)?
   - w pliku `<app_name>/views.py` tworzę widoki -> docelowo należy używać class
   - piszę unit tests
6. Czy potrzebuję template do widoku?
    - tworzę go w `<app_name>/templates/<app_name_namespace>/<file_name>.html`
    - podpinam do widoku
    - piszę unit tests
7. czy potrzebny jest router?
   - tworzę lokalny router -> `<app_name>/urls.py` -> użyj live template
   - pamiętaj o app_name (namespace) i name do endpointa
   - podpisam lokalny router do globalnego -> `config/urls.py` -> funkcja include
   - piszę unit tests
8. Testuję manualnie, czy działa
    - PROFIT:
