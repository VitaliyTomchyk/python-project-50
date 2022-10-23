from gendiff.cli.cli import parcer
from gendiff.generate_diff.generate_diff import generate_diff


def main():
    parce = parcer()
    result = generate_diff(parce[0], parce[1], parce[2])
    return result


if __name__ == '__main__':
    main()
