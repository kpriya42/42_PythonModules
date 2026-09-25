#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.data: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data available")
        value = self.data.pop(0)
        rank = self.rank
        self.rank += 1
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for num in data:
                if not isinstance(num, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int] |
               list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for num in data:
                self.data.append(str(num))
        else:
            self.data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for txt in data:
                if not isinstance(txt, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for txt in data:
                self.data.append(txt)
        else:
            self.data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.validate_log_dict(data)
        if isinstance(data, list):
            for log_entry in data:
                if not isinstance(log_entry, dict):
                    return False
                if not self.validate_log_dict(log_entry):
                    return False
            return True
        return False

    def validate_log_dict(self, log: dict[str, str]) -> bool:
        if not isinstance(log.get("log_level"), str) or \
                not isinstance(log.get("log_message"), str):
            return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for log_entry in data:
                self.data.append(self.to_string(log_entry))
        else:
            self.data.append(self.to_string(data))

    def to_string(self, log: dict[str, str]) -> str:
        if "log_level" in log and "log_message" in log:
            return f"{log['log_level'].strip()}: {log['log_message']}"
        return str(log)


def ft_data_processor() -> None:
    print("=== Code Nexus - Data Processor ===")

    # ==================================
    #      Testing Numeric Processor
    # ==================================
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()

    print(f"Trying to validate input '42': {num.validate(42)}")
    print("Trying to validate input 'Hello': "
          f"{num.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' "
          "without prior validation:")
    try:
        num.ingest("foo")  # type: ignore[arg-type]
    except Exception as e:
        print(f"  Got Exception!!! {e}")

    num_list = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_list}")
    num.ingest(num_list)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f"Numeric value {rank}: {value}")

    # ===============================
    #      Testing Text Processor
    # ===============================
    print("\nTesting Text Processor...")

    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")

    text_list = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_list}")
    text.ingest(text_list)

    print("Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f"Text value {rank}: {value}")

    # ===============================
    #     Testing Log Processor
    # ===============================
    print("\nTesting Log Processor...")

    log = LogProcessor()
    print("Trying to validate input 'Hello': "
          f"{log.validate('Hello')}")

    log_list = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print(f"Processing data: {log_list}")
    log.ingest(log_list)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    ft_data_processor()
