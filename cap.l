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