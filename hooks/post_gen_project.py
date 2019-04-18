#!/usr/bin/env python
import os
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.pure_sci }}' == 'y':
        print('Doing just science template')
        remove_file('tests/test_{{cookiecutter.repo_name}}.py')
        os.rmdir('tests')
        remove_file('scripts/.keep')
        os.rmdir('scripts')
        remove_file('lib/.keep')
        os.rmdir('lib')
        remove_file('setup.py')
        # remove_file('environment.yml')  # an environment is not necessary or
        # desirable... but maybe it is
        remove_file('requirements.txt')
        remove_file('.travis.yml')
        remove_file('{{ cookiecutter.repo_name}}/__init__.py')
        remove_file('{{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}.py')
        os.rmdir('{{cookiecutter.repo_name}}')
        os.mkdir('codes/')
    elif '{{ cookiecutter.pure_soft }}' == 'y':
        print('Doing just software template')
        remove_file('manuscripts/.keep')
        os.rmdir('manuscripts')
        remove_file('presentations/.keep')
        os.rmdir('presentations')
        remove_file('analyses/figures/.keep')
        remove_file('analyses/.keep')
        os.rmdir('analyses/figures')
        os.rmdir('analyses')
        remove_file('data/.keep')
        os.rmdir('data')
        # add conda-autoenv.sh to bashrc/profile/cshrc (DOES NOT BELONG HERE)
        # print('Installing conda-autenv')
    else:
        print('Doing full template')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    # add entry on gitignore for data dir
    subprocess.call(['sed', '-i.bak', 's/# \/data\//\/data\//', '.gitignore'])

    # delete all the .keep files, so that future git-ing don't track empty
    for root, dirs, files in os.walk("."):
        for file_ in [file_ for file_ in files if file_ == '.keep']:
            os.remove(os.path.join(root, file_))

    # initiate the local git repo, first commit and master/origin push
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'branch', 'develop'])
    subprocess.call(['git', 'checkout', 'develop'])
