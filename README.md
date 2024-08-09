# codi-cooperatiu-internal-tools
Eines i mòduls interns de Codi Cooperatiu

# Contribució
## Instal·la els requisits

Instal·la les dependències per al desenvolupament anant a la carpeta «codi-cooperatiu-internal-ttols» i després s'executa:

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