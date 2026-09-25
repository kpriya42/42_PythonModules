#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVplugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []

        for _, value in data:
            values.append(value)

        print("CSV Output:")
        print(",".join(values))


class JSONplugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items: list[str] = []

        for rank, value in data:
            items.append(f'"item_{rank}": "{value}"')

        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


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
                print(f"DataStream error - Can't \
                      process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total = proc.rank + len(proc.data)
            remaining = len(proc.data)

            name = type(proc).__name__.replace("Processor", " Processor")

            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            export_data: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc.data:
                    break
                export_data.append(proc.output())

            plugin.process_output(export_data)


def ft_data_pipeline() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    # =======================================
    #   Initialize object & Display Stats
    # =======================================
    print("\nInitialize Data Stream...")
    ds_obj = DataStream()
    ds_obj.print_processors_stats()

    # =================================
    #   Register all 3 processors
    # =================================
    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    ds_obj.register_processor(num_proc)
    txt_proc = TextProcessor()
    ds_obj.register_processor(txt_proc)
    log_proc = LogProcessor()
    ds_obj.register_processor(log_proc)

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

    # =========================================
    #   Process a data stream & Display Stats
    # =========================================
    print(f"\nSend first batch of data on stream: {data_stream}")
    ds_obj.process_stream(data_stream)
    ds_obj.print_processors_stats()

    # =========================================
    #   Export the data stream to CSV plugin
    #            & Display Stats
    # =========================================
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds_obj.output_pipeline(3, CSVplugin())
    ds_obj.print_processors_stats()

    # ==========================================
    #   Process new data stream & Display Stats
    # ==========================================
    data_stream2 = [21,
                    ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                    [
                        {
                            'log_level': 'ERROR',
                            'log_message': '500 server crash'
                        },
                        {
                            'log_level': 'NOTICE',
                            'log_message': 'Certificate expires in 10 days'
                        }
                    ],
                    [32, 42, 64, 84, 128, 168],
                    'World hello']
    print(f"\nSend another batch of data: {data_stream2}")
    ds_obj.process_stream(data_stream2)
    ds_obj.print_processors_stats()

    # =============================================
    #   Export the new data stream to JSON plugin
    #            & Display Stats
    # =============================================
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds_obj.output_pipeline(5, JSONplugin())
    ds_obj.print_processors_stats()


if __name__ == "__main__":
    ft_data_pipeline()
