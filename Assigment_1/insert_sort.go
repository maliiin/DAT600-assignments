package main

import (
	"fmt"
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
	for _, size := range sizes {
		arr := generateRandomArray(size)

		// Measure execution time
		startTime := time.Now()

		steps := insertionSort(arr)

		// Calculate execution time
		elapsedTime := time.Since(startTime)

		fmt.Printf("Array size: %d\n", size)
		fmt.Println("Number of steps:", steps)
		fmt.Println("Execution Time:", elapsedTime)
		fmt.Println()
	}
}

func generateRandomArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i + 1 // Just an example, you can modify this based on your requirements
	}
	return arr
}
