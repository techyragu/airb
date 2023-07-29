package main

import "testing"

func TestAdd(t *testing.T) {
	got := add(7, 5)
	want := 12

	if got != want {
		t.Errorf("got: %q, want: %q", got, want)
	}
}
