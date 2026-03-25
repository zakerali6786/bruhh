%{
#include<stdio.h>
%}

%%
[aeiouAEIOU] { printf("Vowel\n"); }
[a-zA-Z]     { printf("Consonant\n"); }
.            { printf("Invalid\n"); }
%%

int main(){
    yylex();
    return 0;
}


flex table.l
gcc lex.yy.c -o table.exe
table.exe