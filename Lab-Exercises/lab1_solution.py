def determine_clearance_tier(age, is_developer):
    if age < 18:
        return "Tier 3: Guest"
    if is_developer:
        return "Tier 1: Admin Infrastructure Access"
    return "Tier 2: Standard Executive Access"


def parse_developer_status(value):
    return value.strip().lower() == "yes"


def main():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: ").strip())
    developer_status = input("Are you a developer? (yes/no): ")
    is_developer = parse_developer_status(developer_status)

    clearance_tier = determine_clearance_tier(age, is_developer)
    print(
        f"Profile Summary: Name={name}, Age={age}, "
        f"Developer={is_developer}, Clearance={clearance_tier}"
    )


if __name__ == "__main__":
    main()
