%{
#include<stdio.h>
%}

%%
[0-9]+"."[0-9]+ { printf("Valid Real Number\n"); }
.               { printf("Invalid\n"); }
%%

int main(){
    yylex();
    return 0;
}


flex table.l
gcc lex.yy.c -o table.exe
table.exe