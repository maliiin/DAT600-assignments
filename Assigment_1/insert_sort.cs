using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // Create an array for testing
        int[] arrayToSort = {6,2,4,1,3,5};

        // Measure the execution time
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();

        // Call your sorting function
        int steps = InsertionSort(arrayToSort);

        // Stop the stopwatch
        stopwatch.Stop();

        // Display the results
        Console.WriteLine("Sorted array: " + string.Join(", ", arrayToSort));
        Console.WriteLine("Number of steps: " + steps);
        Console.WriteLine("Execution time: " + stopwatch.Elapsed);
    }

    static int InsertionSort(int[] arr)
    {
        int key = 1;
        int steps = 0;

        while (key < arr.Length)
        {
            steps++;
            for (int i = 0; i < key; i++)
            {
                steps++;
                if (arr[key] < arr[i])
                {
                    int temp = arr[key];
                    arr[key] = arr[i];
                    arr[i] = temp;
                    steps += 3;
                }
            }
            steps++;
            key++;
        }

        return steps;
    }
}
