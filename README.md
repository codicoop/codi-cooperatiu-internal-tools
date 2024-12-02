# codi-cooperatiu-internal-tools

Internal tools and modules of Codi Cooperatiu

## flowbite_css

`flowbite_css` automatically applies form customizations. These customizations use Flowbite styles, a customization of Tailwind.

### Configuration

To use these customizations, you need to add the `flowbite_css` app to the `INSTALLED_APPS` parameter in the `settings.py` file.

#### CODI_COOP_ENABLE_MONKEY_PATCH

The `CODI_COOP_ENABLE_MONKEY_PATCH` parameter in the `settings.py` file controls whether a monkey patch is applied to Django's form fields within your application.

By default, the `CODI_COOP_ENABLE_MONKEY_PATCH` parameter is disabled (`False`). This means the monkey patch will not be applied. If you want to enable the monkey patch, you need to add the `CODI_COOP_ENABLE_MONKEY_PATCH` parameter to the `settings.py` file and set it to `True`.

#### Examples:

**Enable monkey patching:**

```python
# settings.py

CODI_COOP_ENABLE_MONKEY_PATCH = True
```

When this parameter is enabled (`True`), Django form fields such as `CharField`, `EmailField`, `IntegerField`, `ChoiceField`, `MultipleChoiceField`, and `BooleanField` will use the custom fields defined in your application (`CharBoundField`, `BooleanBoundField`, etc.), enabling custom styling and behavior in your forms.

**Disable monkey patching:**

```python
# settings.py

CODI_COOP_ENABLE_MONKEY_PATCH = False  # Default value
```

If this parameter is disabled (`False`), Django's form fields will work with their default behavior and styling, without additional customizations.

#### FORM_RENDERER

You can also use a custom template to render all the HTML associated with the fields (`<label />` and any other HTML) with Flowbite classes. In this case, you need to use the `CustomFormRenderer` form renderer by configuring the `FORM_RENDERER` parameter in the `settings.py` file:

```python
# settings.py

FORM_RENDERER = "flowbite_css.renderers.CustomFormRenderer"
```

# Contribution

## Install Requirements

Install the development dependencies by navigating to the "codi-cooperatiu-internal-tools" folder and running:

```commandline
pip install -r requirements.txt
```

In addition to these requirements, you also need to install Django. To install the current version of Django:

```commandline
pip install django
```

The code comes with git hook scripts. These can be installed by running:

```commandline
pre-commit install
```

The pre-commit hook will now run automatically when making a git commit, checking adherence to the style guide (black, isort, and flake8).

## Run Tests

Before submitting a pull request, run the full test suite of "codi-cooperatiu-internal-tools" using:

```commandline
make test
```

If you do not have `make` installed, the test suite can also be executed using:

```commandline
pytest --ds=tests.test_settings --cov=flowbite_classes
```
