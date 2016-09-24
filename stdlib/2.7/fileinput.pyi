from typing import Iterable, Callable, IO, Union, Iterator

class FileInput(Iterable[str]):
    def __init__(
        self,
        files: Union[str, Iterable[str]]=None,
        inplace: bool=...,
        backup: str=...,
        bufsize: int=...,
        mode: str=...,
        openhook: Callable[[str, str], IO[str]]=...
        ) -> None: ...

    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, i) -> str: ...
    def next(self) -> str: ...
    def nextfile(self) -> None: ...
    def readline(self) -> str: ...
    def filename(self) -> Union[str, None]: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...

def input(
    files: Union[str, Iterable[str]]=None,
    inplace: bool=...,
    backup: str=...,
    bufsize: int=...,
    mode: str=...,
    openhook: Callable[[str, str], IO[str]]=...) -> FileInput: ...


def filename() -> Union[str, None]: ...
def lineno() -> int: ...
def filelineno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...
def nextfile() -> None: ...
def close() -> None: ...

def hook_compressed(filename: str, mode: str) -> IO[str]: ...
def hook_encoded(encoding: str) -> Callable[[str, str], IO[str]]: ...
