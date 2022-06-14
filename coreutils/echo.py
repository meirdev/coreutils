import re

import click


def interpreter_backslash_escape(string: str) -> str:
    def callback(match: re.Match) -> str:
        chars = match.group("chars")

        match chars[0]:
            case "a":
                chars = "\a"
            case "b":
                chars = "\b"
            case "f":
                chars = "\f"
            case "n":
                chars = "\n"
            case "r":
                chars = "\r"
            case "v":
                chars = "\v"
            case "x":
                chars = chr(int(chars[1:], base=16))
            case "0":
                chars = chr(int(chars[1:], base=8))
            case "\\":
                chars = "\\"

        return chars

    if (blackslash_c_idx := string.find("\c")) != -1:
        string = string[:blackslash_c_idx]
    else:
        string = re.sub(
            r"\\(?P<chars>[\\abcfnrtv]|x[a-f0-9]{1,2}|0[0-7]{1,3})",
            callback,
            string,
            flags=re.IGNORECASE,
        )

    return string


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.argument("string", nargs=-1)
@click.option(" /-n", "newline", default=True)
@click.option("-e/-E", "escape", default=True)
def main(
    string: tuple[str, ...],
    newline: bool,
    escape: bool,
):
    string = " ".join(string)

    if escape:
        string = interpreter_backslash_escape(string)

    end = "\n" if newline else ""

    print(string, end=end)


if __name__ == "__main__":
    main()
