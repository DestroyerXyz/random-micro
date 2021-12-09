//SPDX-License-Identifier: MIT

package main

import (
	"fmt"
	"os"
	"strconv"
)

var retries int

// Print fuel left
func fuelGauge(fuel float64, startingFuel float64) {
	if fuel != startingFuel {
		fmt.Printf("Fuel Remaining: %v million litres\n", fuel)
	}
}

// Ask user for amount of fuel to start with
func inputStartingFuel() float64 {
	var startingFuelStr string
	var startingFuel float64
	fmt.Printf("Enter the amount of fuel you have available (in million litres):\n> ")
	fmt.Scan(&startingFuelStr)
	startingFuel, _ = strconv.ParseFloat(startingFuelStr, 64)
	if startingFuel <= 0 {
		fmt.Printf("Invalid choice!\nTry again\n\n")
		retries++
		if retries < 3 {
			inputStartingFuel()
		} else {
			fmt.Printf("Too many unsuccessful attempts\nExiting...\n")
			os.Exit(1)
		}
	}
	return startingFuel
}

//Ask user to choose which planet to fly to
func choosePlanet() string {
	var planetNumStr string
	var planetChoice string
	var planetNum int
	listOfPlanets := [8]string{"Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}
	fmt.Printf("Choose the number for the planet you would like to visit:\n1. %v\n2. %v\n3. %v\n4. %v\n5. %v\n6. %v\n7. %v\n8. %v\n\n> ", listOfPlanets[0], listOfPlanets[1], listOfPlanets[2], listOfPlanets[3], listOfPlanets[4], listOfPlanets[5], listOfPlanets[6], listOfPlanets[7])
	fmt.Scan(&planetNumStr)
	fmt.Printf("\n")
	planetNum, _ = strconv.Atoi(planetNumStr)
	if planetNum <= 8 && planetNum > 0 {
		planetChoice = listOfPlanets[planetNum-1]
	} else {
		fmt.Printf("Invalid choice!\nTry again\n\n")
		retries++
		if retries < 3 {
			choosePlanet()
		} else {
			fmt.Printf("Too many unsuccessful attempts\nExiting...\n")
			os.Exit(1)
		}
	}
	return planetChoice
}

// Calculate amount of fuel required to reach chosen planet (in millio litres)
func calculateFuelRequired(planet string) (fuel float64) {
	switch planet {
	case "Mercury":
		fuel = 200
	case "Venus":
		fuel = 100
	case "Mars":
		fuel = 100
	case "Jupiter":
		fuel = 200
	case "Saturn":
		fuel = 300
	case "Uranus":
		fuel = 400
	case "Neptune":
		fuel = 500
	case "Pluto":
		fuel = 600
	default:
		fuel = 0
	}
	return fuel
}

// Welcome greeting to chosen planet
func greetPlanet(planet string) {
	fmt.Printf("Welcome to %v!\n", planet)
}

// Inform about not enough fuel remaining to fly to chosen planet
func cantFly(planet string) {
	fmt.Printf("You don't have enough available fuel to reach %v!\n", planet)
}

// Check if possible to fly to chosen planet and return fuel remaining after reaching said planet
func flyToPlanet(planet string, fuel float64) float64 {
	var fuelRemaining, fuelCost float64
	fuelRemaining = fuel
	fuelCost = calculateFuelRequired(planet)

	if fuelRemaining >= fuelCost {
		if planet != "" {
			greetPlanet(planet)
		}
		fuelRemaining -= fuelCost
	} else {
		cantFly(planet)
	}

	return fuelRemaining
}

//Program main() function
func main() {
	// Choose planet and enter default amount of fuel
	startingFuel := inputStartingFuel()
	fuel := startingFuel
	planetChoice := choosePlanet()
	// And then liftoff!
	fuel = flyToPlanet(planetChoice, fuel)
	// Print remaining amount of fuel
	fuelGauge(fuel, startingFuel)
}
