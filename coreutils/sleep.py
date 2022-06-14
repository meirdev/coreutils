import time

import click


def convert_seconds(seconds: str) -> float:
    suffix_multiplier = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "d": 60 * 60 * 24,
    }

    if seconds[-1] in suffix_multiplier:
        suffix = seconds[-1]
        seconds = seconds[:-1]
    else:
        suffix = "s"

    seconds = float(seconds)
    if seconds < 0:
        raise ValueError

    return seconds * suffix_multiplier[suffix]


def validate_seconds(_ctx, _param, value: tuple[str, ...]) -> tuple[float, ...]:
    seconds_list = []

    try:
        for seconds in value:
            seconds_list.append(convert_seconds(seconds))
    except (ValueError, IndexError):
        raise click.BadParameter(f'invalid time interval "{seconds}"') from None

    return tuple(seconds_list)


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.argument("seconds", nargs=-1, required=True, callback=validate_seconds)
def main(seconds: tuple[float, ...]):
    time.sleep(sum(seconds))


if __name__ == "__main__":
    main()
