#!/bin/bash

parent_name="susu"
module_name="testserver"

docker build \
-t "${parent_name}/${module_name}" \
.