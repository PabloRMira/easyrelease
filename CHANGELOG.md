# Release notes

## 0.2.2

### :tada: Bugfixes:
* [FIX] Missing requirement twine ([#27](https://github.com/PabloRMira/easyrelease/pull/27))

## 0.2.1

### :tada: Bugfixes:
* [FIX] conda-build with option --build-only does not output package to project folder ([#22](https://github.com/PabloRMira/easyrelease/pull/22))

### :bulb: Documentation:
* [DOC] Add documentation ([#26](https://github.com/PabloRMira/easyrelease/pull/26))

## 0.2.0

### :rocket: New features:
* [FEA] Run pytests or nbdev_test_nbs before GitHub release, pypi publishing or conda build
* [FEA] Add functions to build package and publish to pypi ([#14](https://github.com/PabloRMira/easyrelease/pull/14))
* [FEA] Add tools to for conda packaging and anaconda upload ([#8](https://github.com/PabloRMira/easyrelease/pull/8))
* [FEA] Add templates and CLI to setup project ([#5](https://github.com/PabloRMira/easyrelease/pull/5))
* [FEA] Add function to update gitignore ([#4](https://github.com/PabloRMira/easyrelease/pull/4))

### :bulb: Documentation:
* [DOC] Document package usage

### :hammer_and_wrench: Refactoring / Maintenance:
* [MNT] Reduce dependency on fastcore ([#15](https://github.com/PabloRMira/easyrelease/pull/15))
* [MNT] Robustify ini templates and enhanced gh-release-config ([#12](https://github.com/PabloRMira/easyrelease/pull/12))
* [MNT] Shutdown CI because not working with conda ([#10](https://github.com/PabloRMira/easyrelease/pull/10))