package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Reply struct {
	Name  string `json:"name"`
	Repos int    `json:"public_repos"`
}

func main() {
	url := "https://api.github.com/users/techyragu"
	resp, err := http.Get(url)
	if err != nil {
		log.Fatalf("Unable to Fetch %s. Err: %s", url, err)
	}

	if resp.StatusCode != http.StatusOK {
		log.Fatalf("Failed to Fetch %s. Code: %d", url, resp.StatusCode)
	}
	defer resp.Body.Close()

	//io.Copy(os.Stdout, resp.Body)

	var repo Reply
	decoder := json.NewDecoder(resp.Body)
	decoder.Decode(&repo)

	fmt.Println(repo)

}
