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

    def ingest(self, data: int | float | list[int | float]) -> None:
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

    def validate_log_dict(self, log: dict[Any, Any]) -> bool:
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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            result: bool = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    result = True
                    break
            if not result:
                print(f"DataStream error - Can't process element "
                      f"in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total = proc.rank + len(proc.data)
            remaining = len(proc.data)

            name = type(proc).__name__.replace("Processor", " Processor")

            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def ft_data_stream() -> None:
    print("=== Code Nexus - Data Stream ===")

    # =======================================
    #   Initialize object & Display Stats
    # =======================================
    print("\nInitialize Data Stream...")
    ds_obj = DataStream()
    ds_obj.print_processors_stats()

    # ==================================================
    #   Register Numeric processor, process a data
    #              stream & Display Stats
    # ==================================================
    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    ds_obj.register_processor(num_proc)

    data_stream = ['Hello world',
                   [3.14, -1, 2.71],
                   [
                      {
                          'log_level': 'WARNING',
                          'log_message': 'Telnet access! Use ssh instead'
                      },
                      {
                          'log_level': 'INFO',
                          'log_message': 'User wil is connected'
                      }
                    ],
                   42,
                   ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {data_stream}")
    ds_obj.process_stream(data_stream)
    ds_obj.print_processors_stats()

    # ==============================================
    #   Register Text and Log processors, process
    #   same Data Stream again & Display Stats
    # ==============================================
    print("\nRegistering other data Processors")
    txt_proc = TextProcessor()
    ds_obj.register_processor(txt_proc)
    log_proc = LogProcessor()
    ds_obj.register_processor(log_proc)

    print("Send the same batch again")
    ds_obj.process_stream(data_stream)
    ds_obj.print_processors_stats()

    # ==========================================
    #      Consume elements & Display Stats
    # ==========================================
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(3):
        txt_proc.output()
    for _ in range(1):
        log_proc.output()
    ds_obj.print_processors_stats()


if __name__ == "__main__":
    ft_data_stream()
