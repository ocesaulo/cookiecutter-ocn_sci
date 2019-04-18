#!/usr/bin/env python
import os
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.pure_sci }}' == 'y':
        print('Doing just scuence template')
        remove_file('tests/*')
        os.rmdir('tests')
        os.rmdir('scripts')
        os.rmdir('lib')
        remove_file('setup.py')
        # remove_file('environment.yml')  # an environment is not necessary or
        # desirable... but maybe it is
        remove_file('requirements.txt')
        remove_file('.travis.yml')
        remove_file('{{ cookiecutter.repo_name}}/*')
        os.rmdir('{{cookiecutter.repo_name}}')
        os.mkdir('codes/')
    elif '{{ cookiecutter.pure_soft }}' == 'y':
        print('Doing just software template')
        os.rmdir('manuscripts')
        os.rmdir('presentations')
        os.rmdir('analyses/figures')
        os.rmdir('analyses')
        os.rmdir('data')
        # add conda-autoenv.sh to bashrc/profile/cshrc (DOES NOT BELONG HERE)
        # print('Installing conda-autenv')
    else:
        print('Doing full template')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    # add entry on gitignore for data dir
    subprocess.call(['sed', '-i.bak', ''s/#\/data\//\/data\//'', '{{
        cookiecutter.repo_name }}/.gitignore'])

    # initiate the local git repo, first commit and master/origin push
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'branch', 'develop'])
    subprocess.call(['git', 'checkout', 'develop'])
