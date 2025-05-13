#!/bin/bash
##The `until` loop is similar to the `while` loop but it executes as long as the condition is false (essentially the inverse of `while`).

##Example: Wait Until a Condition is Met**

#!/bin/bash

COUNT=2

until [ "$COUNT" -gt 9 ]; do
    echo "Count is $COUNT"
    COUNT=$((COUNT + 2))
done


##Note**: In many scenarios, `until` can be used similarly to a `do-while` loop in other languages.