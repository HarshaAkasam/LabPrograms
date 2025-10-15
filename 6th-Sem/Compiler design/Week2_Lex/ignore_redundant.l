
%{
/* ignore_redundant.l - scanner that ignores redundant spaces, tabs, newlines and prints tokens */
%}
ID      [A-Za-z_][A-Za-z0-9_]*
NUM     [0-9]+
%%
{ID}        { printf("ID(%s) ", yytext); }
{NUM}       { printf("NUM(%s) ", yytext); }
";"         { printf("SEMICOLON "); }
[ \t\n\r]+  { /* ignore */ }
.           { printf("SYM(%s) ", yytext); }
%%
int main(){ yylex(); return 0; }
