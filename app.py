from gfw import rules


def main():
    """
    Main Function
    """
    pac_set = set()
    with open("./user-rule.txt") as pac_file:
        for line in pac_file:
            if line[:-2] not in rules:
                pac_set.add(line)

    with open("./user-rule.txt", "w") as pac_file:
        for line in sorted(list(pac_set)):
            pac_file.write(line)


if __name__ == "__main__":
    main()
