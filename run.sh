#!/bin/bash

parent_name="susu"
short_parent_name="susu"
module_name="testserver"

it=$1

if [ ${#it} == 0 ];
then
    it="-d"
fi

docker run $it --rm \
--name "${short_parent_name}_${module_name}_1" \
-p 8001:8001 \
"${parent_name}/${module_name}"