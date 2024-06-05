package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	var qntRepeticoes int
	_, err := fmt.Scanln(&qntRepeticoes)
	if err != nil {
		fmt.Println(err)
	}
	for i := 0; i < qntRepeticoes; i++ {
		var input string
		var result, acrescimo int
		var listofstrings []string
		fmt.Fscan(os.Stdin, &input)
		listofstrings = strings.Fields(input)
		fmt.Println("Número de termos:", len(listofstrings))

		palavra1, palavra2 := listofstrings[0], listofstrings[1]
		num, err := strconv.Atoi(palavra1)
		if err != nil {
			fmt.Println(err)
		}
		if num > 45 {
			if num > 45 && palavra2 == "2T" {
				result = (math.Floor(float64(num)/45) * 45) + 45
				acrescimo = (num + 45) - 90
			}
			result = 45
			acrescimo = num - 45
		} else {
			if palavra2 == "2T" {
				result = num + 45
			}
			result = num
		}
		if acrescimo > 0 {
			fmt.Printf("%d+%d", result, acrescimo)
		} else {
			fmt.Println(result)
		}

	}
}
