#include <stdio.h>
#include <ctype.h>

int encryptChar(char letter) {
	if(isalpha(letter)) {
		if(islower(letter)) {
			return letter-'a';
		}
		else {
			return letter-'A';
		}
		}
	return -1;
	}
	
	

void encryptString(const char* input, int* output) {
	int i = 0;
	while (input[i] != '\0') {
		output[i] = (encryptChar(input[i]) - 1) * (encryptChar(input[i]) + 1);
		i++;
	}
	
	
}

int main() {
	char input[100];
	int output[100];
	printf("Enter the string you want to encrypt: ");
	scanf("%s", input);
	
	encryptString(input, output);
	int i = 0;
	while (output[i] != '\0') {
		printf("%d\n", output[i]);
		i++;
	}
	
	return 0;
}

