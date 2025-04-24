import argparse


def main():
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument("name", help="Name of the user")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()