package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	slice1 := []int{}
	slice2 := []int{}

	for scanner.Scan() {
		text := scanner.Text()
		numbers := strings.Fields(text)

		leftNumber, _ := strconv.Atoi(numbers[0])
		rightNumber, _ := strconv.Atoi(numbers[1])

		slice1 = append(slice1, leftNumber)
		slice2 = append(slice2, rightNumber)
	}

	similarity := 0

	slices.Sort(slice1)
	slices.Sort(slice2)

	for index := range slice1 {
		left_element := slice1[index]
		occurrences := count_occurrences(left_element, slice2)
		similarity += left_element * occurrences
	}

	fmt.Println(similarity)

}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func count_occurrences(element int, slice []int) int {
	occurrences := 0

	for _, value := range slice {
		if value == element {
			occurrences++
		}
	}
	return occurrences
}
