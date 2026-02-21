import sys

print("=== Player Score Analytics ===")
if len(sys.argv) <= 1:
    print("No scores provided. Usage:"
          " python3 ft_score_analytics.py <score1> <score2> ...")
else:
    try:
        list = []
        i = 1
        while i < len(sys.argv):
            list = list + [int(sys.argv[i])]
            i += 1
        print(f"Scores processed: {list}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(list)}")
        print(f"Average score: {sum(list) / (len(sys.argv) - 1)}")
        print(f"High score: {max(list)}")
        print(f"Low score: {min(list)}")
        print(f"Score range: {max(list) - min(list)}\n")
    except ValueError:
        print("invalid scores")
    except Exception as Error:
        print(f"Unexpected error: {Error}")
