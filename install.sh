#!/bin/bash

apt update -y && apt upgrade -y && wget https://raw.githubusercontent.com/Interceptv/scanny/main/instcheck.sh && chmod 777 instcheck.sh && ./instcheck.sh
