# Codrone Python API

---

## pair()

### Description

This function connects your controller with the program.

You shouldn't tell the LLM about this function. You should only call it once at the start of the program.

### Usage

```pair()```

#### Parameters

None

#### Returns

None

---

## close()

### Description

This function closes the connection of your controller with the program.

You shouldn't tell the LLM about this function. You should only call it once at the start of the program.

### Usage

```close()```

#### Parameters

None

#### Returns

None

---

## takeoff()

### Description

This function makes the drone takeoff at an average height of 80 centimeters and hover. The drone will always hover for 1 second in order to stabilize before it executes the next command. NOTE: The takeoff parameters or height cannot be modified.

### Usage

```takeoff()```

#### Parameters

None

#### Returns

None

---

## land()

### Description

This function makes the drone stop all commands, hover, and make a soft landing where it is.

### Usage

```land()```

#### Parameters

None

#### Returns

None

---

## emergency_stop()

### Description

This function immediately stops all commands and motors, so the drone will stop flying immediately.

### Usage

```emergency_stop()```

#### Parameters

None

#### Returns

None

---

## hover()

### Description

This function makes the drone hover for a given amount of time. If given no parameters, it will hover indefinitely until given a another command.

### Usage

```hover(int seconds)```

#### Parameters

integer duration: duration of the hovering in seconds

#### Returns

None

---

## avoid_wall()

### Description

A looped method that makes the drone fly forward until it reaches a desired distance based on the front range sensor. The range of front sensor is from 0cm-100cm

### Usage

```avoid_wall()```

```avoid_wall(timeout)```

```avoid_wall(distance)```

```avoid_wall(timeout, distance)```

#### Parameters

integer timeout: timeout is an optional parameter that is the duration in seconds that the function will run. the default value is 2

integer distance: distance is an optional parameter that is the distance in centimeters the drone will stop at in front of an object. the default value is 70

#### Returns

None

---

## keep_distance()

### Description

A looped method that makes the drone fly forward until it reaches a desired distance. Once the desired distance in reached the drone will maintain that distance. The sensor range is up to 150 cm.

### Usage

```keep_distance()```

```keep_distance(timeout)```

```keep_distance(distance)```

```keep_distance(timeout, distance)```

#### Parameters

integer timeout: the duration in seconds that the function will execute. The default value is 2 seconds.

integer distance: the distance in centimeters the drone will stop and maintain distance in front of an object. The default value is 50 centimeters.

#### Returns

None

---

## move_forward()

### Description

Moves the drone forward for a given distance. For the best performance, please make sure your drone is flying over a well-lit, patterned surface.

### Usage

```move_forward(distance)```

```move_forward(distance, unit, speed)```

#### Parameters

float distance: the distance to travel.

string unit: The unit of measurement for the distance flown. Available units are "cm" (centimeter), "ft" (feet), "in" (inches), "m" (meter).

float speed: The drone's speed, in meters per second. The default speed is 1.0 meter per second. Max is 2.0 meters per second.

#### Returns

None

---

## move_backward()

### Description

Moves the drone backward for a given distance. For the best performance, please make sure your drone is flying over a well-lit, patterned surface.

### Usage

```move_backward(distance)```

```move_backward(distance, unit, speed)```

#### Parameters

float distance: the distance to travel.

string unit: The unit of measurement for the distance flown. Available units are "cm" (centimeter), "ft" (feet), "in" (inches), "m" (meter).

float speed: The drone's speed, in meters per second. The default speed is 1.0 meter per second. Max is 2.0 meters per second.

#### Returns

None

---

## move_left()

### Description

Moves the drone left for a given distance. For the best performance, please make sure your drone is flying over a well-lit, patterned surface.

### Usage

```move_left(distance)```

```move_left(distance, unit, speed)```

#### Parameters

float distance: the distance to travel.

string unit: The unit of measurement for the distance flown. Available units are "cm" (centimeter), "ft" (feet), "in" (inches), "m" (meter).

float speed: The drone's speed, in meters per second. The default speed is 1.0 meter per second. Max is 2.0 meters per second.

#### Returns

None

---

## move_right()

### Description

Moves the drone right for a given distance. For the best performance, please make sure your drone is flying over a well-lit, patterned surface.

### Usage

```move_right(distance)```

```move_right(distance, unit, speed)```

#### Parameters

float distance: the distance to travel.

string unit: The unit of measurement for the distance flown. Available units are "cm" (centimeter), "ft" (feet), "in" (inches), "m" (meter).

float speed: The drone's speed, in meters per second. The default speed is 1.0 meter per second. Max is 2.0 meters per second.

#### Returns

None

---

## move_distance()

### Description

Moves the drone by the specified distances along the x, y, and z axes, relative to its current position and heading. If two or more distances have non-zero values, the function will move the drone by these distances simultaneously. For the best performance, please make sure your drone is flying over a well-lit, patterned surface.

### Usage

```move_distance(positionX, positionY, positionZ, velocity)```

#### Parameters

float positionX: The distance to travel in the x-direction, in meters. This corresponds to forward/backward movement.

float positionY: The distance to travel in the y-direction, in meters. This corresponds to left/right movement.

float positionZ: The distance to travel in the z-direction, in meters. This corresponds to vertical movement.

float velocity: The drone's velocity, in meters per second. The default velocity is 1.0 meter per second. Max is 2.0 meters per second.

#### Returns

None

---

## turn_degree()

### Description

Turns right or left with absolute reference frame to drone's initial heading. Positive degrees turn to the left and negative degrees turn to the right.

### Usage

```turn_degree(degree, timeout, p_value)```

#### Parameters

integer degree: angle of turn in degrees (-180 - 180)

integer timeout: optional parameter that is duration in seconds that drone will try to turn. default value is 3.

integer p_value: optional parameter that is the gain of the proportional controller, if this increased CDE will turn quicker, the smaller the slower. default value is 10.

#### Returns

None

---

## turn_left()

### Description

Turns the drone left using the built in gyroscope. The default degree is 90.

### Usage

```turn_left()```

```turn_left(degree)```

```turn_left(timeout)```

```turn_left(degree, timeout)```

#### Parameters

integer degree: optional parameter that turns the drone in the given degree. default value is 90.

integer timeout: optional parameter that is duration in seconds that drone will try to turn. default value is 3.

#### Returns

None

---

## turn_right()

### Description

Turns the drone_right using the built in gyroscope. The default degree is 90.

### Usage

```turn_right()```

```turn_right(degree)```

```turn_right(timeout)```

```turn_right(degree, timeout)```

#### Parameters

integer degree: optional parameter that turns the drone in the given degree. default value is 90.

integer timeout: optional parameter that is duration in seconds that drone will try to turn. default value is 3.

#### Returns

None