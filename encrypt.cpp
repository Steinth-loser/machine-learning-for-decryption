#include <stdio.h>
#include <ctype.h>

int encryptChar(char letter) {
	if(isalpha(letter)) {
		if(islower(letter)) {
			return letter-'a' + 1;
		}
		else {
			return letter-'A' + 1;
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
	char input[10];
	int output[10];
	printf("Enter the string you want to encrypt: ");
	scanf("%s", input);
	
	encryptString(input, output);
	for(int i = 0; i < sizeof(output); i++){
		printf("\n%d", output[i]);
	}
	
	return 0;
}

