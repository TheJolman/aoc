package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	content, err := os.ReadFile("inputs/day01")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(string(content))
}
