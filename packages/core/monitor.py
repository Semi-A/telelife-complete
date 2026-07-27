import psutil
import os


def get_system_usage():
    process = psutil.Process(os.getpid())

    memory = process.memory_info().rss / 1024 / 1024  # MB

    cpu = process.cpu_percent(interval=0.1)

    return {
        "cpu_percent": round(cpu, 2),
        "ram_mb": round(memory, 2),
        "ram_percent": round(
            psutil.virtual_memory().percent,
            2
        ),
        "total_ram_mb": round(
            psutil.virtual_memory().total / 1024 / 1024,
            2
        )
    }