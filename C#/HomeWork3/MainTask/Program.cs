using System;
using System.Collections.Generic;

namespace ChessProblem
{
    class Program
    {   
        // two-dimensional 8 by 8 array named grid
        static int[,] grid = new int[8, 8];

        static void Main(string[] args)
        {
            // number of obstacles that will be added to the board
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                // reads input and splits it into an array of strings
                string[] obstacle = Console.ReadLine().Split(' ');

                // converts 1 and 2 elements to an integer. Then subtracts 1, since the grid is zero-indexed but the coordinates are one-indexed (first row and column of the grid are 0,0 rather than 1,1).
                int x = Convert.ToInt32(obstacle[0]) - 1;
                int y = Convert.ToInt32(obstacle[1]) - 1;

                // represents an obstacle on the chessboard
                grid[x, y] = -1;
            }

            // reads input and splits it into an array of strings
            string[] start = Console.ReadLine().Split(' ');

            // converts 1 and 2 elements to an integer. Then subtracts 1, since the grid is zero-indexed but the coordinates are one-indexed (first row and column of the grid are 0,0 rather than 1,1).
            int startX = Convert.ToInt32(start[0]) - 1;
            int startY = Convert.ToInt32(start[1]) - 1;

            // sets the starting position of the king to 0
            grid[startX, startY] = 0;

            // reads input and splits it into an array of strings
            string[] end = Console.ReadLine().Split(' ');

            // converts 1 and 2 elements to an integer. Then subtracts 1, since the grid is zero-indexed but the coordinates are one-indexed (first row and column of the grid are 0,0 rather than 1,1).
            int endX = Convert.ToInt32(end[0]) - 1;
            int endY = Convert.ToInt32(end[1]) - 1;

            int minSteps = FindMinimalSteps(startX, startY, endX, endY);

            Console.WriteLine(minSteps);
        }

        static int FindMinimalSteps(int startX, int startY, int endX, int endY)
        {
            // initialize a queue to store the moves that are being made
            Queue<int> moves = new Queue<int>();

            // enqueuing starting x and y
            moves.Enqueue(startX);
            moves.Enqueue(startY);

            // used to store the possible moves of the king
            int moveX = -1;
            int moveY = -1;

            // loop to bfs until the destination (endX, endY) is reached, or until there are no more moves to make
            while (moves.Count > 0 && (moveX != endX || moveY != endY))
            {
                moveX = moves.Dequeue();
                moveY = moves.Dequeue();

                // two loops iterate through each of the eight possible moves that a king can make from the current position (x, y)
                for (int offsetX = -1; offsetX <= 1; offsetX++)
                {
                    // loop iterates three times, for -1, 0 and 1, covering all the possible offsets that a king can make in a single move
                    for (int offsetY = -1; offsetY <= 1; offsetY++)
                    {
                        // skip 0 offset
                        if (offsetX == 0 && offsetY == 0)
                        {
                            continue;
                        }

                        // coordinates of the next potential move of the king
                        // moves.Enqueue(startX);
                        // moveX = moves.Dequeue();
                        int newX = moveX + offsetX;
                        int newY = moveY + offsetY;

                        // checks whether the new position within the board boundaries and there is no obstacle at that position
                        if (newX >= 0 && newX < 8 && newY >= 0 && newY < 8 && grid[newX, newY] != -1)
                        {
                            // checks if the new square is reachable and has not been visited before
                            if (grid[newX, newY] == 0)
                            {
                                // update its distance value in the grid and add it to the queue of squares to be visited later
                                grid[newX, newY] = grid[moveX, moveY] + 1;
                                moves.Enqueue(newX);
                                moves.Enqueue(newY);
                            }

                            // checks if the new square has already been visited but the current path to it is shorter than the previously calculated path
                            else if (grid[moveX, moveY] + 1 < grid[newX, newY])
                            {
                                // update the distance and add it to the queue again
                                grid[newX, newY] = grid[moveX, moveY] + 1;
                                moves.Enqueue(newX);
                                moves.Enqueue(newY);
                            }
                        }
                    }
                }
            }

            return grid[endX, endY] == 0 ? -1 : grid[endX, endY];
        }
    }
}
