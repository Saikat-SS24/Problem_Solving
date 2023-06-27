#include<stdio.h>
#include <string.h>
char table[10][4]={{},{},{'a','b','c'},{'d','e','f'},{'g','h','i'},{'j','k','l'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y','z'}};
char each[10]={0,0,3,3,3,3,3,4,3,4};
int len;
int cnt;
char **ans;
char *gdigits;
void fun(int currdig,char *locans,char charcnt){
    if(currdig==len){
        locans[charcnt]='\0';
        ans[cnt]=malloc(sizeof(char)*9);
        strcpy(ans[cnt],locans);
        cnt++;
        return;
    }
    int num=gdigits[currdig]-'0';
    for(int i=0;i<each[num];i++){
        locans[charcnt]=table[num][i];
        fun(currdig+1,locans,charcnt+1);
    }
}
char ** letterCombinations(char * digits, int* returnSize){
    len=strlen(digits);
    *returnSize=1;
    for(int i=0;i<len;i++){
        *returnSize*=each[digits[i]-'0'];
    }
    gdigits=digits;
    cnt=0;
    ans=malloc(sizeof(char *)*(*returnSize));
    if(*returnSize==1){
        *returnSize=0;
        return NULL;
    }
    char locans[9]={'\0'};
    fun(0,locans,0);
    return ans;
}
