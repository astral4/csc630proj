'''
A parser for simple appraisals.

<expr> ::= <appraisal> | <antiappraisal>

<antiappraisal> ::= <not> <appraisal>
<not> ::= "not "

<appraisal> ::= <positive> | <negative>
<positive> ::= "good" | "excellent"
<negative> ::= "bad" | "terrible"
'''

from typing import Generator

Parser = Generator[tuple[bool | None, int], None, None]

def positive(input: str, start: int) -> Parser:
    if input[start:].startswith("good"):
        yield (True, start + len("good"))
    if input[start:].startswith("excellent"):
        yield (True, start + len("excellent"))

def negative(input: str, start: int) -> Parser:
    if input[start:].startswith("bad"):
        yield (True, start + len("bad"))
    if input[start:].startswith("terrible"):
        yield (True, start + len("terrible"))

def negate(input: str, start: int) -> Parser:
    if input[start:].startswith("not "):
        yield (None, start + len("not "))

def appraisal(input: str, start: int) -> Parser:
    for parse in positive(input, start):
        yield parse
    for parse in negative(input, start):
        yield parse

def antiappraisal(input: str, start: int) -> Parser:
    for _, not_end in negate(input, start):
        for value, appraisal_end in appraisal(input, not_end):
            yield (not value, appraisal_end)

def expr(input: str, start: int) -> Parser:
    for parse in appraisal(input, start):
        yield parse
    for parse in antiappraisal(input, start):
        yield parse

if __name__ == "__main__":
    print(list(expr("not excellent but good", 0)))