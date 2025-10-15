
/* Simple JFlex specification - tokens for identifiers and numbers */
%%
%class SimpleScanner
%unicode
%public
%standalone
%%
[ \t\r\n]+               { /* skip whitespace */ }
"if"                    { return sym.IF; }
"else"                  { return sym.ELSE; }
[A-Za-z_][A-Za-z0-9_]*   { return sym.ID; }
[0-9]+                  { return sym.NUM; }
.                       { /* ignore unknown */ }
