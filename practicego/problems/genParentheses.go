package main

func generateParenthesis(A int) []string {
	var ans []string
	solve(A, &ans, "", 0, 0)
	return ans
}

func solve(pairs int, ans *[]string, pair string, ob int, cb int) {
	if len(pair) == 2*pairs {
		*ans = append(*ans, pair)
		return
	}

	if ob < pairs {
		solve(pairs, ans, pair+"(", ob+1, cb)
	}

	if cb < ob {
		solve(pairs, ans, pair+")", ob, cb+1)
	}

}
