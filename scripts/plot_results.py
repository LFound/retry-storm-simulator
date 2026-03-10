import csv
import os
import matplotlib.pyplot as plt

RESULTS_FILE = "results/retry_storm_results.csv"


def main():
    os.makedirs("results", exist_ok=True)

    failure_rates = []
    total_attempts = []
    permanent_failures = []

    with open(RESULTS_FILE, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            failure_rates.append(float(row["failure_rate"]))
            total_attempts.append(int(row["total_attempts"]))
            permanent_failures.append(int(row["permanent_failures"]))

    plt.figure()
    plt.plot(failure_rates, total_attempts, marker="o")
    plt.xlabel("Failure Rate")
    plt.ylabel("Total Attempts")
    plt.title("Total Attempts vs Failure Rate")
    plt.tight_layout()
    plt.savefig("results/total_attempts_vs_failure_rate.png")
    plt.close()

    plt.figure()
    plt.plot(failure_rates, permanent_failures, marker="o")
    plt.xlabel("Failure Rate")
    plt.ylabel("Permanent Failures")
    plt.title("Permanent Failures vs Failure Rate")
    plt.tight_layout()
    plt.savefig("results/permanent_failures_vs_failure_rate.png")
    plt.close()

    print("Saved plots:")
    print("- results/total_attempts_vs_failure_rate.png")
    print("- results/permanent_failures_vs_failure_rate.png")


if __name__ == "__main__":
    main()