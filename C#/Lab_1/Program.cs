using System;
using System.IO;

namespace MyApp
{
    internal class Programm{

        static int ReadNumber(){
            // int a = Convert.ToInt32(Console.ReadLine());
            // int b = Convert.ToInt32(Console.ReadLine());

            int a = Console.Read();
            while (char.IsWhiteSpace((char)a)){

                a = Console.Read();
            }

            int n = 0;
            while (char.IsDigit((char)a))
            {
                n = n*10;
                n = n + (a - '0');
                a = Console.Read();
            }

            return n;
        }
        
        static void Main(string[] args){
            int a = ReadNumber();
            int b = ReadNumber();
            Console.WriteLine(a + b);
            // Console.ReadKey();
        }
    }
}