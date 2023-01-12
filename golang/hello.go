package main
import "fmt"


func main() {

	var slice []int

	fmt.Println(len(slice))
	slices()
	return
	

}


func slices() {

	slice := []int{
		10,
		12,
	}

	
	fmt.Println("Это капасити->", cap(slice), "\n", "Это длинна->", len(slice))
	var slice2 []int = append(slice, 13, 14, 16)
	fmt.Println("Это капасити->", cap(slice2), "\n", "Это длинна->", len(slice2), slice2)

	return
}


