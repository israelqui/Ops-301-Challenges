#!/usr/bin/env python3

# Script: Psutil
# Author: Israel Quirola
# Date: Dec 11, 2023

import psutil

def get_system_info():
    cpu_times = psutil.cpu_times()

    # Time spent by normal processes executing in user mode
    user_time = cpu_times.user

    # Time spent by processes executing in kernel mode
    kernel_time = cpu_times.system

    # Time when system was idle
    idle_time = cpu_times.idle

    # Time spent by priority processes executing in user mode
    priority_user_time = cpu_times.nice

    # Time spent waiting for I/O to complete
    io_wait_time = cpu_times.iowait

    # Time spent for servicing hardware interrupts
    irq_time = cpu_times.irq

    # Time spent for servicing software interrupts
    softirq_time = cpu_times.softirq

    # Time spent by other operating systems running in a virtualized environment
    steal_time = cpu_times.steal

    # Time spent running a virtual CPU for guest operating systems
    guest_time = cpu_times.guest

    return {
        "User Time": user_time,
        "Kernel Time": kernel_time,
        "Idle Time": idle_time,
        "Priority User Time": priority_user_time,
        "IO Wait Time": io_wait_time,
        "IRQ Time": irq_time,
        "SoftIRQ Time": softirq_time,
        "Steal Time": steal_time,
        "Guest Time": guest_time
    }

# Fetch and print system information
system_info = get_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")
