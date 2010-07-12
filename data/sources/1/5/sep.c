#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 100000
#define MIN -100000

int main(int argc, char** argv)
{
	char line[MAX_LEN];
	int cisla[100];
	int i, cislo=0, cisel=0;

	gets(line);
	line[strlen(line)] = ' ';
	for (i=0;i<strlen(line);i++) {
		if(line[i]!=' ') {
			cislo *= 10;
			cislo += (int) line[i]-48;
		} else {
			cisla[cisel] = cislo;
			cislo = 0;
			cisel++;
		}
	}

	int max = MIN;
	for(i=0;i<cisel;i++) {
		if (cisla[i]>max) {
			max = cisla[i];
		}
	}
	printf("%i", max);

	return 0;
}
