using System;
using System.Collections.Generic;
using System.Linq;

namespace CityPartition
{
    class Program
    {
        static List<int>[] adjacencyList;
        static int[] group;

        static bool DFS(int city, int currentGroup)
        {
            group[city] = currentGroup;
            bool validPartition = true;

            foreach (int neighbor in adjacencyList[city])
            {
                if (group[neighbor] == 0)
                {
                    validPartition &= DFS(neighbor, 3 - currentGroup);
                }
                else if (group[neighbor] == currentGroup)
                {
                    return false;
                }
            }

            return validPartition;
        }

        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            int M = int.Parse(Console.ReadLine());

            adjacencyList = new List<int>[N + 1];
            group = new int[N + 1];

            for (int i = 1; i <= N; i++)
            {
                adjacencyList[i] = new List<int>();
            }

            for (int i = 0; i < M; i++)
            {
                int[] road = Console.ReadLine().Split().Select(int.Parse).ToArray();
                adjacencyList[road[0]].Add(road[1]);
                adjacencyList[road[1]].Add(road[0]);
            }

            bool partitionExists = DFS(1, 1);

            for (int i = 2; i <= N && partitionExists; i++)
            {
                if (group[i] == 0)
                {
                    partitionExists &= DFS(i, 1);
                }
            }

            if (partitionExists)
            {
                Console.WriteLine(string.Join(" ", Enumerable.Range(1, N).Where(city => group[city] == 1)));
                Console.WriteLine(string.Join(" ", Enumerable.Range(1, N).Where(city => group[city] == 2)));
            }
            else
            {
                Console.WriteLine("Nelze");
            }
        }
    }
}