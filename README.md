# easyrelease
> Automate your GitHub, pypi and conda releases


## How to install

Via pip

`pip install easyrelease`

or via conda

`conda install easyrelease`

## Packages vs Application

We conceptually differentiate between two kind of projects:

* Packages: These are python projects you want to bundle for others to install via `pip` or `conda`
* Applications: These are python projects without packaging purposes like a web application. You can still use this package for this kind of projects in order to automate your release workflow

## How to use

### Prerequisites

After installation you need the fulfill the following prerequisites for the package to work:

#### Git project

You need to initialize a git project in your project root folder for this package to work, i.e. run in your command line

`git init`

#### GitHub credentials

You need to store your GitHub credentials (GitHub username and token) in your project root for automatic GitHub releases. The credentials should be stored in a file called `.gh-credentials` with the following contents:

```ini
gh_user = Your GitHub username
gh_token = Your GitHub token
```

#### Package structure

> Only for python packages

For this package to work you need to comply to the following minimal project structure for python packages

```
package_name
|-- .git
|-- package_name
|   |-- __init__.py
|   |-- module1.py
|   |-- module2.py
|   |-- ...
|-- tests
|   |-- test_module1.py
|   |-- test_module2.py
|   |-- ...
```

#### Pypi credentials

> Only for python packages

To publish to Pypi you need to store your pypi credentials in a file with the name `.pypi-credentials` in your user root or project root directory. The file should include the following contents

```ini
username = Your Pypi username
password = Your Pypi password
```

#### Anaconda credentials

> Only for python packages

To publish to Anaconda you need to store your anaconda credentials in a file with the name `.anaconda-credentials` in your user root or project root directory. The file should include the following contents

```ini
username = Your Anaconda username
password = Your Anaconda password
```

### Getting started

#### For applications

Only once:

0. Fulfill the [prerequisites](#prerequisites)
1. Run `easyrelease-init application`
2. Edit your in the previous step generated file `settings.ini`
3. Edit your in the previous step generated file `.gh-release-config.yaml`

Each time you want to make a GitHub release:

1. Run `gh-release` to make a GitHub release
2. Run `make-changelog` to generate / update your CHANGELOG

#### For packages

Only once:

0. Fulfill the [prerequisites](#prerequisites)
1. Run `easyrelease-init application`
2. Edit your in the previous step generated file `settings.ini`
3. Edit your in the previous step generated file `.gh-release-config.yaml`
4. Run `login-to-anaconda`

Each time you want to release / publish your package:

1. Run `gh-release` to make a GitHub release
2. Run `make-changelog` to generate / update your CHANGELOG
3. Run `publish-pypi-package` to publish to pypi
4. Run `update-meta-yaml` to generate / update your meta.yaml under conda-bld
  * (Optionally recommended): Check your meta.yaml
5. Run `build-conda-package` to build your conda package
7. Run `upload-conda-package` to publish your conda package
