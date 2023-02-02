# Overview

Out of the four topics we were given, we decided to explore context-free grammar and its application using programming languages. We explored multiple possible directions for our project, and ended up focusing on parsing with the context-free grammars we created. We chose this route as it gave us practical experience, allowing us to leverage our understanding of the topics we learned in class to create solutions to real-world problems. 

# Example with Lark

See directory `./lark-example`.

## Usage

A CI tool that parses and interprets a DSL (Domain-Specific Language) called turtle. Start with:

```bash
$ python lark-example/LarkProgram.py
```

This opens a shell to input turtle commands. The grammar for the language is in `./lark-example/turtle_grammar.lark`. For instance, entering `f 100` draws a line forward by 100 pixels.

## Error Handling

If the input does not make logical sense to the parser, it will recognize this and throw an error.
