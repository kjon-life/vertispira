#!/bin/bash
# validate-version.sh

validate_version() {
    local version=$1
    local current_quarter=$(date +%m)
    local current_year=$(date +%Y)
    
    # Extract n and m from version 0.n.m
    local n=$(echo $version | cut -d. -f2)
    local m=$(echo $version | cut -d. -f3)
    
    # Calculate expected n based on current quarter
    # March (3) = 1, June (6) = 2, September (9) = 3, December (12) = 4
    local expected_n=$(( (current_quarter + 2) / 3 ))
    
    if [[ $m == "0" ]]; then
        # Feature release - must align with quarters
        if [[ $n != $expected_n ]]; then
            echo "Error: Feature release version 0.$n.0 doesn't align with current quarter ($current_quarter)"
            return 1
        fi
    else
        # Bug fix release - must be for current or previous quarter
        if [[ $n != $expected_n && $n != $(($expected_n - 1)) ]]; then
            echo "Error: Bug fix release version 0.$n.$m is not for current or previous quarter"
            return 1
        fi
    fi
    
    return 0
}