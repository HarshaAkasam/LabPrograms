
%{
/* patterns.l - identify integers, identifiers, keywords, operators */
%}
DIGIT   [0-9]
ID      [A-Za-z_][A-Za-z0-9_]*
%%
"if"            { printf("KEYWORD_IF\n"); }
"else"          { printf("KEYWORD_ELSE\n"); }
{ID}            { printf("IDENT(%s)\n", yytext); }
{DIGIT}+        { printf("INT(%s)\n", yytext); }
[+\-*/=]        { printf("OP(%s)\n", yytext); }
[ \t\r\n]+      { /* ignore whitespace */ }
.               { printf("UNKNOWN(%s)\n", yytext); }
%%
int main(){ yylex(); return 0; }
