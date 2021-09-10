package main

import "fmt"

// Print fuel left
func fuelGauge(fuel int) {
  fmt.Printf("Fuel Remaining: %v gallons\n", fuel)
}

// Calculate amount of fuel required
func calculateFuel(planet string) (fuel int) {
  switch planet {
    case "Venus":
      fuel = 300000
    case "Mercury":
      fuel = 500000
    case "Mars":
      fuel = 700000
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
func cantFly() {
  fmt.Println("We do not have the available fuel to fly there.")
}

// Check if possible to fly to chosen planet and return fuel remaining after travelling to said planet
func flyToPlanet(planet string, fuel int) int {
  var fuelRemaining, fuelCost int
  fuelRemaining = fuel
  fuelCost = calculateFuel(planet)

  if fuelRemaining >= fuelCost {
    greetPlanet(planet)
    fuelRemaining -= fuelCost
  } else {
    cantFly()
  }

  return fuelRemaining
}

func main() {
  // Choose planet and enter default amount of fuel
  fuel := 1000000
  planetChoice := "Venus"
  // And then liftoff!
  fuel = flyToPlanet(planetChoice, fuel)
  // Print remaining amount of fuel
  fuelGauge(fuel)
}
