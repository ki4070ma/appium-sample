[![Build Status](https://dev.azure.com/ki4070ma/ki4070ma.appium-sample/_apis/build/status/ki4070ma.appium-sample?branchName=master)](https://dev.azure.com/ki4070ma/ki4070ma.appium-sample/_build/latest?definitionId=3&branchName=master)
[![Build Status](https://travis-ci.org/ki4070ma/appium-sample.svg?branch=master)](https://travis-ci.org/ki4070ma/appium-sample)

# Readme
To learn appium

## Folder

### Preparation
* Run appium server

### mobile
* For android phone
* Run script
   * ```python GnucashAndroidTest.py```
* Run mypy
   * ```mypy .```
* Run pyright
   * ```npx pyright .```

### tv
* For android tv

# Development
* Setup
   * ```pip install -r development.txt```
   * ```pre-commit install```
* Autopep8
   * ```python -m autopep8 -r --global-config .config-pep8 -i .```
