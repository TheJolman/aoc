package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var lines []string

func main() {
	file, err := os.Open("inputs/day01")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	part1()
}

func part1() {
	password := 0
	dial := 50

	for _, line := range lines {
		direction := string(line[0])
		amount, _ := strconv.Atoi(string(line[1:]))
		switch direction {
		case "L":
			dial -= amount
		case "R":
			dial += amount
		}
	}
	fmt.Printf("Password: %d\n", password)
}
