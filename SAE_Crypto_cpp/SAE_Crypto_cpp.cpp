#include <time.h>
#include <vector>
#include <string>
#include <iostream>
//CPU optimisation

#include <emmintrin.h>
#include <wmmintrin.h>
#include <smmintrin.h>
#include <tmmintrin.h>
#include <immintrin.h>


using namespace std;

//split a list into n blocks

vector<vector<int>> split_list(vector<int> a_list, int n)
{
	vector<vector<int>> liste;
	for (int i = 0; i < a_list.size(); i += n)
	{
		vector<int> temp;
		for (int j = i; j < i + n; j++)
		{
			temp.push_back(a_list[j]);
		}
		liste.push_back(temp);
	}

	if (a_list.size() % n != 0)
	{
		for (int i = a_list.size() % n; i < n; i++)
		{
			liste[liste.size() - 1].push_back(0);
		}
	}
	return liste;
}

//multiply a list of list with a matrix

vector<vector<int>> multiply_list_matrix(vector<vector<int>> liste, vector<vector<int>> matrix)
{
	vector<vector<int>> result;
	for (int i = 0; i < liste.size(); i++)
	{
		vector<int> temp;
		for (int j = 0; j < matrix.size(); j++)
		{
			int sum = 0;
			for (int k = 0; k < matrix.size(); k++)
			{
				sum += liste[i][k] * matrix[j][k];
			}
			temp.push_back(sum % 26);
		}
		result.push_back(temp);
	}
	return result;
}

/*
#unsplit a list of list into a list
def unsplit_list(liste) :
	result = []
	for i in range(len(liste)) :
		for j in range(len(liste[i])) :
			result.append(liste[i][j])
			return result
*/

//unsplit a list of list into a list

vector<int> unsplit_list(vector<vector<int>> liste)
{
	vector<int> result;
	for (int i = 0; i < liste.size(); i++)
	{
		for (int j = 0; j < liste[i].size(); j++)
		{
			result.push_back(liste[i][j]);
		}
	}
	return result;
}

//convert a string to a list of int

vector<int> string_to_list(string s)
{
	vector<int> liste;
	for (int i = 0; i < s.size(); i++)
	{
		liste.push_back(s[i] - 'A');
	}
	return liste;
}


char num_to_char(int num)
{
	return num + 64;
}


vector<vector<vector<int>>> create_matrix_list(int start = 1, int end = 26)
{
	vector<vector<vector<int>>> liste;
	for (int i = 1; i < 26; i++)
	{
		for (int j = 1; j < 26; j++)
		{
			for (int k = 1; k < 26; k++)
			{
				for (int l = 1; l < 26; l++)
				{
					vector<vector<int>> temp;
					vector<int> temp1;
					temp1.push_back(i);
					temp1.push_back(j);
					temp.push_back(temp1);
					vector<int> temp2;
					temp2.push_back(k);
					temp2.push_back(l);
					temp.push_back(temp2);
					liste.push_back(temp);
				}
			}
		}
	}
	return liste;
}


/*
#list of all multiplications of a list of matrix by a text

def list_cipher(liste_text, matrix_list):
	#same but with a lambda map and numpy

	result = list(map(lambda x: multiply_list_matrix(liste_text, x), matrix_list))
	result = list(map(lambda x: unsplit_list(x), result))
	result = list(map(lambda x: list(map(lambda y: num_to_char(y), x)), result))
	result = list(map(lambda x: "".join(x), result))

	return result

*/

//list of all multiplications of a list of matrix by a text

vector<string> list_cipher(vector<vector<int>> liste_text, vector<vector<vector<int>>> matrix_list)
{
	vector<string> result;
	for (int i = 0; i < matrix_list.size(); i++)
	{
		vector<vector<int>> temp = multiply_list_matrix(liste_text, matrix_list[i]);
		vector<int> temp2 = unsplit_list(temp);
		string temp3;
		for (int j = 0; j < temp2.size(); j++)
		{
			temp3 += num_to_char(temp2[j]);
		}
		result.push_back(temp3);
	}
	return result;
}



void main() {
	
	/*
	print("CPU count: ", multiprocessing.cpu_count())
    print("Normal Hill Cipher")
    start_time = time.time()
    texte = "NWZN"
    liste_texte = [ord(i) - 64 for i in texte]
    texte_splitted = split_list(liste_texte, 2)
    #transfort to a np array
    texte_splitted = np.array(texte_splitted)
    matrix_list = create_matrix_list()
    liste_cipher = list_cipher(texte_splitted, matrix_list)
	*/

	//calculate computational time

	clock_t start_time = clock();
	string texte = "NWZN";
	vector<int> liste_texte = string_to_list(texte);
	vector<vector<int>> texte_splitted = split_list(liste_texte, 2);
	vector<vector<vector<int>>> matrix_list = create_matrix_list();
	vector<string> liste_cipher = list_cipher(texte_splitted, matrix_list);

	//print the result
	
	for (int i = 0; i < liste_cipher.size(); i++)
	{
		cout << liste_cipher[i] << endl;
	}
	
	
	
	
	
	
	
    return;
}