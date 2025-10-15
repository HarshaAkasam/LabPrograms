
%{
/* remove_whitespace.l - prints input without spaces, tabs, newlines */
%}
%%
[ \t\r\n]+    { /* skip whitespace */ }
.             { putchar(yytext[0]); }
%%
int main(){ yylex(); return 0; }
