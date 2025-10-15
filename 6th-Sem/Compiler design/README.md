Compiler Course — Week-wise deliverables
Structure:
- Week1..Week12 directories with source files, scripts, PlantUML diagrams and sample inputs.
How to use (high level):
- Lex/flex files (.l): use `flex file.l` then `gcc lex.yy.c -lfl -o lexer` to compile and run: `./lexer < input.txt`
- JFlex (.jflex) files: use JFlex tool (Java) to generate scanner.
- Bison/Yacc (.y): use `bison -d file.y` then `gcc file.tab.c -o parser -ly -ll` (depending on system) or `bison -d` and `flex` combo.
- PlantUML (.puml): render diagrams with PlantUML (`plantuml file.puml`) to produce PNG/SVG.
- Python scripts: run with `python3 script.py`

Files included are small, well-commented, and intended as executable samples/demos for each week's tasks.
