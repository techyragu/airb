package read

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func ReadFile(fileName string) {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("Unable to open file %s", fileName)
	}
	defer file.Close()

	s := bufio.NewScanner(file)
	for s.Scan() {
		fmt.Println(s.Text())
	}
}
