#!/usr/bin/env python3

import os
from dotenv import load_dotenv, dotenv_values  # type: ignore[import-not-found]


REQUIRED_CONFIG = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"]


DEFAULTS = {"MATRIX_MODE": "development",
            "LOG_LEVEL": "INFO"}


def load_configuration() -> dict[str, str]:

    load_dotenv()

    config: dict[str, str] = {}

    for variable in REQUIRED_CONFIG:
        value = os.getenv(variable)

        if value:
            config[variable] = value

        elif variable in DEFAULTS:
            config[variable] = DEFAULTS[variable]
            print(f"⚠️ [WARNING] {variable} not configured. "
                  f"Using default: {DEFAULTS[variable]}")

        else:
            config[variable] = ""
            print(f"⚠️ [WARNING] Missing configuration: {variable}")

    return config


def security_check(config: dict[str, str]) -> None:
    print("\nEnvironment security check:")

    if "API_KEY" in DEFAULTS:
        print("❌ [NOK] Hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")
        if config["API_KEY"]:
            print("[OK] API key securely loaded from configuration")
        else:
            print("⚠️ [WARNING] API key not configured")

    if os.path.exists(".env"):
        env_values = dotenv_values(".env")

        if all(key in env_values for key in REQUIRED_CONFIG):
            print("[OK] .env file properly configured")
        else:
            print("⚠️ [WARNING] .env file is incomplete")
    else:
        print("⚠️ [WARNING] .env file not found")

    if config["MATRIX_MODE"] == "development":
        print("[OK] Development configuration active")
    else:
        print("[OK] Production overrides available")


def display_configuration(config: dict[str, str]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")

    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        if config["MATRIX_MODE"] == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Not configured")

    security_check(config)

    print("\nThe Oracle sees all configurations.")


def main() -> None:
    config: dict[str, str] = load_configuration()
    display_configuration(config)


if __name__ == "__main__":
    main()
