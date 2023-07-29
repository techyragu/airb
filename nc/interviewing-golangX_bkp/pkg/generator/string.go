package generator

import (
	"math/rand"
	"strings"
	"time"
)

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

func RandomString() string {
	strLen := rand.Int31n(40)

	//var str string
	var b strings.Builder
	for i := 0; i <= int(strLen); i++ {
		b.WriteString(string(letterRunes[int(rand.Int31n(int32(len(letterRunes))))]))
		//str = str + string(letterRunes[int(rand.Int31n(int32(len(letterRunes))))])
	}
	return b.String()
}

func RandomDate() *time.Time {
	t := time.Date(rand.Intn(11)+2010, time.Month(rand.Intn(12)+1), rand.Intn(28), rand.Intn(23), rand.Intn(59), rand.Intn(59), rand.Intn(59), time.UTC)
	return &t
}
