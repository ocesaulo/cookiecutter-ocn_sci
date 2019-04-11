{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{{ cookiecutter.project_name }}
{{ cookiecutter.project_name|count * "=" }}

{% if cookiecutter.readme_pypi_badge -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}
        :alt: Latest PyPI version
{%- endif %}

{% if cookiecutter.readme_travis_badge -%}
.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}
        :alt: Latest Travis CI build status
{%- endif %}

{% if cookiecutter.readme_readthedocs_badge -%}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.package_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

Overview
--------

{{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

Installation
------------

Usage/Example
-----

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`{{ cookiecutter.package_name }}` was written by `{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>`_.

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io.
{% endif %}

