use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io;
use std::io::BufRead;

#[derive(Clone, Copy, Hash, Eq, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

fn manhattan(a: Point, b: Point) -> i32 {
    return (a.x - b.x).abs() + (a.y - b.y).abs();
}

// type Range = std::ops::Range<i32>;
// but then I lose `Copy` and things get uglier (and slower) elsewhere
#[derive(Clone, Copy, Hash, Eq, PartialEq)]
struct Range {
    start: i32,
    stop: i32,
}

impl Range {
    fn contains(&self, x: i32) -> bool {
        return self.start <= x && x < self.stop;
    }

    fn length(&self) -> i32 {
        return self.stop - self.start;
    }

    fn union(&self, other: Range) -> Option<Range> {
        // overlapping ranges
        if self.contains(other.start) {
            if other.stop > self.stop {
                return Some(Range {
                    start: self.start,
                    stop: other.stop,
                });
            }
            return Some(*self);
        }
        if other.contains(self.start) {
            if self.stop > other.stop {
                return Some(Range {
                    start: other.start,
                    stop: self.stop,
                });
            }
            return Some(other);
        }
        // adjoining ranges
        if other.start == self.stop {
            return Some(Range {
                start: self.start,
                stop: other.stop,
            });
        }
        if self.start == other.stop {
            return Some(Range {
                start: other.start,
                stop: self.stop,
            });
        }
        // disjoint
        return None;
    }
}

fn append_range(ranges: &mut Vec<Range>, new_range: Range) {
    for (i, r) in ranges.iter().enumerate() {
        if let Some(u) = r.union(new_range) {
            if u == *r {
                return;
            }
            ranges.remove(i);
            append_range(ranges, u);
            return;
        }
    }
    ranges.push(new_range);
}

fn collect_ranges(sensors: &HashMap<Point, i32>, y: i32) -> Vec<Range> {
    let mut ranges: Vec<Range> = vec![];
    for (sensor, strength) in sensors {
        let s = strength - (y - sensor.y).abs();
        if s >= 0 {
            append_range(
                &mut ranges,
                Range {
                    start: sensor.x - s,
                    stop: sensor.x + s + 1,
                },
            );
        }
    }
    return ranges;
}

pub fn main() {
    let mut sensors = HashMap::new();
    let mut beacons = HashSet::new();

    let file = File::open("../day15_input.txt").unwrap();
    let pattern =
        Regex::new("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)")
            .unwrap();
    for line in io::BufReader::new(file).lines() {
        if let Some(captures) = pattern.captures(line.unwrap().as_str()) {
            let sx = captures[1].parse::<i32>().unwrap();
            let sy = captures[2].parse::<i32>().unwrap();
            let bx = captures[3].parse::<i32>().unwrap();
            let by = captures[4].parse::<i32>().unwrap();
            let sensor = Point { x: sx, y: sy };
            let beacon = Point { x: bx, y: by };
            let distance = manhattan(sensor, beacon);
            sensors.insert(sensor, distance);
            beacons.insert(beacon);
        }
    }

    let mut part1 = 0;
    for r in collect_ranges(&sensors, 2000000) {
        part1 += r.length();
    }
    for b in beacons {
        if b.y == 2000000 {
            part1 -= 1
        }
    }
    println!("{}", part1);

    let xs = Range {
        start: 0,
        stop: 4000001,
    };
    for y in 0..4000001 {
        let mut ranges = collect_ranges(&sensors, y);
        ranges.sort_by_key(|r| r.start);
        for r in ranges {
            if r.union(xs) != Some(r) {
                let x = r.stop;
                println!("{}", 4000000 * (x as i64) + (y as i64));
                return;
            }
        }
    }
}
