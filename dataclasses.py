from typing import ForwardRef

# Define a forward reference to the `dataclass` class.
dataclass = ForwardRef('dataclass')

from dataclasses import dataclass

@dataclass(frozen=True,order=True)
class Comment:
    id:str
    user:str
    text:str


def main():
    Comment = Comment(1,'siddh','hello world')
    print(Comment)
    print(astuple(Comment))
    print(asdict(Comment))

if __name__ == __main__ :
    main()