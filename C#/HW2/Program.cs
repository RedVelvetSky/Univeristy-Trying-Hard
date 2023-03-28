using System;

class Program
{
    static void Main(string[] args)
    {
        // Console.Write("Enter an integer greater than 1: ");
        int n = int.Parse(Console.ReadLine());

        Console.Write($"{n}=");
        for (int i = 2; i <= n; i++)
        {
            while (n % i == 0)
            {
                Console.Write(i);
                n /= i;

                if (n != 1)
                {
                    Console.Write("*");
                }
            }
        }
    }
}