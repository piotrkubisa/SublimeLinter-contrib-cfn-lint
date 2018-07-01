from SublimeLinter.lint import Linter


class cfnlint(Linter):
    # TODO: Use custom path to the cflint
    cmd = ('cfn-lint', '--template', '${file}', '--format', 'parseable')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+):\d+:\d+:((?P<warning>W.\d+)|(?P<error>E.\d+)):(?P<message>.+)'
    multiline = True

    defaults = {
        'selector': 'source.yaml, source.json',
    }
