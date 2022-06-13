import click


@click.command()
@click.argument("string", nargs=-1)
def main(string: tuple[str, ...]):
    string = list(string)

    if len(string) == 0:
        string = ["y"]

    string = " ".join(string)

    while True:
        print(string)


if __name__ == "__main__":
    main()
