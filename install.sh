#!/bin/bash

apt update && apt upgrade && wget https://raw.githubusercontent.com/Interceptv/scanny/main/instcheck.sh && chmod 777 instcheck.sh && ./instcheck.sh
