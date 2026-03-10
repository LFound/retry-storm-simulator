import csv
import os
from sim.engine import Simulation


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)

    failure_rates = [0.1, 0.3, 0.5, 0.7]
    all_results = []

    print("Failure Rate | Created | Attempts | Completed | Failures | Retries | Permanent Failures | Max Queue")
    print("-" * 105)

    for failure_rate in failure_rates:
        sim = Simulation(total_jobs=50, failure_chance=failure_rate, seed=42)
        results = sim.run()
        results["failure_rate"] = failure_rate
        all_results.append(results)

        print(
            f"{failure_rate:>12.2f} | "
            f"{results['jobs_created']:>7} | "
            f"{results['total_attempts']:>8} | "
            f"{results['jobs_completed']:>9} | "
            f"{results['failures']:>8} | "
            f"{results['retries']:>7} | "
            f"{results['permanent_failures']:>18} | "
            f"{results['max_queue_depth']:>9}"
        )

    with open("results/retry_storm_results.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "failure_rate",
                "jobs_created",
                "total_attempts",
                "jobs_completed",
                "failures",
                "retries",
                "permanent_failures",
                "max_queue_depth",
            ],
        )
        writer.writeheader()
        writer.writerows(all_results)

    print("\nResults saved to results/retry_storm_results.csv")