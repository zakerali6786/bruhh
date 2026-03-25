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