// not_dynamic.go
package main

import "fmt"

func main() {
	foo := 100
	fmt.Println("foo (1):")
	fmt.Println(foo)
	foo = "not I'm a string!"
	fmt.Println("foo (2):")
	fmt.Println(foo)
}
