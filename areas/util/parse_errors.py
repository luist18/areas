import re

warning_regex = re.compile(r'.*Warning: (?P<warning>.*)')
error_regex = re.compile(r'.*.s:(?P<line>\d*): Error: (?P<error>.*)')
undefined_regex = re.compile(r'.*undefined reference to (?P<undefined>.*)')


def parse_compilation_errors(output):
    output = output.split('\\n')

    warnings = []
    errors = []

    for line in output:
        if warning_regex.match(line):
            # get group warning
            group = warning_regex.match(line).group('warning')

            group = group.replace("'", '`').strip()

            warnings.append(group)

        if error_regex.match(line):
            # get group error
            group = error_regex.match(line).group('error')
            # get group line
            error_line = error_regex.match(line).group('line')

            group = group.replace("'", '`').strip()

            errors.append({
                "line": error_line,
                "error": group,
            })

        if undefined_regex.match(line):
            # get group undefined
            group = undefined_regex.match(line).group('undefined')

            group = group.replace("'", '`').strip()

            errors.append({
                "error": f"undefined reference to {group}",
            })

    return warnings, errors
