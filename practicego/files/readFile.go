package main

import (
	"bytes"
	"files/read"
)

func main() {
	// file, err := os.Open("test.txt")
	// if err != nil {
	// 	log.Fatalf("error: %v", err)
	// }
	// defer file.Close()

	// scanner := bufio.NewScanner(file)

	// for scanner.Scan() {
	// 	fmt.Println(scanner.Text()) // Read line by line
	// }

	// if err := scanner.Err(); err != nil {
	// 	fmt.Println("Error scanning file. ", err)
	// }

	read.ReadFile("test.txt")
	var b bytes.Buffer

}
