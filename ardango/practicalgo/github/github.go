package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type user struct {
	Name         string
	Public_Repos int
}

func githubInfo(login string) (string, int) {

	resp, err := http.Get(login)
	if err != nil {
		log.Fatalf("err: %v", err)
	}
	if resp == nil {
		log.Fatal("No Response")
	}
	//fmt.Println(io.Copy(os.Stdout, resp.Body))

	var u user
	decode := json.NewDecoder(resp.Body)
	if err := decode.Decode(&u); err != nil {
		log.Fatalf("Failed to decode. Err %v", err)
	}
	return u.Name, u.Public_Repos
}

func main() {
	fmt.Println("In Main")
	url := "https://api.github.com/users/techyragu"
	name, repos := githubInfo(url)
	fmt.Printf("Name: %#v, Repos: %#v", name, repos)
}
