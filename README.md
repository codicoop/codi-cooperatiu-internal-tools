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

### Available fields

This library monkey patches many of the default Django fields, meaning that
when you use these Django fields as you would normally do in any model,
you will actually end up using a version of the field that uses a custom
template.

The custom template is specified at `renderers.CustomFormRenderer`.

The custom field templates define the field part of the form control, which means,
the part that is not the widget itself.
As you'll see in every template in the `fields` directory, there's the markup for
rendering labels, errors and so on, but the control itself is rendered with:

`{{ field }}`

This is the part depends on what widget is specified in the Django Form class 
for that field.

We needed to control the classes that will be included in the control itself
(the widget), which needed to be different depending on having or not an error
in the field.

The problem is that when Django renders the widget, the context does not include
any way to know if the field had an error or not.

Check `forms.BaseBoundField` to understand how we solved the problem.

#### CharField, EmailField, IntegerField, ChoiceField, MultipleChoiceField

Bound field that sets the custom classes in the widget: `forms.CharField`
Custom field template: `fields/other.html`.

#### BooleanBoundField

Bound field that sets the custom classes in the widget: `forms.BooleanBoundField`
Custom field template: `fields/checkbox.html`.

#### FileBoundField

Bound field that sets the custom classes in the widget: `forms.FileBoundField`
Custom field template: `fields/file.html`.

#### TimeBoundField

Bound field that sets the custom classes in the widget: `forms.TimeBoundField`
Custom field template: `fields/time.html`.

To use this field is necessary to use the `widgets.FlowBiteTimeInput`
widget in your form's field.

#### DateBoundField

Bound field that sets the custom classes in the widget: `forms.DateBoundField`
Custom field template: `fields/date.html`.

To use this field is necessary to use the `widgets.FlowBiteDateInput`
widget in your form's field.

### Available widgets

The widgets in this section can work with the `CharField` field classes and
template, which is monkey patched to use the `CharBoundField` as a bound field, and 
therefore, the field part will be rendered with the `fields/other.html` tempalte.

In other words, the only part that we need to override to achieve the desired
result is the widget template and/or properties.

#### Standard numeric input

In most cases we want to show a numeric field that doesn't come with the up and
down arrows to increase and decrease the number.
Additionally, we want to control how the number is rendered in the field, i.e.,
if we're outputting the number with commas as a decimal separator, some browsers
will modify the numeric input controls and replace the decimal separator with
dots, causing inconsistent behavior.

To achieve that we need the input control to be a `text` type, and to add to it
a `data-input-counter` property that will limit the field to numeric characters.

Implementation: use the widget `widgets.FlowBiteNumericInput` as you would
normally do with any Django widget.

#### Incremental numeric input

This input displays a plus and minus buttons at the sides of the control for
increasing and decrementing the number.

Implementation: use the widget `widgets.FlowBiteNumericIncrementalInput` as you would
normally do with any Django widget.

# Contribution

## Install Requirements

Make sure you are using python >3.10.

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

## Run linting, formatting and tests using tox

[Install tox](https://tox.wiki/en/4.23.2/installation.html) in a isolated
environment, for exampel if you use pip, run:

```commandline
python -m pip install --user tox
```

Then you can run it with:

```commandline
python -m tox
```

One of the tox commands is the linter, you can run it alone with:

```commandline
python -m tox -e lint
```

Note that tox is meant to be run in the github action that will provide different
python versions, but if you run it like that it will only run in the version
that you have in your environment.

## Publishing a New Version to PyPI

To release a new version of the library to PyPI, follow these steps:

1. **Prepare a Release Branch:**
   - Ensure all changes are merged into the `master` branch.
   - Create a new branch named after the release version (e.g., `v1.2.3`).
   - Update the `version` field in the `project` section of the `pyproject.toml` file to the new release version.
   - Commit the changes with a message like `Version <release-version>`.
   - Push the branch to the remote repository and create a pull request titled `Version <release-version>`.

2. **Tag the Release:**
   - Once the pull request has been reviewed and merged, create a Git tag for the release. Use the following command:
     ```bash
     git tag -a <release-version> <commit> -m "Release <release-version>"
     ```
     Replace `<release-version>` with the version number (e.g., `v1.2.3`) and `<commit>` with the commit hash of the merged pull request.
   - Push the tag to the remote repository:
     ```bash
     git push origin <release-version>
     ```

3. **Create a GitHub Release:**
   - Open the [GitHub Releases page](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release).
   - Click "Draft a new release."
   - In the **Tag version** field, select the previously pushed tag `<release-version>`.
   - Use `<release-version>` as the release title.
   - In the description, list the changes introduced in this release compared to the previous version.
   - Click "Publish release."

4. **Automatic Deployment:**
   - Once the release is published, GitHub Actions will automatically trigger the deployment process and publish the new version of the library to PyPI, as configured in the repository.
