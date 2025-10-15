
/* Simple bison grammar (LALR) for arithmetic expressions */
%token NUM
%left '+' '-'
%left '*' '/'
%%
input: /* empty */
     | input line
     ;
line: '\n' 
    | exp '\n' { printf("= %d\n", $1); }
    ;
exp: NUM { $$ = $1; }
   | exp '+' exp { $$ = $1 + $3; }
   | exp '-' exp { $$ = $1 - $3; }
   | exp '*' exp { $$ = $1 * $3; }
   | exp '/' exp { $$ = $1 / $3; }
   | '(' exp ')' { $$ = $2; }
   ;
%%
int main(){ yyparse(); return 0; }
int yyerror(char *s){ fprintf(stderr,"error: %s\n",s); return 0; }
