from abc import ABC, abstractmethod


class ReadWriteCloser(ABC):
    @abstractmethod
    async def read(self) -> bytes:
        ...

    @abstractmethod
    async def write(self, data: bytes) -> None:
        ...

    @abstractmethod
    async def close(self) -> None:
        ...


class BaseSession(ABC):
    @abstractmethod
    def open(self) -> ReadWriteCloser:
        ...

    @abstractmethod
    def accept(self) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def go_away(self) -> bytes:
        ...

    @abstractmethod
    def ping(self) -> bytes:
        ...


class BaseStream(ReadWriteCloser):
    @abstractmethod
    def set_read_deadline(self) -> None:
        ...

    @abstractmethod
    def set_write_deadline(self) -> None:
        ...
