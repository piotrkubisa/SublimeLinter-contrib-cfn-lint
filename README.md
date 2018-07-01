SublimeLinter-contrib-cfn-lint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-cfn-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-cfn-lint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [cfn-lint](https://github.com/awslabs/cfn-python-lint). It will be used with files that have the yaml (CloudFormation) syntax.

## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `cfn-lint` is installed on your system.

In order for `cfn-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-cfn-lint settings:

|Setting|Description    |
|:------|:--------------|
|foo    |Something.     |
|bar    |Something else.|
