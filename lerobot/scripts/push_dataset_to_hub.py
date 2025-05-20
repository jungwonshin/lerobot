#!/usr/bin/env python

# Example:
# python -m lerobot.scripts.push_dataset_to_hub 
# --path /Users/jws/.cache/huggingface/lerobot/jwshin95/subtask1_nobase 
# --repo_id jwshin95/subtask1_nobasev4

import argparse
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

def parse_args():
    parser = argparse.ArgumentParser(description="Push a local HuggingFace dataset to the Hub")
    parser.add_argument(
        "--path", 
        type=str, 
        required=True, 
        help="Local directory containing the dataset"
    )
    parser.add_argument(
        "--repo_id", 
        type=str, 
        required=True, 
        help="Repository ID on HuggingFace Hub (format: username/dataset_name)"
    )
    parser.add_argument(
        "--private", 
        action="store_true", 
        help="Whether to make the dataset private"
    )

    parser.add_argument(
        "--branch",
        type=bool
    )
    # Removed unused arguments
    return parser.parse_args()

def main():
    args = parse_args()
    
    print(f"Loading dataset from {args.path}...")
    dataset = LeRobotDataset(
        repo_id=args.repo_id,
        root=args.path
    )
    
    print(f"Pushing dataset to {args.repo_id}...")
    dataset.push_to_hub(
        args.repo_id,
        private=args.private
    )
    print("Dataset successfully pushed to Hub!")
    
    return 0

if __name__ == "__main__":
    main()
