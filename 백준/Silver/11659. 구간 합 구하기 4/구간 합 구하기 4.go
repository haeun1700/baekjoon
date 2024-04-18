package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, m, i, j int
	fmt.Fscan(reader, &n, &m)
	var arr = make([]int, n + 2)
	for idx :=1; idx <= n; idx++ {
		fmt.Fscan(reader, &arr[idx])
		arr[idx] += arr[idx-1]
	}
	for idx:=0; idx<m; idx++ {
		fmt.Fscan(reader, &i, &j)
		fmt.Fprintln(writer, arr[j] - arr[i - 1])
	}
}
