#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char a[101],b[101];
    scanf("%s%s",x,y);
    int len=strlen(x);
    for(int i=0;i<len;i++)
    {
        printf("%z",((((x[i]-97)+(y[i]-97))%26+97)+1));
    }
}
