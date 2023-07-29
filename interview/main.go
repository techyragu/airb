package main

import (
	"fmt"
	"strings"
)

/*
Write a program to find the word frequencies for a given paragraph?

Extend the function to find the top 3 most frequently occurring words.
Take a TDD approach to this problem if possible. How much time do you need to finish this solution?

Paragraph - Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type specimen book.
 It has survived not only five centuries, but also the leap into electronic typesetting,
 remaining essentially unchanged.
 It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages
*/

func main() {
	var paragraph string = `Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
 when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
 It has survived not only five centuries, but also the leap into electronic typesetting, 
 remaining essentially unchanged. 
 It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages`

	words := strings.Split(paragraph, " ")
	wordCount := make(map[string]int)
	for _, word := range words {
		wordCount[word] += 1
	}

	fmt.Println(wordCount)

}
