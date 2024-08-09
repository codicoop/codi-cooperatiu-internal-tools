# codi-cooperatiu-internal-tools
Eines i mòduls interns de Codi Cooperatiu

# Contribució
## Instal·la els requisits

Instal·la les dependències per al desenvolupament anant a la carpeta «codi-cooperatiu-internal-tools» i després s'executa:

```commandline
pip install -r requirements.txt
```

A més d'aquests requisits també hauràs d'instal·lar el propi Django. Per a instal·lar la versió actual de Django:

```commandline
pip install django
```

El codi ve amb git hook scripts. Aquests es poden instal·lar executant-se:

```commandline
pre-commit install
```

El pre-commit ara s'executarà automàticament al fer git-commit i comprovarà l'adhesió a la guia d'estil (black, isort i flake8).

## Executa les proves

Abans d'enviar una pull request, executeu tot el conjunt de proves «codi-cooperatiu-internal-tools» via:

```commandline
make test
```

Si no teniu instal·lat el `make`, el conjunt de proves també es pot executar via:

```commandline
pytest --ds=tests.test_settings --cov=flowbite_classes
```