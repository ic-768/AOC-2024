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

	sum := 0

	slices.Sort(slice1)
	slices.Sort(slice2)

	for index := range slice1 {
		sum += abs(slice1[index] - slice2[index])
	}

	fmt.Println(sum)

}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
