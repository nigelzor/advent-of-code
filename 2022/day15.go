package main

import (
	"bufio"
	"image"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func manhattan(a image.Point, b image.Point) int {
	return abs(a.X-b.X) + abs(a.Y-b.Y)
}

type Range struct {
	start int
	stop  int
}

func (r *Range) contains(x int) bool {
	return r.start <= x && x < r.stop
}

func (r *Range) length() int {
	return r.stop - r.start
}

func (r *Range) union(other *Range) *Range {
	// overlapping ranges
	if r.contains(other.start) {
		if other.stop > r.stop {
			return &Range{r.start, other.stop}
		}
		return r
	}
	if other.contains(r.start) {
		if r.stop > other.stop {
			return &Range{other.start, r.stop}
		}
		return other
	}
	// adjoining ranges
	if other.start == r.stop {
		return &Range{r.start, other.stop}
	}
	if r.start == other.stop {
		return &Range{other.start, r.stop}
	}
	// disjoint
	return nil
}

func appendRange(ranges []Range, newRange *Range) []Range {
	for i, r := range ranges {
		u := r.union(newRange)
		if u == &r {
			return ranges
		}
		if u != nil {
			ranges = append(ranges[:i], ranges[i+1:]...)
			return appendRange(ranges, u)
		}
	}
	return append(ranges, *newRange)
}

func collectRanges(sensors map[image.Point]int, y int) []Range {
	var ranges []Range
	for sensor, strength := range sensors {
		strength -= abs(y - sensor.Y)
		if strength >= 0 {
			ranges = appendRange(ranges, &Range{sensor.X - strength, sensor.X + strength + 1})
		}
	}
	return ranges
}

func main() {
	sensors := make(map[image.Point]int)
	beacons := make(map[image.Point]bool)

	file, err := os.Open("day15_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	pattern := regexp.MustCompile("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		match := pattern.FindStringSubmatch(scanner.Text())
		if len(match) != 5 {
			log.Fatal("Expected 5 matches, got ", len(match))
		}
		sx, err := strconv.Atoi(match[1])
		if err != nil {
			log.Fatal(err)
		}
		sy, err := strconv.Atoi(match[2])
		if err != nil {
			log.Fatal(err)
		}
		bx, err := strconv.Atoi(match[3])
		if err != nil {
			log.Fatal(err)
		}
		by, err := strconv.Atoi(match[4])
		if err != nil {
			log.Fatal(err)
		}
		sensor := image.Pt(sx, sy)
		beacon := image.Pt(bx, by)
		distance := manhattan(sensor, beacon)
		sensors[sensor] = distance
		beacons[beacon] = true
	}

	part1 := 0
	for _, r := range collectRanges(sensors, 2000000) {
		part1 += r.length()
	}
	for b := range beacons {
		if b.Y == 2000000 {
			part1 -= 1
		}
	}
	println(part1)

	xs := Range{0, 4000000 + 1}
	for y := 0; y <= 4000000; y++ {
		ranges := collectRanges(sensors, y)
		sort.Slice(ranges, func(i, j int) bool {
			return ranges[i].start < ranges[j].start
		})
		for _, r := range ranges {
			if r.union(&xs) != &r {
				x := r.stop
				println(4000000*x + y)
				return
			}
		}
	}
}
