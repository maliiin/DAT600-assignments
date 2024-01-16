package main

import (
	"fmt"
	"math/rand"
	"time"
)

func insertionSort(arr []int) int {
	steps := 0
	key := 1

	for key < len(arr) {
		steps++
		for i := 0; i < key; i++ {
			steps++
			if arr[key] < arr[i] {
				arrKey := arr[key]
				arr[key] = arr[i]
				arr[i] = arrKey
				steps += 3
			}
		}
		key++
	}

	return steps
}

func main() {
	// Example usage:
	sizes := []int{6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152}
	totTime := 0 * time.Second
	for _, size := range sizes {
		arr := generateRandomArray(size)

		// Measure execution time
		startTime := time.Now()

		steps := insertionSort(arr)

		// Calculate execution time
		elapsedTime := time.Since(startTime)
		totTime += elapsedTime
		fmt.Printf("Array size: %d\n", size)
		fmt.Println("Number of steps:", steps)
		fmt.Println("Execution Time:", elapsedTime)
		fmt.Println()

	}
	fmt.Println("Total time:", totTime)
}

func generateRandomArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		// Generate a random integer between 0 and 9
		arr[i] = rand.Intn(100)

	}
	return arr
}
