"""CLI for drug-discovery-ai."""
import sys, json, argparse
from .core import DrugDiscoveryAi

def main():
    parser = argparse.ArgumentParser(description="AI-powered drug discovery — molecular generation, property prediction, and docking")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = DrugDiscoveryAi()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.search(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"drug-discovery-ai v0.1.0 — AI-powered drug discovery — molecular generation, property prediction, and docking")

if __name__ == "__main__":
    main()
