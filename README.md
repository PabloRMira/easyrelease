# easyrelease
> Automate your GitHub, pypi and conda releases


[![PyPI](https://img.shields.io/pypi/v/easyrelease?color=yellow&label=pypi%20version)](https://pypi.org/project/easyrelease/#description)
[![conda](https://anaconda.org/pablormira/easyrelease/badges/version.svg)](https://anaconda.org/pablormira/easyrelease)
[![plattform](https://anaconda.org/pablormira/easyrelease/badges/platforms.svg)](https://anaconda.org/pablormira/easyrelease)

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

#### CONDA_BLD_PATH

> Only for Linux users and only in case of problems

In case of problems concerning permission errors building your package via `build-conda-package` you may need to add the following line to your `~/.bashrc`

```bash
export CONDA_BLD_PATH=/tmp/conda-bld
```


### Getting started

#### For applications

Only once:

0. Fulfill the [prerequisites](#prerequisites)
1. Run `easyrelease-init application`
2. Edit your in the previous step generated file `settings.ini`
3. Edit your in the previous step generated file `.gh-release-config.yaml`

`.gh-release-config.yaml` sets the title and keyword that will be used to assign your commits to a certain section in your GitHub release notes and changelog. So if for example you want all commits to be in your release notes without keyword matching, you could modify `.gh-release-config.yaml` as

```yaml
gh_categories:
  - title: "### Commits:"
    keyword: ""
```


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

## Versioning

We version our package via [semantic versioning](https://semver.org), i.e., 

* We use three digits separated by points x1.x2.x3, e.g. 0.5.1
* We increase x1 (the major version) if we introduce breaking changes
  * Exception: Versions with 0 at the beginning (e.g. 0.5.1) mean that the package is not stable yet and therefore every new feature could be a breaking change
* We increase x2 (the minor version) if we introduce a new feature
* We increase x3 (the patch version) if we fix a bug

New documentation, refactoring / maintenance of code and admin tasks do not change the versions.

You can follow the changes introduced by each version in our [CHANGELOG](https://github.com/PabloRMira/easyrelease/blob/main/CHANGELOG.md)

## Differences to [fastrelease](https://github.com/fastai/fastrelease)

This package was inspired by the [fastrelease](https://github.com/fastai/fastrelease) package but it differs from it in the way it generates the release notes. 

`easyrelease` generates the release notes out of the commit messages whereas `fastrelease` generates the release notes out of GitHub issues.

This package was also motivated by the fact that `fastrelease` did not work for me out of the box in my first attempt and I really liked the idea of automating releases and package publishing.

## Compatibility with [nbdev](https://github.com/fastai/nbdev)

This package was developed and is compatible with the [nbdev](https://github.com/fastai/nbdev) framework but it also works for ordinary project development without notebooks.

In the case you want to develop your project with `nbdev` you need to first initialize your project via `nbdev` and afterwards run `easyrelease-init`. This is because the `settings.ini` we initialize for your project is a proper / strict subset of the `settings.ini` from `nbdev`
