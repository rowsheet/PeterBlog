// type_saftey.go
package main

import "fmt"

func main() {
	foo := "I'm a string!"

	fmt.Println("foo (1):")
	fmt.Println(foo)

	foo += 1
	fmt.Println("foo (2):")
	fmt.Println(foo)
}
