cookiecutter-ocn_sci
====================

.. image:: https://img.shields.io/pypi/v/cookiecutter_ocn_sci.svg
        :target: https://pypi.python.org/pypi/cookiecutter_ocn_sci
        :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/ocesaulo/cookiecutter_ocn_sci.svg
        :target: https://travis-ci.org/ocesaulo/cookiecutter_ocn_sci
        :alt: Latest Travis CI build status

.. image:: https://readthedocs.org/projects/cookiecutter-ocn-sci/badge/?version=latest
        :target: https://cookiecutter-ocn-sci.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Overview
--------

Science Projects Boilerplate

Cookiecutter template of directory structure for ocean data science projects, whether
focused purely on science or with a software development component.
Automates boring things like starting a git version control repo and creation, 
activation and deactivation of conda environments.

Inspired by several templates:

pythonpypackage
minimal
datascience

Installation
------------

1) Install cookiecutter::
        
        pip install -U cookiecutter

2) Install conda-autoenv (https://github.com/sharonzhou/conda-autoenv)::

        pip install git+https://github.com/ocesaulo/conda-autoenv.git@develop
        echo "source `which conda_autoenv.sh`" >> ~/.bash_profile
 
Usage/Example
-------------

Run::

   cookiecutter https://github.com/ocesaulo/cookiecutter-ocn_sci.git

Give inputs and select the options; pure_sci deletes python pkg developement
files and directories, while pure_soft deletes folders related to the
organization of the science component: manuscripts, analyses, figures, etc. 

If you no like:
---------------

I don't either, so modify the .json file and then create your own structure based on this.

TODO
-------

Still a work in progress...

May want to tweak what get's git initialized or the structure of folders

May want to add more specific templates for scripts, notebooks

Improve the test and doc templating

Authors
-------

`cookiecutter_ocn_sci` was written by `Saulo M Soares <ocesaulo@gmail.com>`_.


* Free software: MIT license
* Documentation: https://cookiecutter-ocn-sci.readthedocs.io.

