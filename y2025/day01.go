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

	switch os.Args[1] {
	case "1":
		part1()
	case "2":
		part2()
	}
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
		if dial%100 == 0 {
			password++
		}
	}
	fmt.Printf("Password: %d\n", password)
}

func part2() {
	password := 0
	dial := 50

	for _, line := range lines {
		prevPos := dial

		direction := string(line[0])
		amount, _ := strconv.Atoi(string(line[1:]))
		switch direction {
		case "L":
			dial -= amount
		case "R":
			dial += amount
		}

		diff := dial - prevPos
		timesCrossedZero := diff / 100 * 100
		if timesCrossedZero < 0 {
			timesCrossedZero *= -1
		}

		password += timesCrossedZero
	}

	fmt.Printf("Password: %d\n", password)
}
