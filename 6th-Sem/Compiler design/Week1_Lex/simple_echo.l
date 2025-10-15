
%{
/* simple_echo.l - echo input to output using lex */
%}
%%
.   { ECHO; }
\n  { ECHO; }
%%
int main(int argc, char **argv){
  yylex();
  return 0;
}
