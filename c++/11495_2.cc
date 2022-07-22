#include <bits/stdc++.h>
using namespace std;

long long count1;

int array1[500005];
int array2[500005];

void mergesort(int *array, int len, int offset)
{
    if (len > 1)
    {
        int *first = array1 + offset;
        if (first == array)
            first = array2 + offset;
        
        for (int i = 0; i < len; ++i)
            first[i] = array[i];
        
        int firstLength = len / 2;
        int secondStart = firstLength, secondLength = len - secondStart;
        int *second = first + secondStart;
        
        mergesort(first, firstLength, offset);
        mergesort(second, secondLength, offset + secondStart);
        
        int i = 0, j = 0;
        int pos = 0;
        
        int currentCost = count1;
        
        while (i < firstLength && j < secondLength)
        {
            if (first[i] < second[j])
                array[pos++] = first[i++];
            else
            {
                array[pos++] = second[j++];
                count1 += firstLength - i;
                cout << count1 << " ";
            }
        }
        
        for (; i < firstLength; ++i, ++pos)
            array[pos] = first[i];
        for (; j < secondLength; ++j, ++pos)
            array[pos] = second[j];
    }
}

int main()
{
    ifstream cin("11495.txt");
    int N;
    
    while (cin >> N, N)
    {
        for (int i = 0; i < N; ++i)
            cin >> array1[i];
        
        mergesort(array1, N, 0);
          
        cout << (count1 % 2 ? "Marcelo\n" : "Carlos\n");
        count1 = 0;
    }
}