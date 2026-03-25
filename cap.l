%{
#include<stdio.h>
#include<ctype.h>
%}

%%
"//".* {
    for(int i=0; yytext[i]; i++)
        putchar(toupper(yytext[i]));
}
.|\n { printf("%s", yytext); }
%%

int main(){
    yylex();
    return 0;
}



flex table.l
gcc lex.yy.c -o table.exe
table.exe