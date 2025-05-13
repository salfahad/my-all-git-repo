#!/bin/bash
 ##The `case` statement allows you to execute different blocks of code based on the value of a variable.

##Example: Check a Variable's Value**

Student="Fahad"

case $Student in
    "Bilal")
        echo "Option Ball selected."
        ;;
    "Saad")
        echo "Option Car selected."
        ;;
    "Jahan")
        echo "Option Plane selected."
        ;;
    *)
        echo "Invalid option."
        ;;
esac

Student="Fahad"

case $Student in
    "Bilal")
        echo "Option Ball selected."
        ;;
    "Fahad")
        echo "Option Car selected."
        ;;
    "Jahan")
        echo "Option Plane selected."
        ;;
    *)
        echo "Invalid option."
        ;;
esac