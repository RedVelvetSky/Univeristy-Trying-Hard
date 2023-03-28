using System;
using System.Linq;
using System.Collections.Generic;

namespace WaterJugProblem
{
    internal class Program
    {
        public static string[] ReadNumbers()
        {
            // Read a line of input from the console
            string input = Console.ReadLine();

            // Split the input into individual numbers
            string[] numbers = input.Split(' ');

            return numbers;
        }

        public static string[] DeleteEmptyCells(string[] arr)
        {
            // Using LINQ to filter the array
            string[] filteredArr = arr.Where(s => !string.IsNullOrWhiteSpace(s)).ToArray();

            return filteredArr;
        }

        static void Main(string[] args)
        {
            // Reading numbers
            string[] numbers = ReadNumbers();
            numbers = DeleteEmptyCells(numbers);

            // Convert each number to an integer
            int a = Convert.ToInt16(numbers[0]);
            int b = Convert.ToInt16(numbers[1]);
            int c = Convert.ToInt16(numbers[2]);
            int x = Convert.ToInt16(numbers[3]);
            int y = Convert.ToInt16(numbers[4]);
            int z = Convert.ToInt16(numbers[5]);
            int maxVolume = a + b + c;

            // Creating a list with the initial volumes
            List<int> initialVolumes = new List<int>() {x, y, z}; 

            // Creating a hash set to keep track of the visited states
            HashSet<int> visitedVolumes = new HashSet<int>(); 

            // Creating a dictionary to keep track of the minimum number of transfers reach each possible volume
            Dictionary<int, int> minTransfers = new Dictionary<int, int>(); 

            // Creating a queue to store the states that need to be explored
            Queue<Tuple<List<int>, int>> volumesToCheck = new Queue<Tuple<List<int>, int>>(); 
 
            volumesToCheck.Enqueue(Tuple.Create(initialVolumes, 0)); 
 
            while (volumesToCheck.Count > 0) 
            { 
                var current = volumesToCheck.Dequeue(); 
                var currentVolumes = current.Item1; 
                var currentTransfers = current.Item2;

                // keeping track of which volumes have already been visited
                var hash = currentVolumes[0] * 100 + currentVolumes[1] * 10 + currentVolumes[2];

                if (!visitedVolumes.Contains(hash)) 
                { 
                    visitedVolumes.Add(hash); 
 
                    // finding a valid volume from the current volumes
                    var volume = currentVolumes.Find(v => v >= 0 && v <= a + b + c && (v % a == 0 || v % b == 0 || v % c == 0));

                    // adding a new key-value pair if the key volume does not exist
                    if (!minTransfers.ContainsKey(volume)) 
                    { 
                        minTransfers[volume] = currentTransfers; 
                    }
                    
                    for (int i = 0; i < 3; i++) 
                    { 
                        for (int j = 0; j < 3; j++) 
                        { 
                            if (i != j) 
                            { 
                                var nextVolumes = new List<int>(currentVolumes);
                                var transfer = Math.Min(currentVolumes[i], a + b + c - currentVolumes[j]);

                                nextVolumes[i] -= transfer; 
                                nextVolumes[j] += transfer; 

                                volumesToCheck.Enqueue(Tuple.Create(nextVolumes, currentTransfers + 1)); 
                            } 
                        } 
                    } 
                } 
            }


            // // Iterating through the minTransfers and print out each volume along with its minimum number of pours
            // // Iterating through the minTransfers and print out each volume along with its minimum number of pours
            bool reachable = false;
            for (int i = 0; i <= maxVolume; i++) 
            { 
                if (minTransfers.ContainsKey(i)) 
                { 
                    reachable = true;
                    Console.Write(i + ":" + minTransfers[i] + " "); 
                } 
            }
            if (!reachable)
            {
                Console.Write("impossible");
            }

        }
    }
}
            
        
    

