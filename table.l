%{
#include<stdio.h>
%}

%option noyywrap
%option yylineno

%%
"if"|"for"|"while"|"return"|"printf"  
{ printf("%-10d %-15s %-15s\n", yylineno, yytext, "KEYWORD"); }

[0-9]+  
{ printf("%-10d %-15s %-15s\n", yylineno, yytext, "NUMBER"); }

[a-zA-Z]+  
{ printf("%-10d %-15s %-15s\n", yylineno, yytext, "IDENTIFIER"); }

[+*/=-]  
{ printf("%-10d %-15s %-15s\n", yylineno, yytext, "OPERATOR"); }

[(){};<>]  
{ printf("%-10d %-15s %-15s\n", yylineno, yytext, "SPECIAL"); }

[ \t\n] ;
. ;
%%

int main(){
    printf("%-10s %-15s %-15s\n","LINE","LEXEME","TOKEN");
    printf("-------------------------------------------------\n");
    yylex();
}