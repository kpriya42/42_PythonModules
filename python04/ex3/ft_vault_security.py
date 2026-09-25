#!/usr/bin/env python3


def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        with open(filename, action) as file:
            if action == 'r':
                data = file.read()
            elif action == 'w':
                file.write(content)
                data = "Content successfully written to file"
            else:
                return (False, 'Unknown action')
        return (True, data)
    except Exception as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    output: tuple[bool, str] = secure_archive("../Sample.txt", "r")
    print(output)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("New_vault_sec.txt", "w", output[1]))


if __name__ == "__main__":
    main()
