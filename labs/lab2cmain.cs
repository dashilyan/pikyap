using System;
class Program
{
	static void Main()
	{
		string str1 = Console.ReadLine();
		string str2 = Console.ReadLine();

		Console.WriteLine("Посимвольное сравнение: ", symb_compare(str1, str2));
		Console.WriteLine("Расстояние Левенштейна: ", levenshtein_distance(str1, str2));
	}
	static int symb_compare(string str1, string str2)
	{
		int num = Math.Abs(str1.Length - str2.Length);

		if (str1.Length > str2.Length)
		{
			for (int i = 0; i < str2.Length; i++)
			{
				if (str1[i] != str2[i])
				{
					num++;
				}
			}
		}
		else
		{
			for (int i = 0; i < str1.Length; i++)
			{
				if (str1[i] != str2[i])
				{
					num++;
				}
			}
		}

		return num;
	}
	static int levenshtein_distance(string s, string t)
	{
		int m = s.Length;
		int n = t.Length;
		int[,] d = new int[m + 1, n + 1];

		for (int i = 1; i <= m; i++)
		{
			d[i, 0] = i;
		}

		for (int j = 1; j <= n; j++)
		{
			d[0, j] = j;
		}

		for (int j = 1; j <= n; j++)
		{
			for (int i = 1; i <= m; i++)
			{
				int cost = (s[i - 1] == t[j - 1]) ? 0 : 1;
				d[i, j] = Math.Min(Math.Min(d[i - 1, j] + 1,      // удаление
											 d[i, j - 1] + 1),     // вставка
									d[i - 1, j - 1] + cost);    // замена
			}
		}

		return d[m, n];
	}
	static void print_mas(int[,]mas, int a, int b)
	{
		for (int i = 0; i < a; i++)
		{
			for (int j=0; j < b; j++)
			{
				Console.WriteLine(mas[i, j].ToString()," ");
			}
			Console.WriteLine("\n");
		}
	}
}